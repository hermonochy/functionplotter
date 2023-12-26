from matplotlib.figure import Figure 
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib



fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg
    
layout = [
    [sg.Text("Plot test")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.In("formel")],    
    [sg.Button("Plot")],
    [sg.Button("Ok")],    
]

# Create the form and show it without the plot
window = sg.Window(
    "Matplotlib Single Graph",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    print ("daddy is dumb",event,values)
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    # Add the plot to the window
    draw_figure(window["-CANVAS-"].TKCanvas, fig)





window.close()
