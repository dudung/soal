#	
#	0010.py
#	

x1 = 1
y1 = 8
x2 = 5
y2 = 20

print("Known points")
print("x1 = ", x1, ", y1 = ", y1, sep="")
print("x2 = ", x2, ", y2 = ", y2, sep="")
print()

def f(x):
	m = (y2 - y1) / (x2 - x1)
	y = m * (x - x1) + y1
	return y

def g(y):
	m = (x2 - x1) / (y2 - y1)
	x = m * (y - y1) + x1
	return x

x = 3
y = f(x)
print("Interpolate y")
print("x = ", x, ", y = ", y, sep="")
print()

y = 11
x = g(y)
print("Interpolate x")
print("y = ", y, ", x = ", x, sep="")
