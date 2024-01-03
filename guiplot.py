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
    
leftPane = [
    [sg.Text("Plot")],
    [sg.Canvas(key="-CANVAS-")],]
rightPane = [
    [sg.Text("x limits")],
    [sg.Slider( orientation = "horizontal",key = "defstart",range = (-100,0),default_value = -3), 
       sg.Slider( orientation = "horizontal",key = "defend",range = (0,100),default_value = 3) ],
    [sg.Text("y limits")],    
    [sg.Slider( orientation = "horizontal",key = "ystart",range = (-100,0),default_value = -4), 
       sg.Slider( orientation = "horizontal",key = "yend",range = (0,100),default_value = 10) ],       
    [sg.Text("Formula")],         
    [sg.In("sin (x)", key='expression')], 
    [sg.Canvas(key="-CANVAS-")],    
    [sg.Button("Plot")],
    [sg.Button("Quit")],]

layout = [
  [sg.Column(leftPane, element_justification='c' ),sg.Column(rightPane, element_justification='c' ),]
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
    try:
       if event == "Plot":
           print ("plot button", values['expression'])       
           operand =exp.parse(values['expression'])
    except (Exp.ExpressionError,) as e:
      sg.popup("expression error" + str(e))  
      
         
    ax.set(xlim=[values["defstart"], values["defend"]], ylim=[values["ystart"], values["yend"]])
        
    xvals =np.linspace(values["defstart"],values["defend"],500 )
    yvals = []
        
    try:
      for x in xvals:
          yvals.append(operand.eval({"x":x}))
      line2.set_xdata(xvals)
      line2.set_ydata(yvals)
      update_figure(figureCanvas)
    except (KeyError, TypeError,ValueError,) as e:
      sg.popup("Formula cannot be evaluated. " + str(e))     
        
window.close()
