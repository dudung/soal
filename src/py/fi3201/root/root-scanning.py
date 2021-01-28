#	
#	root-scanning.py
#	Finding root using scanning method
#	
#	Sparisoma Viridi | https://butiran.github.io/
#	
#	Execute: node root-scanning.js
#	
#	20210128
#	1235 Start this program.
#	1758 Continue after test_function test.
#	1806 Add reference 1, just now about it.
#	1828 Test it and ok.
#	
#	References
#	1. Glenn Maynard, "Answer to 'Why are there no ++ and --​
#	   operators in Python?'", StackOverflow, 6 Sep 2010 23:57,
#	   url https://stackoverflow.com/a/3654936 [20210128].
#

# Import necessary libraries
import numpy as np

# Define a test function
def test_function(x):
	a = 0.05
	x1 = -1
	x2 = 3.45
	x3 = 8
	y = a*(x-x1)*(x-x2)*(x-x3)
	return y


# Define input
f = test_function
xbeg = 2
xend = 5
dx = 1

# Define default message
xroot = "not found";

# Do iteration
Nstep = 0;
x = xbeg;

while x <= xend:
	# Increase Nstep;
	Nstep += 1
	
	# Calculate S0 and S
	if x == xbeg:
		S0 = np.sign(f(x))
	else:
		S = np.sign(f(x))
	
	# Check S0.S for root
	if x > xbeg:
		if S0 * S < 0:
			xroot = x - 0.5 * dx;
			break;
	
	x += dx;

# Display result
print("f(x)   0.05(x+1)(x-3.45)(x-8)");
print("Δx    ", dx, sep="")
print("xbeg  ", xbeg, sep="")
print("xend  ", xend, sep="")
print("Nstep ", Nstep, sep="")
print("xroot ", xroot, sep="")
