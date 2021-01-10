# 
# vect3fun4use.py
# Example of using vect3fun4.py file (from import)
#
# Sparisoma Viridi | https://github.com/dudung
# 
# 20210110
# 2020 Start creating this example.
# 2027 Test it and ok with [1].
# 
# References
# 1. url https://stackoverflow.com/a/20309470 [20210110].

# Define two vector using array
r1 = [1, 1, 0]
r2 = [-1, 1, 0]

# Add two vectors
from vect3fun4 import add
r3 = add(r1, r2)
print(r1, " + ", r2, " = ", r3, sep="")

# Substract two vectors
from vect3fun4 import sub
r4 = sub(r1, r2)
print(r1, " - ", r2, " = ", r4, sep="")

# Calculate dot product of two vectors
from vect3fun4 import dot
p = dot(r1, r2)
print(r1, " \xb7 ", r2, " = ", p, sep="")

# Calculate cross product of two vectors
from vect3fun4 import cross
r5 = cross(r1, r2)
print(r1, " \xd7 ", r2, " = ", r5, sep="")
