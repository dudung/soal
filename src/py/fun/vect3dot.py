# 
# vect3dot.py
# Dot product of two 3-d vectors in Python 3.7
#
# Sparisoma Viridi | https://github.com/dudung
# 
# 20210110
# 1953 Start creating this example.
# 1956 Test it and ok.
# 2000 Add \xb7 for middle dot.
#

# Define two vector using array
r1 = [1, 2, 3]
r2 = [2, 2, 9]

# Calculate dot product of two vectors
p = r1[0] * r2[0] + r1[1] * r2[1] + r1[2] * r2[2]

# Display result
print("r1 = ", r1, sep="");
print("r2 = ", r2, sep="");
print("p = r1 \xb7 r2 = ", p, sep="");
