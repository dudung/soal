---
layout: post
author: viridi
title: function intro
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: python
date: 2021-01-10 21:23:00 +07
tags: ["function"]
permalink: /code/py/function-intro
---
Brief introduction to function in Python with an example is presented here.


## function
How a varying quantity depends on another quantity can be represented in a function [[1](#ref1)], e.g. $y$ depends on $x$

\begin{equation}
\label{fintro-function}
y = f(x)
\end{equation}

and it may also be said, in this case, that $x$ is independent variable, while $y$ is dependent variable [[2](#ref2)].


## polynomial
A univariate polynomial [[3](#ref3)] can be expressed, e.g. with order of two, in the form of

\begin{equation}
\label{fintro-polynomial-2}
P(x) = c_0 + c_1 \ x + c_2 x^2,
\end{equation}

where $c_0$, $c_1$, $c_2$ are coefficients. We will use list, a generic containers in Python [[4](#ref4)], instead of array to store the coefficients

```python
c0 = 6
c1 = -5
c2 = 1
coeff = [c0, c1, c2]
```

where `coeff` is variable with type of Python list. We can also using number directyl in the list, between `[` and `]`, the square brackets. Previous example still uses `c0`, `c1`, and `c2` only to give better relation to Eqn. \eqref{fintro-polynomial-2}.


## syntax
In Python we can define a function [[5](#re5), [6](#re6)] as follow

```python
def function_name(argument):
	# Relate the argument (as input) with processed_value (as output)
	processed_value = argument
	return processed_value
```

which is an illustration of a user-defined function.


## example
Suppose that we have following quadratic equation

\begin{equation}
\label{fintro-example-quadratic}
f(x) = x^2 - 5x + 6,
\end{equation}

that has values of $x$ and $y$

$x$ | 0 | 1 | 2 | 3 | 4 | 5
$y$ | 6 | 2 | 0 | 0 | 2 | 6

Eqn. \eqref{fintro-example-quadratic} can be implemented in Python (there are some other ways) as follow

```python
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
```

that produces some output from previous table

```cmd
$ python3.7 fun/funx.py
x1 = 0, fun(x1) = 6
x2 = 2, fun(x2) = 0
x3 = 4, fun(x3) = 2
```

when executed. Notice that $f(x)$ in Eqn. \eqref{fintro-example-quadratic} is represented as `fun(x)` in the code.


## exercises
1. 


## note
+ Function name should represent purpose of the function and argument(s) should be defined to give a clear description and usage of the function.
+ Codes are tested with Python 3.7 using Cygwin (x86) in Windows 10 Home (x64).
+ It would be better if a function also includes doctring (documentation string), which has not yet been used in here.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Function (mathematics)", Wikipedia, The Free Encyclopedia, 9 Jan 2021, 17:09 UTC, <https://en.wikipedia.org/w/index.php?oldid=999330249> [20210110].
2. <a name="ref2"></a>Wikipedia-Autoren, "Abhängige und unabhängige Variable", Wikipedia, Die freie Enzyklopädie, 1 Dez 2020, 17:28 UTC, <https://de.wikipedia.org/w/index.php?oldid=206134794> [20210110].
3. <a name="ref3"></a>Eric W. Weisstein,  "Univariate Polynomial", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/UnivariatePolynomial.html> [20210111].
4. <a name="ref4"></a>Shreya Khare, "Array in Python \| Set 1 (Introduction and Functions)", GeeksforGeeks, 07 Oct 2020, url <https://www.w3schools.com/python/python_functions.asp> [20210111].
5. <a name="ref5"></a>-, "Python Functions", Programiz, url <https://www.programiz.com/python-programming/function> [20210111].
6. <a name="ref6"></a>-, "Python Functions", W3Schools, url <https://www.w3schools.com/python/python_functions.asp> [20210110].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/code/py/2021-01-10-function-intro.md)
