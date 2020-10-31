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

# Create an array and find its min, med, max
x = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
print("init =", x)
x.sort()
print("sort =", x)
N = len(x)
print("N =", N)
im = int((N + 1) / 2 - 1)
xm = x[im]
print("min =", x[0])
print("med =", xm)
print("max =", x[N - 1])

# Create similar array and sort it manually
y = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
print("init =", y)

