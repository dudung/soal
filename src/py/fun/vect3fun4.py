# 
# vect3fun4.py
# Collect functions for manipulating two 3-d vectors
#
# Sparisoma Viridi | https://github.com/dudung
# 
# 20210110
# 2015 Start creating this example.
# 2016 Copy functions from vect3addfun.py, vect3subfun.py,
#      vect3dotfun.py, and vect3crossfun.py files.
#

# Define function add with two arguments
def add(a, b):
	c = [0, 0, 0]
	c[0] = a[0] + b[0]
	c[1] = a[1] + b[1]
	c[2] = a[2] + b[2]
	return c

# Define function sub with two arguments
def sub(a, b):
	c = [0, 0, 0]
	c[0] = a[0] - b[0]
	c[1] = a[1] - b[1]
	c[2] = a[2] - b[2]
	return c

# Define dot function with two arguments
def dot(a, b):
	p = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
	return p

# Define cross function with two arguments
def cross(a, b):
	c = [0, 0, 0]
	c[0] = a[1] * b[2] - a[2] * b[1]
	c[1] = a[2] * b[0] - a[0] * b[2]
	c[2] = a[0] * b[1] - a[1] * b[0]
	return c
