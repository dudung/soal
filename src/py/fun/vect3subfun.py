# 
# vect3subfun.py
# Substract two 3-d vectors using function in Python 3.7
#
# Sparisoma Viridi | https://github.com/dudung
# 
# 20210110
# 1952 Start creating this example.
# 1953 Test it and ok.
#

# Define function sub with two arguments
def sub(a, b):
	c = [0, 0, 0]
	c[0] = a[0] - b[0]
	c[1] = a[1] - b[1]
	c[2] = a[2] - b[2]
	return c

# Define two vector using array
r1 = [1, 2, 3]
r2 = [2, 2, 9]

# Substract two vectors
r3 = sub(r1, r2)

# Display result
print("r1 = ", r1, sep="");
print("r2 = ", r2, sep="");
print("r3 = r1 - r2 = ", r3, sep="");
