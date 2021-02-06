#	
#	plot-trav-wave-x-package
#	Animate spatial profile of a travelling wave 
#	
#	Sparisoma Viridi | https://butiran.github.io
#	
#	20210206
#	1151 Use package and module for plot-trav-wave-x.py file.
#	1205 Add relative directory for package [1].
#	
#	References
#	1. Shinbero, "Answer to'Importing modules from parent folder'",
#	   StackOverflow, 29 Jan 2020 at 0406, url https://stackoverflow 
#	   .com/a/28712742 [20210206].
# 


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import sys

# Set parent directory before import in-house modules or packages
sys.path.insert(0,'..')
from butiran.wave import wave_1d as w1d


# Define travelling wave parameters
A = 0.2
T = 1
_lambda = 1
_phi = 0

# Create travelling wave object
wave = w1d.TravellingWave(A, T, _lambda, _phi)

# Set observation time
t = 0

# Create array of position x
x = np.arange(0, 2, 0.04)

# Calculate displacement y using wave object
y = wave.displacement(x, t)


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
