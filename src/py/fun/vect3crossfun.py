# 
# vect3crossfun.py
# Cross product of two 3-d vectors using function in Python 3.7
#
# Sparisoma Viridi | https://github.com/dudung
# 
# 20210110
# 2009 Start creating this example.
# 2011 Test it and ok.
#

# Define cross function with two arguments
def cross(a, b):
	c = [0, 0, 0]
	c[0] = a[1] * b[2] - a[2] * b[1]
	c[1] = a[2] * b[0] - a[0] * b[2]
	c[2] = a[0] * b[1] - a[1] * b[0]
	return c

# Define two vector using array
r1 = [1, 1, 0]
r2 = [-1, 1, 0]

# Calculate cross product of two vectors
r3 = cross(r1, r2)

# Display result
print("r1 = ", r1, sep="");
print("r2 = ", r2, sep="");
print("r3 = r1 \xd7 r2 = ", r3, sep="");
