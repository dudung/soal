#	
#	plot-sine-wave.py
#	Produce a PNG file of a sine wave plot
#	
#	Sparisoma Viridi | https://butiran.github.io
#	
#	Execute: py plot-sine-wave.py
#	Output: sine-t-<time>.png
#	
#	20210212
#	1901 Create this by modifying moving-sine-wave.py from [1].
#	1902 Remove FuncAnimation from matplotlib.animation.
#	1904 Can save as PNG as in [2].
#	1949 Add comments and can show figure, learn Line2D [3].
#	1955 Can set axes label [4].
#	2002 Show grid [5].
#	2011 Use arange but modify [6] from xtics to set_xtics.
#	2021 Add text box [7].
#	2027 Set figure size [8], but in inch?
#	2038 Convert time with certain precision for output [9].
#	2024 Change size for Jekyll blog, hopefully better.
#	2120 Add _varphi to the function wave.
#	
#	References
#	1. Parul Pandey, "Animations with Mathplotlib", Towards Data Science, 14 Apr 2019, url https://towardsdatascience.com/animation-with-matplotlib-d96375c5442c [20210212].
#	2. Yann, Bhargav Rao, "Answer to 'matplotlib savefig in jpeg format'", StackOverflow, 01 Aug 2018 at 01:48, url https://stackoverflow.com/a/8827350 [20210212].
#	3. SHUBHAMSINGH10, "Matplotlib.axes.Axes.plot() in Python", GeeksforGeeks, 12 Apr 2020, url https://www.geeksforgeeks.org/matplotlib-axes-axes-plot-in-python/ [20210212].
#	4. Luv Dhamija, "Answer to 'How to set X and Y axis Title in matplotlib.pyplot'", StackOverflow, 08 Jun 2020 at 06:29, url https://stackoverflow.com/a/62256244 [20210212].
#	5. Andrey Sobolev, Peter Mortensen, "Answer to 'How do I draw a grid onto a plot in Python?'", StackOverflow, 20 Mar 2017 at 17:42, url https://stackoverflow.com/a/8210686 [20210212].
#	6. unutbu, "Answer to 'Changing the “tick frequency” on x or y axis in matplotlib?'", StackOverflow, 26 Sep 20212 at 19:24, url https://stackoverflow.com/a/12608937 [20210212].
#	7. Anake, "Answer to 'automatically position text box in matplotlib'", StackOverflow, 29 Oct 2015 at 14:59, url https://stackoverflow.com/a/33417697 [20210212].
#	8. iPas, cbare, "Answer to 'How do you change the size of figures drawn with matplotlib?'", StackOverflow, 01 Feb 2015 at 06:21, url https://stackoverflow.com/a/24073700 [20210212].
#	9. HAL 9001, "Answer to 'Convert floating point number to a certain precision, and then copy to string'", StackOverflow, 06 Mar 2019 at 19:57, url https://stackoverflow.com/a/15263885 [20210212].
#	

#	Import necessary packages
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredText


#	Define a function representing a sine wave
def swave(x, t):
	A = 1.5
	_lambda = 1
	k = 2 * np.pi / _lambda
	T = 1
	_omega = 2 * np.pi / T
	_varphi = 0
	y = A * np.sin(k * x - _omega *t + _varphi)
	return y


#	Use style
plt.style.use("seaborn-pastel")

#	Create figure with certain size in inch
fig = plt.figure(figsize=(2.5, 2.5))

#	Set x range
xmin = 0
xmax = 2
xrange = (xmin, xmax)

#	Set y range
ymin = -2
ymax = 2
yrange = (ymin, ymax)

# Set x and y axes
ax = plt.axes(xlim=xrange, ylim=yrange)

#	Set axes label
ax.set_xlabel("x")
ax.set_ylabel("y")

#	Set xtics
dx = 0.5
xtics = np.arange(xmin, xmax + dx, dx)
ax.set_xticks(xtics)

#	Set ytics
dy = 1
ytics = np.arange(ymin, ymax + dy, dy)
ax.set_yticks(ytics)

#	Get Line2D object representing plotted data
line, = ax.plot([], [], lw=3)

#	Show grid or with True
plt.grid()

#	Create data
t = 0
x = np.linspace(0, 4, 100)
y = swave(x, t)
line.set_data(x, y)

# Add time information
ts = "{:.2f}".format(t)
atext = AnchoredText("t = " + ts, loc=1)
ax.add_artist(atext)

#	Save plot as PNG image
plt.savefig("sine-t-" + ts + ".png")

# Show plot
plt.show()
