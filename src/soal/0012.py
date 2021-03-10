#	
#	0012.py
#	

a = 1
b = -4
c = 4

print("Equation\n", a, "x^2 + ", b, "x + ", c, sep="")
print();

D = b * b - 4 * a * c

print("Discriminant\nD = ", D)
print()

print("Comment")
if D > 0:
	print("There are two roots")
else:
	if D == 0:
		print("There is one double root")
	else:
		print("There is not any real root")
