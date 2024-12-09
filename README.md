# Math function plotter

## Overview
Plots mathematical functions inputted by user.
This works by evaluating a function with module [py-expression](https://pypi.org/project/py-expression/), creating a function graph with [Matplotlib](https://matplotlib.org/). This function graph is displayed in a Graphical User interface (GUI)[PySimpleGUI](https://www.pysimplegui.org). Sliders allow selection of ranges to be plotted. 

![The plotting window](images/plotterGUI.png)

## Installation
You should get a copy of the code using `git clone`.

`git clone https://github.com/hermonochy/functionplotter.git`

Then you need to go into the directory.

`cd functionplotter`

If `git` is not on your system, you may install it with
`sudo apt install git` on linux or with `brew install git` on Mac OS X.
If you use MS Windows, find out yourself. Hint: There is a git console for Windows. 

It's recommended to use [virtual environments](https://frankcorso.dev/setting-up-python-environment-venv-requirements.html) as below to avoid headaches with Python module conflicts. 

### Create a virtual environment for Python:
`python3 -m venv .` If this does not work, try `pip install venv`.

### Activate virtual environment:
`source ./bin/activate`

### Install dependencies inside virtual environment
`pip3 install -r requirements.txt `

### Start program
`python3 guiplot.py `

Enter the function you want to plot into the textfield and press the plot button.
Adjust area to plot with the sliders.

It is possible to plot more than one function. Separate them with a comma.
![The plotting window with multiple functions](images/plotterGUImultiPlot.png)

### Running the program again (if the virtual environment exists)
If running the program again on the same computer, the virtual environment does not need to be created and no packages need to be installed.
Just go to the directory of the program, activate the virtual environment, and start the program as before.
`source ./bin/activate`
`python3 guiplot.py `


## Future work
- More GUI error messages.
- 2D/3D plot
- Widgets for fine grained definition area.
- Saving and reloading functions.
- Saving plot.
