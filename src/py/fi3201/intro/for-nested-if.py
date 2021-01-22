# 
# for-nested-if.py
# Use for and if to display something in Python 3.7
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3.7 for-nested-if.py
# 
# 20210122
# 1203 Create this example form for only.
# 1457 Choose on of the output
# 1637 Rename from for-if.py previously.
# 

for i in range(4, 10):
	for j in range(4, 10):
		k = i * j
		if i == j:
			print(k, end=" ")
		else:
			print("00", end=" ")
	print()
