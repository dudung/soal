#	
#	0014.py
#	

def avg(lst):
	return sum(lst) / len(lst)

def SS(a, b):
	aavg = avg(a)
	bavg = avg(b)
	ss = 0;
	N = min(len(a), len(b))
	for i in range(0, N):
		ss += (a[i] - aavg) * (b[i] - bavg)
	return ss

x = [1, 2, 3, 4, 5]
y = [2, 5, 8, 11, 14]
print("Data")
print("x = ", x)
print("y = ", y)
print()

b = SS(x, y) / SS(x, x)
a = avg(y) - b * avg(x)
r2 = SS(x, y) * SS(y, x) / ( SS(x, x) * SS(y, y) )

print("Model")
print("y = a + bx")
print()

print("Least squares fitting")
print("a = ", a, sep="")
print("b = ", b, sep="")
print("r^2 = ", r2, sep="")
