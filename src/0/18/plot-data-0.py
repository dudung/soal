#	
#	plot-data-0.py
#	Plot data using Mathplotlib to PNG as simple as possible
#	
#	Sparisoma Viridi | https://github.com/dudung
#	
#	20210407
#	1554 Start this one from previous ones.
#	1624 Set figure size [1], but there is clipping problem.
#	1627 Solution is given by [2] using tight_layout().
#	1649 Finish this example.
#	1652 Clean some lines.
#	1731 Find problem and try to use [3] for tight_layout().
#	1738 Get the solution of using tight_layout() properly.
#	1747 Finish generating files 0170a - 0170e.
#	
#	References
#	1. url https://stackabuse.com/change-figure-size-in-matplotlib/
#	   [20210407].
#	2. url https://stackoverflow.com/a/22809087 [20210407].
#	3. url https://stackoverflow.com/a/45161551/9475509 [20210407].
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
y = (x-10) * (x-2.5) * (x-7.5)

# Get range of x and y
xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)

# Get figure for plotting and set it
fig = plt.figure(figsize=[2.5, 2])

# Configure axes
ax = fig.add_subplot()
ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])

# It must be set after configuring axis to give the effect
fig.tight_layout(rect=[-0.05, -0.05, 1.05, 1.05])

# Set style for plotting and also the data
line, = ax.plot([], [], 'sr-', lw=1, ms=4)
line.set_data(x, y)

# Save plotting result to PNG file
plt.savefig('0180e.png')
