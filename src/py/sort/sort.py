# 
# median.py
# Sort an array of integer
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3 sort.py
# 
# 20201101
# 1534 Start this example from median.py file.
# 1539 Finish this example.
# 
# References
# 1. -, "Python List sort()", Programiz, Parewa Labs, url
#    https://www.programiz.com/python-programming/methods/list
#    /sort [20201101].
# 2. eyquem, pauloue, "Answer to 'Is there a standardized
#    method to swap two variables in Python?'", StackOverflow,
#    12 Feb 2013, 22 Jan 2018, url https://stackoverflow.com/
#    a/14836456 [20201101].
# 3. Abhijit, Banana, "Answer to 'Skip first entry in for loop
#    in python?'", StackOverflow, 9 Apr 2012, 28 Jul 2014, url
#    https://stackoverflow.com/a/10079247 [20201101].

# Create an array, sort, find its min, max, med (all manually)
x = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
print("init =", x)
N = len(x)
print("N =", N)
for i in range(0, N - 1):
	for j in range(i + 1, N):
		if x[i] > x[j]:
			x[i], x[j] = x[j], x[i]
print("sort =", x)

# Add blank line
print()

# Create an array, sort, find its min, max, med (manually)
y = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
print("init =", y)
y.sort()
print("sort =", y)

# Add blank line
print()

# Create an array, sort, find its min, max, med (manually)
z = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
a = sorted(z)
print("init =", z)
print("sort =", a)
