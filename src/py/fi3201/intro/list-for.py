# 
# list-for.py
# Use list with for in Python 3.7
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3.7 list-for.py
# 
# 20210122
# 0955 Create this example, test it, and it works.
# 

# Define a list
x = [1, 7, 8, 5, 4]

# Get length of the list
N = len(x)

for i in range(0, N, 1):
	print(x[i])
	
print()

for i in range(0, N):
	print(x[i])

print()

for i in range(N):
	print(x[i])

print()

for i in x:
	print(i)
