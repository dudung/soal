#	
#	plot-data-4.py
#	Plot data using Mathplotlib to PNG as simple as possible
#	
#	Sparisoma Viridi | https://github.com/dudung
#	
#	20210408
#	0411 Continue from plot-data-3.py program, try [1].
#	0419 Find that init(), animate() do not require return value.
#	0423 Add two series to the animated curve.
#
#	References
#	1. url https://stackoverflow.com/a/60580026 [20210408].
#	

# Import required libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set parameters for plotting
p = ['0184.gif']

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

#	Define wave
def wave(t):
	y = A * sin(k * x - _omega * t + _phi)
	return y

# Create array for time t from tbed to tend with step dt
tbeg = 0
tend = 4 * T
Nt = 10
dt = T / Nt
t = np.arange(tbeg, tend, dt)

# Get range of x and y
y = wave(0)
xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)
xmt = np.arange(xmin, xmax, 2.5 * dx)
ymt = np.arange(ymin, ymax, 0.05)

# Get figure for plotting and set it
fig = plt.figure(figsize=[5, 1.6])

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
fig.tight_layout(rect=[-0.03, -0.07, 1.01, 1.05])

# Prepare curve
line, = ax.plot([], [], 'or-', lw=2, ms=0)
time_template = '$t$ = %.1f s'
time_text = ax.text(0.04, 0.84, '', transform=ax.transAxes)

line2, = ax.plot([], [], 'sb-', lw=0, ms=10)
line3, = ax.plot([], [], 'sg-', lw=0, ms=10)

# Perform animation
def init():
	line.set_data([], [])
	time_text.set_text('')
	line2.set_data([], [])
	line3.set_data([], [])
	return line, time_text,

def animate(i):
	tt = i * dt / T
	y = wave(tt)
	thisx = [x]
	thisy = [y]
	
	line.set_data(thisx, thisy)
	time_text.set_text(time_template % tt)
	
	line2.set_data(x[20], y[20])
	line3.set_data(x[30], y[30])
	
	return line, time_text, line2

ani = animation.FuncAnimation(
	fig, animate, np.arange(1, len(t)),
	interval=70, blit=True, init_func=init
)

ani.save(p[0], fps=10)
