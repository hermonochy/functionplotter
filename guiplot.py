from matplotlib.figure import Figure 
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
import py_expression.core
from py_expression.core import Exp
matplotlib.use("TkAgg")

MAXPLOTLINES=10

exp = Exp()

fig, ax = plt.subplots()
t = np.arange(0, 3, .01)

line2 = []
for i in range(0,MAXPLOTLINES):
  line = ax.plot(t, 2 * np.sin(2 * np.pi * t))[0]
  line2.append(line)
  
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
    [sg.Text("Controls")],
    [sg.Text('_'*50)],
    [sg.Text("X limits")],
    [sg.Slider( orientation = "horizontal",key = "xstart",range = (-100,0),default_value = -3), 
       sg.Slider( orientation = "horizontal",key = "xend",range = (0,100),default_value = 3) ],
    [sg.Text('_'*40)],    
    [sg.Text("Y limits")],    
    [sg.Slider( orientation = "horizontal",key = "ystart",range = (-100,0),default_value = -4), 
       sg.Slider( orientation = "horizontal",key = "yend",range = (0,100),default_value = 10) ],
    [sg.Text('_'*40)],          
    [sg.Text("Formula")],         
    [sg.In("sin (x)", key='expression')], 
    [sg.Canvas(key="-CANVAS-")],    
    [sg.Button("Plot")],
    [sg.Button("Quit")],]

layout = [
  [sg.Column(leftPane, element_justification='c' ),sg.Column(rightPane, element_justification='c' ),]
]

window = sg.Window(
    "Formula Plotter",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)
window['xstart'].bind('<ButtonRelease-1>', ' Release')
window['xend'].bind('<ButtonRelease-1>', ' Release')
window['ystart'].bind('<ButtonRelease-1>', ' Release')
window['yend'].bind('<ButtonRelease-1>', ' Release')


figureCanvas = draw_figure(window["-CANVAS-"].TKCanvas, fig)

while True:
    event, values = window.read()
    print ("event loop info: ",event,values)
    if event == "Quit" or event == sg.WIN_CLOSED:
        break
    if event == "Plot":
        for l in line2:
           l.set_xdata(None)
           l.set_ydata(None)
        print ("plot button", values['expression'])
    try:       
      expressionListString = values['expression']
      expressionList = expressionListString.split (',')
      operand = []
      for i in range(0,len(expressionList)):
           operand.append(exp.parse(expressionList[i]))
    except (py_expression.core.ExpressionError,) as e:
      sg.popup("expression error" + str(e))  
      continue
                                                          
    ax.set(xlim=[values["xstart"], values["xend"]], ylim=[values["ystart"], values["yend"]])
                                   
    xvals =np.linspace(values["xstart"],values["xend"],500 )
    yvals = []
                                                             
    try:
      for i in range(0,len(operand)):
        yvals.append([])
        for x in xvals:
            yvals[i].append(operand[i].eval({"x":x}))
        
        line2[i].set_xdata(xvals)
        line2[i].set_ydata(yvals[i])
      

      
      update_figure(figureCanvas)
    except (KeyError, TypeError,ValueError,) as e:
      sg.popup("Formula cannot be evaluated. " + str(e))     
      continue  
window.close()
