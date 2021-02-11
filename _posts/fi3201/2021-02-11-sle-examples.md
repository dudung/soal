---
layout: post
author: viridi
title: system of linear equations examples
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "linear", "equation", "system"]
date: 2021-02-11 14:24:00 +07
permalink: /fi3201/sle-examples
---
Even today we can solve system of linear equations (SLE) online, eg. for four equations [[1](#ref1)], it is still interesting to study the SLE especially when you try to find the solution for inconsistent system [[2](#ref2)]. Solution of an SLE must satisfy all equations in the system, which are considered collectively, not individually [[3](#ref3)]. We propose some systems in physics and how we can get the SLE from them.


## observing non-uniform linear motion
In a non-uniform linear motion position of particle

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/sle/non-uniform-linear-motion.png)
<br />
Figure <a name="fig:slee">1</a> An object drawn as red circle is moving from left to right with initial position and velocity at $t = 0$ are unknown.
{: refdef}


## speed up and slow down in a linear motion

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/sle/kinematics-1d-nlm-lm-nlm.png)
<br />
Figure <a name="fig:slee">2</a> .
{: refdef}


## battery resistor dc circuit with three loops

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/sle/dc-er-circuit-3-loops.png)
<br />
Figure <a name="fig:slee">3</a> .
{: refdef}



## references
1. <a name="ref1"></a>-, "Online Systems of Equations Solver: Solve equations and systems of equations with Wolfram\|Alpha", Wolfram Alpha, 2021, url <https://www.wolframalpha.com/calculators/system-equation-calculator> [20210211].
2. <a name="ref2"></a>Elizabeth Stapel, "Systems of Linear Equations" Purple Math, 2020, url <https://www.purplemath.com/modules/systlin1.htm> [20210211].
3. <a name="ref3"></a>Wikipedia contributors, "System of linear equations", Wikipedia, The Free Encyclopedia, 17 January 2021, 17:30 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1000977892> [20210211].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-02-11-sle-examples.md)


{% comment %}
Not like the [Newton-Raphson method](/fi3201/root-newton-raphson) that requires a function and its derivative, secant method approximates the derivative with finite-difference method, even it is said that this method actually predates the Newton-Raphson method [[1](#ref1)]. With the approximation it will save large amount of CPU time for machine calculations or considerable amount of effort to do hand calculations if the function has complicated expression, and it gives also a method that converges as fast as the Newton-Raphson method [[2](#ref2)]. This method has still been used in engineering [[3](#ref3)] and improved in mathematics [[4](#ref4)]. This method can be used in Wolfram Languange with `SecantMethodList` [[5](#ref5)] and there is example of implementation of this method in Python [[6](#ref6)].


## formula
Secant method has the formula of

\begin{equation}
\label{eqn:rs-secant-method}
x_{n+2} = x_{n+1} - f(x_{n+1}) \left[ \frac{x_{n+1} - x_n}{f(x_{n+1}) - f(x_n)} \right],
\end{equation}

where $x_{n+1} = x_n + \Delta x$.


## finite difference
We can use finite difference as an approximation of derivative [[7](#ref7)]

\begin{equation}
\label{rs-derivative-finite-difference}
f'(x) \approx \frac{f(x+\Delta x) - f(x)}{\Delta x},
\end{equation}

which will substitute the derivative term $f'(x)$ in Newton-Raphson method

\begin{equation}
\label{eqn:rs-newton-raphson-method}
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\end{equation}

and procude Eqn. \eqref{eqn:rs-secant-method}.


## algorithm
Eqn. \eqref{eqn:rs-secant-method} can be described in following algorithm. We assume that at least one root does exist for $f(x)$.

Algorithm <a name="alg:rs-secant-method-algorithm">1</a> Secant method. \
`I`: $f(x)$, $x_1$, $x_2$, $\epsilon$. \
`O`: $x_{\rm root}$.
1. $n = 1$.
2. $\displaystyle x_{n+2} \leftarrow x_{n+1} - \frac{f(x_{n+1})(x_{n+1} - x_n)}{f(x_{n+1}) - f(x_n)}$.
3. $\|f(x_{n+2})\| < \epsilon \Rightarrow \color{blue}{\bf\scriptsize STEP} \ 6$.
4. $n = n + 1$.
5. $\Rightarrow \color{blue}{\bf\scriptsize STEP} \ 2$.
6. $x_{\rm root} = x_{n+2}$.

Notice that different than [Newton-Raphson method](/fi3201/root-newton-raphson#algorithm), $f'(x)$ is not required but we need also $x_2$ instead of only $x_1$ as the initial guess. And as always there might be many another variations of algorithm than shown in Alg. <a href="#alg:rs-secant-method-algorithm">1</a>.


## flowchart
Fig. <a href="#fig:rs-secant-method-flowchart">1</a> shows the flowchart of secant method, where in general the steps are similar to the [Newton-Raphson method](/fi3201/root-newton-raphson#flowchart)

{:refdef: style="text-align: center;"}
![..](/assets/img/math/root/root-secant-flowchart.png)
<br />
Figure <a name="fig:rs-secant-method-flowchart">1</a> Steps in secant method are described in a flow chart. 
{: refdef}

In this method the result is indicated with $n+2$, while in Newton-Raphson method with $n+1$.


## implementation
In implementing algorithm in Alg. <a href="#alg:rnr-newton-raphson-method-algorithm">1</a> or flowchart in Fig. <a href="#fig:rnr-newton-raphson-method-flowchart">1</a> a program can have following output

```batch
f(x)  0.01x^3 - 0.2192x^2 + 0.3056x + 1.568
x1    2
x2    3
ε     1e-10
Nstep 8
xroot 3.919999999999999
```

where the example is given in Python.

### python
Following code `root-secant.py` has been tested using Python 3.7.7 through Cygwin version 2.873 on Windows 10 Home.

```python
# Import necessary libraries
import numpy as np


# Define a test function
def test_function(x):
	y3 = 0.01 * x * x * x
	y2 = -0.2192 * x * x
	y1 = 0.3056 * x
	y0 = 1.568
	y = y3 + y2 + y1 + y0
	return y


# Define input
f = test_function
xinit1 = 2
xinit2 = 3
eps = 1E-10
n = 0
maxstep = 40

# Define default message and parameter
xroot = "not found"

# Do iteration
Nstep = 0
x = []
x.append(xinit1)
x.append(xinit2)
froot = np.abs(f(x[n+1]))

while froot > eps and n < maxstep - 1:
	x.append(x[n+1] - f(x[n+1]) * (x[n+1] - x[n])  / (f(x[n+1]) - f(x[n])))
	
	froot = np.abs(f(x[n+2]))
	if froot < eps:
		xroot = x[n+2]
	
	n += 1

Nstep = n+2

# Display result
print("f(x)  0.01x^3 - 0.2192x^2 + 0.3056x + 1.568");
print("x1    ", xinit1, sep="")
print("x2    ", xinit2, sep="")
print("ε     ", eps, sep="")
print("Nstep ", Nstep, sep="")
print("xroot ", xroot, sep="")
```

Full source code with comments can be accessed [here](https://github.com/butiran/butiran.github.io/blob/master/src/py/fi3201/root/root-secant.py)


## exercises
1. Compare the results given by `root-secant.py` and previous `root-newton-raphson.py`. Do they produce similar results with the same steps? Explain the difference.
2. Change $x_1$ and $x_2$ and see how they influence the results, i.e. $x_{\rm root}$ and also `Nstep`.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Secant method", Wikipedia, The Free Encyclopedia, 4 January 2021, 18:18 UTC, <https://en.wikipedia.org/w/index.php?oldid=998290429> [20210103].
2. <a name="ref2"></a>Sanyasiraju V. S. S. Yedida, "Secant Method", Department of Mathematics, Indian Institute of Technology Madras, Chennai, url <https://mat.iitm.ac.in/home/sryedida/public_html/caimna/transcendental/iteration%20methods/secant/secant.html> [20210103].
3. <a name="ref3"></a>-, "Secant Method", url <https://www.sciencedirect.com/topics/engineering/secant-method> [20210203].
4. <a name="ref4"></a>-, "Secant Method", url <https://www.sciencedirect.com/topics/mathematics/secant-method> [20210203]. 
5. <a name="ref5"></a>Eric W. Weisstein, "Secant Method" from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/SecantMethod.html> [20210203].
6. <a name="ref7"></a>Patrick Walls, "Secant Method", Mathematical Python, Department of Mathematics, the University of British Columbia, Wed 4 Dec 2019 17:20:04 PST, url <https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/secant/> [20210203].
7. <a name="ref7"></a>Wikipedia contributors, "Finite difference", Wikipedia, The Free Encyclopedia, 22 January 2021, 00:28 UTC, <https://en.wikipedia.org/w/index.php?oldid=1001922880> [20210103]

{% endcomment %}