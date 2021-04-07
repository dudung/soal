#	
#	plot-data-0.py
#	Plot data using Matplotlib to PNG as simple as possible
#	
#	Sparisoma Viridi | https://github.com/dudung
#	
#	20210407
#	1554 Start this one from previous ones.
#	1624 Set figure size [1], but there is clipping problem.
#	1627 Solution is given by [2] using tight_layout().
#	1649 Finish this example.
#	1652 Clean some lines.
#	
#	References
#	1. url https://stackabuse.com/change-figure-size-in-matplotlib/
#	   [20210407].
#	2. url https://stackoverflow.com/a/22809087 [20210407].
#	

# Import required libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt

#	Create array for x data, calculate y data
xmin = 0
xmax = 10
dx = 1
x = np.arange(xmin, xmax+1, dx)
y = - x * (x-10)

# Get range of x and y
xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)

# Get figure for plotting
fig = plt.figure(figsize=[4, 3])
fig.tight_layout()

# Configure axes
ax = fig.add_subplot()
ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])

# Set style for plotting and also the data
line, = ax.plot([], [], 'sr-', lw=1, ms=4)
line.set_data(x, y)

# Save plotting result to PNG file
plt.savefig("0180.png")
