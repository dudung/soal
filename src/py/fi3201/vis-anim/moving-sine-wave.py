#	
#	moving-sine-wave.py
#	Produce a GIF file of moving sine wave
#	
#	Sparisoma Viridi | https://butiran.github.io
#	
#	Execute: py moving-sine-wave.py
#	Output: sine_wave.gif
#	
#	20210212
#	1108 Create this by modifying [1].
#	1113 Try some other styles [2].
#	1621 Add some comments.
#	1732 Function wave does not animate.
#	
#	References
#	1. Parul Pandey, "Animations with Mathplotlib", Towards Data Science, 14 Apr 2019, url https://towardsdatascience.com/animation-with-matplotlib-d96375c5442c [20210212].
#	2. John Hunter, Darren Dale, Eric Firing, Michael Droettboom, and Matplotlib development team, "Style sheets reference", Mathplotlib Version 3.1.2, 05 Jan 2020, url https://matplotlib.org/3.1.1/gallery/style_sheets/style_sheets_reference.html [20210212].
#	

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

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


def wave(x, t):
	A = 1.0
	_lambda = 1
	k = 2 * np.pi / _lambda
	T = 1
	_omega = 2 * np.pi / T
	y = A * np.sin(k * x - _omega *t)
	return y


def init():
	line.set_data([], [])
	return line,

def animate(i):
	x = np.linspace(0, 4, 100)
	y = 2 * np.sin(2 * np.pi * (x - 0.01 * i))
	#y = wave(x, i)
	line.set_data(x, y)
	return line,

anim = FuncAnimation(fig, animate, init_func=init, frames=20, interval=20, blit=True)

anim.save("sine_wave.gif", writer="imagemagick")