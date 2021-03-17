#	
#	root-newton-raphson.py
#	Finding root using Newton-Raphson method
#	
#	Sparisoma Viridi | https://butiran.github.io/
#	
#	Execute: py root-newton-raphson.js
#	
#	20210131
#	1850 Start this program from root-bisection.py.
#	1954 Continue make test_function and its derivative.
#	2006 Test it and ok, also for SHOW_PROGRESS.
#	2009 Correct maxstep to maxstep-1 in while.
#	20210210
#	0527 Typo node --> py.
#	

# Import necessary libraries
import numpy as np


# Define a test function
def test_function(x):
	y3 = 0.01 * x * x * x
	y2 = -0.2192 * x * x
	y1 = 0.3056 * x
	y0 = 1.568
	y = y3 + y2 + y1 + y0
	return y


# Define derivative of the test function
def derivative_test_function(x):
	y2 = 3 * 0.01 * x * x
	y1 = 2 * -0.2192 * x
	y0 = 0.3056
	y = y2 + y1 + y0
	return y


# Define input
f = test_function
dfdx = derivative_test_function
xinit = 2
eps = 1E-10
n = 0
maxstep = 40

# Define default message and parameter
xroot = "not found"
SHOW_PROGRESS = False

# Do iteration
Nstep = 0
x = []
x.append(xinit)
froot = np.abs(f(x[n]))

while froot > eps and n < maxstep - 1:
	x.append(x[n] - f(x[n]) / dfdx(x[n]))
	
	froot = np.abs(f(x[n+1]))
	if froot < eps:
		xroot = x[n+1]
	
	if SHOW_PROGRESS:
		if n == 0:
			fn = f(x[n])
			print("n\tx\tf(x)")
			print(n, x[n], f(x[n]), sep="\t")
		print(n+1, x[n+1], f(x[n+1]), sep="\t") 
	
	n += 1

Nstep = n+1

if SHOW_PROGRESS:
	print()

# Display result
print("f(x)  0.01x^3 - 0.2192x^2 + 0.3056x + 1.568");
print("xinit ", xinit, sep="")
print("ε     ", eps, sep="")
print("Nstep ", Nstep, sep="")
print("xroot ", xroot, sep="")
