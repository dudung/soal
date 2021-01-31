#	
#	root-newton-raphson.py
#	Finding root using Newton-Raphson method
#	
#	Sparisoma Viridi | https://butiran.github.io/
#	
#	Execute: node root-newton-raphson.js
#	
#	20210131
#	1850 Start this program from root-bisection.py.
#	

# Import necessary libraries
import numpy as np


# Define a test function
def test_function(x):
	y3 = 0.025 * x * x * x;
	y2 = -0.2585 * x * x;
	y1 = 0.243 * x;
	y0 = 0.5265;
	y = y3 + y2 + y1 + y0;
	return y


# Define input
f = test_function
xbeg = 1
xend = 8
eps = 1E-6
Nstep = 0
maxstep = 40
n = 0

# Define default message and parameter
xroot = "not found"
SHOW_PROGRESS = True

# Do iteration
Nstep = 0
x = []
x.append(xbeg)
x.append(xend)
froot = np.abs(f(x[n+1]))

while n <= maxstep-3 and froot > eps:
	x.append(0.5*(x[n] + x[n+1]))
	
	fn1 = f(x[n+1])
	fn2 = f(x[n+2])
	c = fn1 * fn2
	if c > 0:
		x[n], x[n+1] = x[n+1], x[n]
	
	if SHOW_PROGRESS:
		if n == 0:
			fn = f(x[n])
			print("n\tx\tf(x)")
			print(n, x[n], fn, sep="\t")
			print(n+1, x[n+1], fn1, sep="\t")
		print(n+2, x[n+2], fn2, sep="\t") 
	
	froot = np.abs(fn2)
	if froot < eps:
		xroot = x[n+2]
	
	n += 1

Nstep = n+2

if SHOW_PROGRESS:
	print()

# Display result
print("f(x)   0.025x^3 - 0.2585x^2 + 0.243x + 0.5265");
print("xbeg  ", xbeg, sep="")
print("xend  ", xend, sep="")
print("ε     ", eps, sep="")
print("Nstep ", Nstep, sep="")
print("xroot ", xroot, sep="")
