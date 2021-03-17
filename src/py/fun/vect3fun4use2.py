# 
# vect3fun4use2.py
# Example of using vect3fun4.py file (import as)
#
# Sparisoma Viridi | https://github.com/dudung
# 
# 20210110
# 2032 Modify vect3fun4use.py file.
# 2034 Test it and ok with [1].
# 
# References
# 1. url https://stackoverflow.com/a/45205175 [20210110].

# Define two vector using array
r1 = [1, 1, 0]
r2 = [-1, 1, 0]

# Import the whole file as a variable
import vect3fun4 as Vect3

# Add two vectors
r3 = Vect3.add(r1, r2)
print(r1, " + ", r2, " = ", r3, sep="")

# Substract two vectors
r4 = Vect3.sub(r1, r2)
print(r1, " - ", r2, " = ", r4, sep="")

# Calculate dot product of two vectors
p = Vect3.dot(r1, r2)
print(r1, " \xb7 ", r2, " = ", p, sep="")

# Calculate cross product of two vectors
r5 = Vect3.cross(r1, r2)
print(r1, " \xd7 ", r2, " = ", r5, sep="")
