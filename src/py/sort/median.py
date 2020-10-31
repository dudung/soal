# 
# median.py
# Find median of an array of integer
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3 median.py
# 
# 20201101
# 0329 Start this example.
# 0433 Use sort to find min, med, max.
# 0530 Able to sort it manually.
# 0538 Can find med with statistics module.
# 0543 Finish comments.
# 
# References
# 1. Vivi Andasari, "Some Basic Operations in Python", Zaman
#    lab, Biomedical Engineering, Boston University, Boston,
#    USA, 15 Sep 2020, url http://people.bu.edu/andasari
#    /courses/basicpython/basicpython.html [20201101].
# 2. -, "Python print() function", w3resource.com, DataSoft,
#    Khosbagan, India, 28 Feb 2020, url https://www.w3resource
#    .com/python/python-print-statement.php [20201101].
# 3. -, "Python List sort()", Programiz, Parewa Labs, url
#    https://www.programiz.com/python-programming/methods/list
#    /sort [20201101].
# 4. Upendra Bartwal, "How to print without newline in
#    Python?", GeeksforGeeks, Noida, India, 2 Feb 2018, url
#    https://www.geeksforgeeks.org/print-without-newline
#    -python/ [20201101].
# 5. eyquem, pauloue, "Answer to 'Is there a standardized
#    method to swap two variables in Python?'", StackOverflow,
#    12 Feb 2013, 22 Jan 2018, url https://stackoverflow.com/
#    a/14836456 [20201101].
# 6. Abhijit, Banana, "Answer to 'Skip first entry in for loop
#    in python?'", StackOverflow, 9 Apr 2012, 28 Jul 2014, url
#    https://stackoverflow.com/a/10079247 [20201101].
# 7. James Gallagher, "Python Median() – A Python Statistics
#    Tutorial", Career Karma, 23 Apr 2020, url https:/
#    /careerkarma.com/blog/python-median [20201101].

# Create an array and find its min, max, med using statistics
z = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
print("init =", z)
print("min =", min(z))
print("max =", max(z))
import statistics
print("mid =", statistics.median(z))

# Add blank line
print()

# Create an array, sort, find its min, max, med (manually)
x = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
print("init =", x)
x.sort()
print("sort =", x)
N = len(x)
print("N =", N)
xmin = min(x)
xmax = max(x)
imed = int((N + 1) / 2 - 1)
xmed = x[imed]
print("min =", xmin)
print("max =", xmax)
print("med =", xmed)

# Add blank line
print()

# Create an array, sort, find its min, max, med (all manually)
y = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
#y = [1, 8, 4, 5, 2, 1, 2]
print("init =", y)
N = len(y)
print("N =", N)
for i in range(0, N - 1):
	for j in range(i + 1, N):
		if y[i] > y[j]:
			y[i], y[j] = y[j], y[i]
print("sort =", y)
imin = 0
imax = N - 1
imed = int((N + 1) / 2 - 1)
print("min =", y[imin])
print("max =", y[imax])
print("med =", y[imed])
