# 
# triangle-number-lines-up-space.py
# Display number in lines with different count / number
# and arrange with some spaces
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3.7 triangle-number-lines-up-space.py
# 
# 20210122
# 1716 Create this example, test it, and it works.
# 

N = 5
for i in range(2, N + 2):
	for j in range(1, N + 2 - i):
		print(" ", end=" ")
	for j in range(1, i):
		print("0", end=" ")
	print()
