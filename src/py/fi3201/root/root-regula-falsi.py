#	
#	root-regula-falsi.py
#	Finding root using regula falsi method
#	
#	Sparisoma Viridi | https://butiran.github.io/
#	
#	Execute: py root-regula-falsi.js
#	
#	20210210
#	0527 Typo node --> py, use newton-raphson.py as template.
#   0827 Continue at campus.
#   1001 Continue after archiving lab modules.
#   1028 Try compile again after install Python 3.9.1 64 bit.
#	

# Import necessary libraries
import numpy as np


# Define a test function
def test_function(x):
	y3 = 0.01 * x * x * x
	y2 = -0.2252 * x * x
	y1 = 0.4136 * x
	y0 = 1.808
	y = y3 + y2 + y1 + y0
	return y



# Define input
f = test_function
x1 = 3
x2 = 6
eps = 1E-10
n = 0
maxstep = 40

# Define default message and parameter
xroot = "not found"
SHOW_PROGRESS = True

# Do iteration
Nstep = 0
x = []
x.append(x1)
x.append(x2)
froot = np.abs(f(x[n]))

while froot > eps and n < maxstep - 1:
	x.append(x[0] - ((x[n+1] - x[0])/(f(x[n+1]) - f(x[0]))) * f(x[0]))
	
	froot = np.abs(f(x[n+2]))
	if froot < eps:
		xroot = x[n+2]
	
	if SHOW_PROGRESS:
		if n == 0:
			fn = f(x[n])
			print("n\tx\tf(x)")
			print(n, x[n], f(x[n]), sep="\t")
			print(n, x[n+1], f(x[n+1]), sep="\t")
		print(n+1, x[n+2], f(x[n+2]), sep="\t") 
	
	n += 1

Nstep = n+2

if SHOW_PROGRESS:
	print()

# Display result
print("f(x)  0.01x^3 - 0.2192x^2 + 0.3056x + 1.568");
print("x1    ", x1, sep="")
print("x2    ", x2, sep="")
print("ε     ", eps, sep="")
print("Nstep ", Nstep, sep="")
print("xroot ", xroot, sep="")
