#	
#	plot-sine.py
#	Produce a PNG file of a sine
#	
#	Sparisoma Viridi | https://butiran.github.io
#	
#	Execute: py moving-sine-wave.py
#	Output: sine.png
#	
#	20210212
#	1901 Create this by modifying moving-sine-wave.py from [1].
#	1902 Remove FuncAnimation from matplotlib.animation.
#	1904 Can save as PNG as in [2].
#	
#	References
#	1. Parul Pandey, "Animations with Mathplotlib", Towards Data Science, 14 Apr 2019, url https://towardsdatascience.com/animation-with-matplotlib-d96375c5442c [20210212].
#	2. Yann, Bhargav Rao, "Answer to ''", StackOverflow, 01 Aug 2018 at 01:48, url https://stackoverflow.com/a/8827350 [20210212].
#	3. John Hunter, Darren Dale, Eric Firing, Michael Droettboom, and Matplotlib development team, "Style sheets reference", Mathplotlib Version 3.1.2, 05 Jan 2020, url https://matplotlib.org/3.1.1/gallery/style_sheets/style_sheets_reference.html [20210212].
#	

#	Import necessary packages
import numpy as np
from matplotlib import pyplot as plt

#	Define a function representing a static wave
def swave(x, t):
	A = 1.0
	_lambda = 1
	k = 2 * np.pi / _lambda
	T = 1
	_omega = 2 * np.pi / T
	y = A * np.sin(k * x - _omega *t)
	return y



#	Use style
plt.style.use("seaborn-pastel")

fig = plt.figure()

#	Set x range
xmin = 0
xmax = 4
xrange = (xmin, xmax)

#	Set y range
ymin = -2
ymax = 2
yrange = (ymin, ymax)

# Set x and y axes
ax = plt.axes(xlim=xrange, ylim=yrange)
line, = ax.plot([], [], lw=3)



t = 0
x = np.linspace(0, 4, 100)
y = swave(x, t)
line.set_data(x, y)

#	Save plot as PNG image
plt.savefig("sine.png")
