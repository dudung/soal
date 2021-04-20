# 
# plot-data-2.py
# Plot data using Mathplotlib to PNG as simple as possible
# 
# Sparisoma Viridi | https://github.com/dudung
#	
# 20210421
# 0319 Modify plot-data-2.py code for ML linear regression.
# 0335 Copy something from plot-two-mass-system-0.py code.
# 0340 Can work as previous one.
# 0503 Can show step, a, b; plot not work for data and curve.
# 
# References
# 1. url https://matplotlib.org/gallery/animation
#    /double_pendulum_animated_sgskip.html [20210205].
# 2. url https://stackoverflow.com/a/37121201/9475509
#    [20210407].
# 

# Import required libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xdata = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ydata = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
a = 1
b = 1

# Define wave parameters
A = 0.1
_lambda = 1
k = 2 * np.pi / _lambda
_phi = 0
v = 1
_omega = k * v
T = np.abs(2 * np.pi / _omega)

# Create array for x and showing two _lambda
dx = _lambda / 20
x = np.arange(0, 2 *_lambda + dx, dx)
print(x)
print(xdata)

def curve(a, b):
	y = a + b * x
	return y

#	Define wave
def wave(t):
	y = A * sin(k * x - _omega * t + _phi)
	return y

# Create array for time t from tbed to tend with step dt
tbeg = 0
tend = 10
dt = 1
t = np.arange(tbeg, tend, dt)

# Get range of x and y
#y = wave(0)
xmin = 0
xmax = 10
dx = 1
ymin = 0
ymax = 10
dy = 1
xmt = np.arange(xmin, xmax + dx, dx)
ymt = np.arange(ymin, ymax + dy, dy)

# Get figure for plotting and set it
fig = plt.figure(figsize=[3, 3])

# Configure axes
ax = fig.add_subplot()
ax.grid(which='both')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
ax.set_xticks(xmt, minor=True)
ax.set_yticks(ymt, minor=True)

# It must be set after configuring axis to give the effect
fig.tight_layout(rect=[-0.03, -0.03, 1.03, 1.03])

# Prepare curve
mark, = ax.plot([], [], 'sr', lw=1, ms=4)
line, = ax.plot([], [], '-b', lw=2)
time_template = 's = %i, a = %.3f, b = %.3f'
time_text = ax.text(0.03, 0.93, '', transform=ax.transAxes)

# Perform animation
def init():
	line.set_data([], [])
	mark.set_data([], [])
	time_text.set_text('')
	return line, mark, time_text

def animate(i):
	tt = i * dt / T
	a = 0.5 * i
	b = 0.5 * i
	y = curve(a, b)
	thisx = [x]
	thisy = [y]
	
	line.set_data([x], [y])
	mark.set_data([xdata], [ydata])
	time_text.set_text(time_template % (i, a, b))
	return line, time_text

ani = animation.FuncAnimation(
	fig, animate, np.arange(1, len(t)),
	interval=70, blit=True, init_func=init
)

# Write to to a GIF animation
writergif = animation.PillowWriter(fps=10)
ani.save('0268.gif', writer=writergif)
