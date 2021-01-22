# 
# for-if.py
# Use for and if to display something in Python 3.7
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3.7 for-nested-if.py
# 
# 20210122
# 1639 Create this example only from nested-for-if.py file.
# 

for i in range(4, 10):
	for j in range(4, 10):
		k = i * j
		if i == j:
			print(k, end=" ")
		else:
			print("00", end=" ")
	print()
