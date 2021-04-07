#	
#	plot-data-2.py
#	Plot data using Mathplotlib to PNG as simple as possible
#	
#	Sparisoma Viridi | https://github.com/dudung
#	
#	20210407
#	1945 Continue from plot-data-1.py program.
#	1829 Continue from plot-data-0.py program.
#	2014 Make wave() and can plot curve with grid.
#	2019 Finish generate data and clean lines.
#	

# Import required libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt

# Set parameters for plotting
p = [0, '0182.png']

# Define wave parameters
A = 0.1
T = 1
_omega = 2 * np.pi / T
_lambda = 1
k = 2 * np.pi / _lambda
_phi = 0

# Create array for x and showing two _lambda
dx = _lambda / 20
x = np.arange(0, 2 *_lambda + dx, dx)

#	Define wave
def wave(t):
	y = A * sin(k * x - _omega * t + _phi)
	return y

# Create array for y using function wave
y = wave(p[0])

# Get range of x and y
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

# Set style for plotting and also the data
line, = ax.plot([], [], 'sr-', lw=2, ms=0)
line.set_data(x, y)

# Save plotting result to PNG file
plt.savefig(p[1])
