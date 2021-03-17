# 
# funx.py
# Example of function in Python 3.7
#
# Sparisoma Viridi | https://github.com/dudung
# 
# 20210110
# 1920 Create this example, test it, and it works.
# 1925 Add another output for clearer meaning.
# 1938 Change f1 to fA to fun for function of x.
#

# Define function fun with argument x
def fun(x):
	c = [6, -5, 1]
	y = c[2] * x**2 + c[1] * x + c[0];
	return y;

# Define some x and use the function
x1 = 0; y1 = fun(x1)
x2 = 2; y2 = fun(x2)
x3 = 4; y3 = fun(x3)

# Display the results
print("x1 = ", x1, ", fun(x1) = ", y1, sep="")
print("x2 = ", x2, ", fun(x2) = ", y2, sep="")
print("x3 = ", x3, ", fun(x3) = ", y3, sep="")
