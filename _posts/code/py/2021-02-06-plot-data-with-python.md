---
layout: post
author: viridi
title: plot data with python
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: code
tags: ["python", "plot", "numpy", "matplotlib"]
date: 2021-02-06 09:00:00 +07
permalink: /code/py/plot-data-with-python
---
Inspired by [[1](#ref1)] how to plot a function will be described here in brief. 


## function to be plotted
Suppose that we have data of a sine function for plotting provided by following function

\begin{equation}
\label{eqn:pdw-wave-function}
y(x, t) = A \sin(\omega t - kx + \varphi_0),
\end{equation}

which is actually expression of a travelling wave [[2](#ref2)]. We are interested to show the spatial profile at certain time. Then we must have the values of amplitude $A$, angular frequency $\omega$, time $t$, wavenumber $k$, and phase constant $\varphi_0$ [[3](#ref3)].

Let $A = 0.2 \ {\rm m}$, $T = 1 \ {\rm s}$, $\lambda = 1 \ {\rm m}$, $\varphi_0 = \pi \ {\rm rad}$. Then using the relation

\begin{equation}
\label{eqn:pdw-angular-frequency}
\omega = \frac{2\pi}{T}
\end{equation}

and

\begin{equation}
\label{eqn:pdw-wavenumber}
k = \frac{2\pi}{\lambda}
\end{equation}

we can have $\omega = 2\pi \ {\rm rad/s}$ and $k = 2\pi \ {\rm rad/m}$.

## code
Following code `plot-trav-wave-x.py` are used to plot Eqn. \eqref{eqn:pdw-wave-function}.

```python
# Import required libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt


# Define a function for travelling wave
def travwave(x, t):
	A = 0.2
	T = 1
	_l = 1
	_w = 2 * np.pi / T
	k = 2 * np.pi / _l
	_varphi0 = np.pi
	y = A * sin(_w * t - k * x + _varphi0)
	return y


# Set observation time
t = 0.50

# Create x and y data
x = np.arange(0, 2, 0.04)
y = travwave(x, t)

# Get figure for plotting
fig = plt.figure()

# Configure axes
ax = fig.add_subplot(
	111,
	autoscale_on=True,
	xlim=(0, 2),
	ylim=(-0.2, 0.2)
)
ax.set_aspect('equal')
ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')

# Set style for plotting
line, = ax.plot([], [], 'sr-', lw=1, ms=4)
time_template = 't = %.2f s'
time_text = ax.text(0.8, 0.8, '', transform=ax.transAxes)

# Set data and time information
line.set_data(x, y)
time_text.set_text(time_template % t)

# Show plotting result
plt.show()
```

where full code with comments can be obtained [here](https://github.com/butiran/butiran.github.io/blob/master/src/py/anim/plot-trav-wave-x.py).


## result
Using observation time $t = 0, 0.5, 1 \ {\rm s}$ we can have following figure.

{:refdef: style="text-align: center;"}
![..](/assets/img/code/py/wave/trav-wave-t0.00.png)
![..](/assets/img/code/py/wave/trav-wave-t0.25.png)
![..](/assets/img/code/py/wave/trav-wave-t0.50.png)
<br />
Figure <a name="fig:pdw-travelling-wave">1</a> Travelling wave from Eqn. \eqref{eqn:pdw-wave-function} at time $t$: $0 \ \rm s$ (top), $0.25 \ \rm s$ (middle), and $0.5 \ \rm s$ (bottom).
{: refdef}

Fig. <a href="#fig:pdw-travelling-wave">1</a> show the result of `plot-trav-wave-x.py` by setting `t = 0.0`, `t = 0.25`. and `t = 0.5` after the line `# Set observation time`.


## exercises
1. Explain the use of Python function `arange` from `NumPy` in creating an array.
2. In setting axis using `plot` there is format for mark, line, and color, where we use `sr-` in the code `plot-trav-wave-x.py`. Find the format and what options we can use for them.
3. How can changle an axis label?
4. If we want to plot other function, e.g $f(x) = 0.1(x - 5)^2 + 1$, which part of the code `plot-trav-wave-x.py` should be modified? Show that part after you modify it.
5. Find reference of `add_subplot` function and explain the meaning of first argument `111` from given code.


## references
1. <a name="ref1"></a>John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team, "The double pendulum problem", Matplotlib Version 2.1.2, Feb 2018, url <https://matplotlib.org/gallery/animation/double_pendulum_animated_sgskip.html> [20210205].
2. <a name="ref2"></a>Carl R. Nave, "Plane Wave Expressions", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/Waves/wavsol.html#c5> [20210206].
3. <a name="ref3"></a>S. Hussain Ather, "How to Calculate Phase Constant", Sciencing, 28 Dec 2019, url <https://sciencing.com/calculate-phase-constant-8685432.html> [20210206].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/code/py/2021-02-06-plot-data-with-python.md)
