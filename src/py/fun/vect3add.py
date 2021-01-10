# 
# vect3add.py
# Add two 3-d vectors in Python 3.7
#
# Sparisoma Viridi | https://github.com/dudung
# 
# 20210110
# 1940 Start creating this example.
# 1946 Test it and ok.
#

# Define two vector using array
r1 = [1, 2, 3]
r2 = [2, 2, 9]

# Add two vectors
r3 = [0, 0, 0]
r3[0] = r1[0] + r2[0]
r3[1] = r1[1] + r2[1]
r3[2] = r1[2] + r2[2]

# Display result
print("r1 = ", r1, sep="");
print("r2 = ", r2, sep="");
print("r3 = r1 + r2 = ", r3, sep="");
