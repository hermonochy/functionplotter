from matplotlib.figure import Figure 
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
from py_expression.core import Exp
matplotlib.use("TkAgg")

exp = Exp()

fig, ax = plt.subplots()
t = np.arange(0, 3, .01)
line2 = ax.plot(t, 2 * np.sin(2 * np.pi * t))[0]

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

def update_figure(fg,):
    fg.draw()
    
layout = [
    [sg.Text("Plot test")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Slider( orientation = "horizontal",key = "defstart",range = (-100,0),default_value = -3), 
       sg.Slider( orientation = "horizontal",key = "defend",range = (0,100),default_value = 3) ],    
    [sg.In("sin (x)", key='expression')],    
    [sg.Button("Plot")],
    [sg.Button("Quit")],    
]

window = sg.Window(
    "Matplotlib Single Graph",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)

figureCanvas = draw_figure(window["-CANVAS-"].TKCanvas, fig)

while True:
    event, values = window.read()
    print ("event loop info: ",event,values)
    if event == "Quit" or event == sg.WIN_CLOSED:
        break

    if event == "Plot":
        print ("plot button", values['expression'])       
        operand =exp.parse(values['expression'])
        
        ax.set(xlim=[values["defstart"], values["defend"]], ylim=[-4, 10])
        
        xvals =np.linspace(values["defstart"],values["defend"],500 )
        yvals = []
        
        try:
          for x in xvals:
              yvals.append(operand.eval({"x":x}))
          line2.set_xdata(xvals)
          line2.set_ydata(yvals)
          update_figure(figureCanvas)
        except (KeyError, TypeError,ValueError) as e:
          sg.popup("Formula cannot be evaluated. " + str(e))     
        
window.close()
