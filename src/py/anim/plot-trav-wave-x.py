#	
#	plot-trav-wave-x
#	Plot spatial profile of a travelling wave 
#	
#	Sparisoma Viridi | https://butiran.github.io
#	
#	20210206
#	0525 Learn to plot from [1].
#	0538 Learn from [2].
#	0544 Use \pi from [3].
#	0557 Can draw a sine function.
#	0604 Learn add_subplot [4].
#	0618 Just know this one [5].
#	0639 Read style in plotting [6].
#	0654 Give comments for clearer reading of the code.
#	0702 Add axis label [7].
#	
#	References
#	1. url https://matplotlib.org/gallery/animation
#	   /double_pendulum_animated_sgskip.html [20210205].
#	2. The SciPy community, "numpy.arange", NumPy, 31 Jan 2021,
#	   url https://numpy.org/doc/stable/reference/generated
#	   /numpy.arange.html [20210206].
#	3. The SciPy community, "Constants", NumPy, 31 Jan 2021,
#	   url https://numpy.org/doc/stable/reference
#	   /constants.html [20210206].
#	4. John Hunter, Darren Dale, Eric Firing, Michael Droettboom,
#	   and the Matplotlib development team, "matplotlib.pyplot
#	   .subplot", 5 Jan 2020, url https://matplotlib.org/3.1.1
#	   /api/_as_gen/matplotlib.pyplot.subplot.html [20210206].
#	5. Guido Mocha, "Answer to ''", StackOverflow, 9 Sep 2019 at 
#	   13:55, url https://stackoverflow.com/a/57855482 [20210206].
#	6. John Hunter, Darren Dale, Eric Firing, Michael Droettboom,
#	   and the Matplotlib development team, "matplotlib.axes
#	   .Axes.plot", 5 Jan 2020, url https://matplotlib.org/3.1.1
#	   /api/_as_gen/matplotlib.axes.Axes.plot.html [20210206].
#	7. John Hunter, Darren Dale, Eric Firing, Michael Droettboom,
#	   and the Matplotlib development team, "Simple axes labels",
#	   18 May 2019, url https://matplotlib.org/3.1.1/api/_as_gen
#	   /matplotlib.axes.Axes.plot.html [20210206].
#	

# Import required libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt


# Define a function for travelling wave
def travwave(x, t):
	A = 0.2
	T = 1
	_l = 1
	_w = 2 * np.pi / T
	k = 2 * np.pi / _l
	_varphi0 = np.pi
	y = A * sin(_w * t - k * x + _varphi0)
	return y


# Set observation time
t = 0.50

# Create x and y data
x = np.arange(0, 2, 0.04)
y = travwave(x, t)

# Get figure for plotting
fig = plt.figure()

# Configure axes
ax = fig.add_subplot(
	111,
	autoscale_on=True,
	xlim=(0, 2),
	ylim=(-0.2, 0.2)
)
ax.set_aspect('equal')
ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')

# Set style for plotting
line, = ax.plot([], [], 'sr-', lw=1, ms=4)
time_template = 't = %.2f s'
time_text = ax.text(0.8, 0.8, '', transform=ax.transAxes)

# Set data and time information
line.set_data(x, y)
time_text.set_text(time_template % t)

# Show plotting result
plt.show()
