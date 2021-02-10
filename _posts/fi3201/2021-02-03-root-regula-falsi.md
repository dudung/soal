---
layout: post
author: viridi
title: root regula falsi
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "root", "false position"]
date: 2021-02-09 19:01:00 +07
permalink: /fi3201/root-regula-falsi
---
Regula falsi method is part of bracketing method in root-finding algorithms, which can determine successively smaller intervals containing a root [[1](#ref1)]. It is a very old method for solving an equation with one unknown, which is in simple terms the method using trial and error technique [[2](#ref2)]. It is also known as method of false position [[3](#ref3)].


## formulation
Assume that there is

\begin{equation}
\label{eqn:rrf-function}
f(x) = \sum_n c_n x^n
\end{equation}

as a function, whose root is to be found when

\begin{equation}
\label{eqn:rrf-function-root}
f(x_{\rm root}) = 0.
\end{equation}

Let $x_1$ and $x_2 > x_1$ which produce

\begin{equation}
\label{eqn:rrf-function-x1-f1}
f(x_1) = f_1
\end{equation}

and

\begin{equation}
\label{eqn:rrf-function-x2-f2}
f(x_2) = f_2.
\end{equation}

Using Eqns. \eqref{eqn:rrf-function-x1-f1} and \eqref{eqn:rrf-function-x2-f2} we can have equation of a line

\begin{equation}
\label{eqn:rrf-function-equation-of-a-line-1}
y = \left( \frac{f_2 - f_1}{x_2 - x_1} \right) (x - x_1) + f_1
\end{equation}

or

\begin{equation}
\label{eqn:rrf-function-equation-of-a-line-2}
y = \left( \frac{f_2 - f_1}{x_2 - x_1} \right) (x - x_2) + f_2.
\end{equation}

Eqns. \eqref{eqn:rrf-function-equation-of-a-line-1} and \eqref{eqn:rrf-function-equation-of-a-line-2} produce $x$ intercept

\begin{equation}
\label{eqn:rrf-function-equation-of-a-line-1-x-intercept}
x = x_1 - \left( \frac{x_2 - x_1}{f_2 - f_1} \right) f_1 
\end{equation}

or

\begin{equation}
\label{eqn:rrf-function-equation-of-a-line-2-x-intercept}
x = x_2 - \left( \frac{x_2 - x_1}{f_2 - f_1} \right) f_2 
\end{equation}

by setting $y = 0$. Both Eqns. \eqref{eqn:rrf-function-equation-of-a-line-1-x-intercept} will produce

\begin{equation}
\label{eqn:rrf-regula-falsi}
x = \frac{x_1 f_2 - x_2 f_1}{f_2 - f_1}
\end{equation}

as in [[1](#ref1)].


## iterative formula
Keep the first point $x_1$ fixed, then set label $2$ as $n-1$ and $n$ for the new $x$ we can have Eqn. \eqref{eqn:rrf-function-equation-of-a-line-1-x-intercept}

\begin{equation}
\label{eqn:rrf-regula-falsi-iterative-formula}
x_n = x_1 - \left( \frac{x_{n-1} - x_1}{f_{n-1} - f_1} \right) f_1 
\end{equation}

as a iterative formula [[2](#ref1)]. Notice that it relates $x_1$, $x_{n-1}$, and $x_n$, where the first point remains the same.


## algorithm
We can describe Eqn. \eqref{eqn:rrf-regula-falsi-iterative-formula} in following algorithm with assumption that at least one root does exist for $f(x)$.

Algorithm <a name="alg:rrf-regula-falsi-algorithm">1</a> Regula falsi method. \
`I`: $f(x)$, $x_1$, $x_2$, $\epsilon$. \
`O`: $x_{\rm root}$.
1. $n = 1$.
2. $\displaystyle x_{n+2} \leftarrow x_1 - \left[ \frac{x_{n+1} - x_1}{f(x_{n+1}) - f(x_1)} \right] f(x_1)$.
3. $\|f(x_{n+2})\| < \epsilon \Rightarrow \color{blue}{\bf\scriptsize STEP} \ 6$.
4. $n = n + 1$.
5. $\Rightarrow \color{blue}{\bf\scriptsize STEP} \ 2$.
6. $x_{\rm root} = x_{n+2}$.

Different than [Newton-Raphson method](/fi3201/root-newton-raphson#algorithm) or [secant method](/fi3201/root-secant#algorithm), in this method $x_1$ is always there and used to predict $x_n$ with $x_{n_1}$. And remember as always that another variations of algorithm than shown in Alg. <a href="#alg:rrf-secant-method-algorithm">1</a> might exist.


## flowchart
Fig. <a href="#fig:rrf-regula-falsi-method-flowchart">1</a> shows other alternative to Alg. <a href="#alg:rrf-regula-falsi-algorithm">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/root/root-regula-falsi-flowchart.png)
<br />
Figure <a name="fig:rrf-regula-falsi-method-flowchart">1</a> Steps in regula falsi method are described in a flow chart. 
{: refdef}

The result is indicated with $n+2$ in this method as in secant method.


## test function
We would like to examine following function

\begin{equation}
\label{eqn:rrf-test-function}
f(x) = 0.01 x^3 - 0.2252 x^2 + 0.4136 x + 1.808,
\end{equation}

whose roots are $-2$, $4.52$, and $20$. The progress in obtaining prediction of root is given in Fig. <a href="#fig:rrf-regula-falsi-results">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/root/root-regula-falsi-2.png) \
![..](/assets/img/math/root/root-regula-falsi-3.png) \
![..](/assets/img/math/root/root-regula-falsi-4.png)
<br />
Figure <a name="fig:rrf-regula-falsi-results">2</a> Regula falsi method: $x_1$ and $x_2$ are initial guess (top), $x3$ is predicted using $x_1$ and $x_2$ (middle), and $x_4$ is predicted using $x_1$ and $x_3$ (bottom). 
{: refdef}

Using a spreadsheet following output is obtained

```
x	f(x)
3	1.292
6	-1.6576
4.314076485	0.203951017
4.560395574	-0.040916642
4.512495995	0.007568713
4.521408615	-0.001421887
4.519736097	0.00026635
4.52004946	-4.99201E-05
4.519990731	9.35524E-06
4.520001737	-1.75324E-06
4.519999674	3.2857E-07
4.520000061	-6.15763E-08
```

which leads to $x_{\rm root} = 4.52$.


## implementation
Following result can obtained
```
n       x       f(x)
0       3       1.2920000000000005
0       6       -1.6575999999999984
1       4.314076484947113       0.2039510165570917
2       4.560395574452329       -0.040916642034676265
3       4.512495994584455       0.007568713039659336
4       4.521408614724482       -0.0014218869629232245
5       4.519736096966463       0.0002663500357777959
6       4.520049460146103       -4.992014680826884e-05
7       4.51999073091976        9.355237911456982e-06
8       4.520001737094587       -1.7532428879807327e-06
9       4.519999674456336       3.2856990794805085e-07
10      4.520000061009185       -6.157632737036067e-08
11      4.519999988566447       1.1539840194529916e-08
12      4.520000002142729       -2.1626476165437225e-09
13      4.519999999598438       4.0529468670058577e-10
14      4.520000000075255       -7.595479800670546e-11

f(x)  0.01x^3 - 0.2192x^2 + 0.3056x + 1.568
x1    3
x2    6
ε     1e-10
Nstep 16
xroot 4.520000000075255
```

using following code

```python
# Import necessary libraries
import numpy as np


# Define a test function
def test_function(x):
	y3 = 0.01 * x * x * x
	y2 = -0.2252 * x * x
	y1 = 0.4136 * x
	y0 = 1.808
	y = y3 + y2 + y1 + y0
	return y



# Define input
f = test_function
x1 = 3
x2 = 6
eps = 1E-10
n = 0
maxstep = 40

# Define default message and parameter
xroot = "not found"

# Do iteration
Nstep = 0
x = []
x.append(x1)
x.append(x2)
froot = np.abs(f(x[n]))

while froot > eps and n < maxstep - 1:
	x.append(x[0] - ((x[n+1] - x[0])/(f(x[n+1]) - f(x[0]))) * f(x[0]))
	
	froot = np.abs(f(x[n+2]))
	if froot < eps:
		xroot = x[n+2]
	
	n += 1

Nstep = n+2

# Display result
print("f(x)  0.01x^3 - 0.2192x^2 + 0.3056x + 1.568");
print("x1    ", x1, sep="")
print("x2    ", x2, sep="")
print("ε     ", eps, sep="")
print("Nstep ", Nstep, sep="")
print("xroot ", xroot, sep="")
```

named `root-regula-falsi.py` whose source is available [here](https://github.com/butiran/butiran.github.io/blob/master/src/py/fi3201/root/root-regula-falsi.py).


## exercises
1. Draw the values $x_2$, $x_3$, $x_4$, .., $x_n$ during the process of finding the root in a $y-x$ chart.
2. Compare this method with another ones, e.g. Newton-Raphson method, secant method, and show the steps required for same accuracy.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Root-finding algorithms", Wikipedia, The Free Encyclopedia, 15 January 2021, 23:25 UTC, <https://en.wikipedia.org/w/index.php?oldid=1000624440> [20210203].
2. <a name="ref2"></a>Wikipedia contributors, "Regula falsi", Wikipedia, The Free Encyclopedia, 29 January 2021, 23:01 UTC, <https://en.wikipedia.org/w/index.php?oldid=1003635041> [20210203].
3. <a name="ref3"></a>Eric W. Weisstein, "Method of False Position", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/RegulaFalsi.html> [20210203].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-02-03-root-regula-falsi.md)
