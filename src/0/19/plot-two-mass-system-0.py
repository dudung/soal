#	
#	plot-two-mass-system-0.py
#	Plot data using Mathplotlib to GIF for 2-mass-sys
#	
#	Sparisoma Viridi | https://github.com/dudung
#	
#	20210411
#	1820 Start by modifying plot-data-5.py file.
#	1832 Try to use butiran library [1].
#	1856 Implement prespective inspired by [2], more simple.
#	2008 Can produce GIF, animation not work with plot().
#	2121 Find [3] for removing warning.
#	2156 Can not install ffmpeg, user GIF Scrubber [4].
#	
#	References
#	1. url https://pypi.org/project/butiran/ [20210411].
#	2. url https://stackoverflow.com/a/4268351 [20210411].
#	3. url https://stackoverflow.com/a/62196206 [20210411].
#	4. url https://chrome.google.com/webstore/detail/gif-
#	   scrubber/gbdacbnhlfdlllckelpdkgeklfjfgcmp  [20210411].
#	

# Import required libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse
from butiran.vect3 import Vect3

# Set parameters for plotting
p = ['0195.gif', '0195.mp4']

# Create array for time t from tbed to tend with step dt
tbeg = 0
tend = 2
T = tend - tbeg
Nt = 20
dt = T / Nt
t = np.arange(tbeg, tend + dt, dt)

# Define 1st collony
R1 = 0.5
r1 = Vect3(0, 0, -R1)
m1 = 1

# Define 2nd collony
R2 = 0.5
r2 = Vect3(0, 0, R2)
m2 = 1

#	Caculate r dan R vectors
r = Vect3.sub(r2, r1)
Rnum = Vect3.add(Vect3.mul(m1, r1), Vect3.mul(m2, r2))
Rden = m1 + m2
R = Vect3.div(Rnum, Rden)

# Define size due to perspective in x direction
def sizep(d, x):
	c = 0.2
	d = d * (1 + c * x)
	return d

# Set range of x and y
rx = [-2, 2, 0.25]
ry = [-2, 2, 0.25]
xmt = np.arange(rx[0], rx[1] + rx[2], rx[2])
ymt = np.arange(ry[0], ry[1] + ry[2], ry[2])

# Get figure for plotting and set it
fig = plt.figure(figsize=[4.4, 4])

# Configure axes
ax = fig.add_subplot()
ax.set_xlabel('$y$')
ax.set_ylabel('$z$')
ax.set_xlim([rx[0], rx[1]])
ax.set_ylim([ry[0], ry[1]])
ax.grid(which='both')
ax.set_xticks(xmt, minor=True)
ax.set_yticks(ymt, minor=True)

# It must be set after configuring axis to give the effect
fig.tight_layout(rect=[-0.02, -0.02, 1.02, 1.02])

# Prepare curve
line, = ax.plot([], [], 'or-', lw=2, ms=0)
time_template = '$t$ = %.1f s'
time_text = ax.text(0.01, 0.95, '', transform=ax.transAxes)

g1 = Ellipse(
	(r1.y, r1.z), 2 * R1, 2 * R1,
	edgecolor='g', fc='#cfc', lw=2
)
ax.add_patch(g1)
g2 = Ellipse(
	(r2.y, r2.z), 2 * R2, 2 * R2,
	edgecolor='g', fc='#cfc', lw=2
)
ax.add_patch(g2)

# Set initial position
X0 = R.x
Y0 = R.y
Z0 = R.z
theta0 = np.pi / 4 * 0
phi0 = np.pi / 4 * 2
r0 = r

#	Set kinematic velocities
Xdot = 0
Ydot = 0
Zdot = 0
thetadot = 2 * np.pi / T * 1
phidot = 2 * np.pi / T * 0

# Perform animation
def init():
	line.set_data([], [])
	time_text.set_text('')
	return line, time_text

def animate(i):
	tt = (i - 1) * dt
	
	print(i)
	
	X = X0 + Xdot * tt
	Y = Y0 + Ydot * tt
	Z = Z0 + Zdot * tt
	theta = theta0 + thetadot * tt
	phi = phi0 + phidot * tt

	l = r0.len()
	x = l * sin(theta) * cos(phi)
	y = l * sin(theta) * sin(phi)
	z = l * cos(theta)

	R = Vect3(X, Y, Z)
	r = Vect3(x, y, z)

	beta = m2 / (m1 + m2)
	
	r1 = Vect3.sub(R, Vect3.mul(beta, r))
	r2 = Vect3.add(R, Vect3.mul(1 - beta, r))
	
	g1.center = r1.y, r1.z
	g2.center = r2.y, r2.z
	
	s1 = sizep(2 * R1, r1.x)
	g1.width = s1
	g1.height = s1
	
	s2 = sizep(2 * R2, r2.x)
	g2.width = s2
	g2.height = s2
	
	if r2.x > r1.x:
		g1.zorder = 2
		g2.zorder = 3
	else:
		g1.zorder = 3
		g2.zorder = 2
	
	time_text.set_text(time_template % tt)
	
	return line, time_text

ani = animation.FuncAnimation(
	fig, animate, np.arange(1, len(t)),
	interval=70, blit=True, init_func=init
)

# Write to to a GIF animation
writergif = animation.PillowWriter(fps=10)
ani.save(p[0], writer=writergif)
