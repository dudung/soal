#	
#	plot-data-1.py
#	Plot data using Mathplotlib to PNG as simple as possible
#	
#	Sparisoma Viridi | https://github.com/dudung
#	
#	20210407
#	1829 Continue from plot-data-0.py program.
#	1842 Learn more about grid ticks [1].
#	1905 Generate data a(0, 1, 1).
#	1907 Generate data b(pi, 1, 1).
#	1908 Generate data c(0, 2, 1), d(0, 1, 2).
#	1907 Generate data e(pi/2, 1, 1).
#	1911 Rearange lines.
#	
#	References
#	1. url https://stackoverflow.com/a/24953575 [20210407].
#

# Import required libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt

# Set parameters for plotting
p = [0, 1, 1, '0181.png']

#	Create array for parametric variable t
T = 1
tbeg = 0
tend = T
dt = 0.01 * T
t = np.arange(tbeg, tend+1, dt)

# Create array for x and y using parametric functions
A = 1
omega = 2 * np.pi / T
phi0 = p[0]
omega1 = p[1] * omega
omega2 = p[2] * omega
x = A * sin(omega1 * t)
y = A * sin(omega2 * t + phi0) 

# Get range of x and y
xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)

# Get figure for plotting and set it
fig = plt.figure(figsize=[2.1, 2])

# Configure axes
ax = fig.add_subplot()
ax.grid(which='both')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
ax.set_xticks([-1, 0, 1])
ax.set_xticks([-1, -0.5, 0, 0.5, 1], minor=True)
ax.set_yticks([-1, 0, 1])
ax.set_yticks([-1, -0.5, 0, 0.5, 1], minor=True)

# It must be set after configuring axis to give the effect
fig.tight_layout(rect=[-0.05, -0.05, 1.05, 1.05])

# Set style for plotting and also the data
line, = ax.plot([], [], 'sr-', lw=2, ms=0)
line.set_data(x, y)

# Save plotting result to PNG file
plt.savefig(p[3])
