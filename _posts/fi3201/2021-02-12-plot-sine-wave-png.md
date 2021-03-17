---
layout: post
author: viridi
title: plot sine wave png
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "plot", "sine", "python"]
date: 2021-02-12 20:53:00 +07
permalink: /fi3201/plot-sine-wave-png
---
How to create a sine function representing a wave, plot it, and save it to a PNG file are discussed here.


## sine wave
It is a continuous wave that has the form of [[1](#ref1)]

\begin{equation}
\label{eqn:pswp-sine-wave}
y(x, t) = A \sin(kx - \omega t + \varphi),
\end{equation}

with $A$ is amplitude, $k$ is wavenumber, $\omega$ is angular frequency, and $\varphi$ is phase, where $y(x, t)$ is displacement of $A$ at position $x$ and time $t$. 

{:refdef: style="text-align: center;"}
![..](/assets/img/code/py/wave/sine-t-0.00.png)
![..](/assets/img/code/py/wave/sine-t-0.25.png) \
![..](/assets/img/code/py/wave/sine-t-0.50.png)
![..](/assets/img/code/py/wave/sine-t-0.75.png)
<br />
Figure <a name="fig:pswp-sine-wave">1</a> A sine wave at four different times showing that it is moving to the right.
{: refdef}

A sine wave with amplitude $A = 1.5$, period $T = 1$, and phase $\varphi = 0$ for time $t = 0, 0.25, 0.5, 0.75$ are given in Fig. <a href="#fig:pswp-sine-wave">1</a>.


## define a function
We can define a function named `swave` that representing Eqn. \eqref{eqn:pswp-sine-wave} in Python as follow

```python
#	Define a function representing a sine wave
def swave(x, t):
	A = 1.5
	_lambda = 1
	k = 2 * np.pi / _lambda
	T = 1
	_omega = 2 * np.pi / T
	_varphi = 0
	y = A * np.sin(k * x - _omega *t + _varphi)
	return y
```

where `np.pi` is for $\pi$. Since Python has built-in `lambda` function for an anonymous function [[2](#ref2)], we will define in the code `_lambda` for $\lambda$, `_omega` for $\omega$, and `_varphi` for $\varphi$. It is for consistency in writing variable name for Greek alphabet and related $\LaTeX$ symbol.


## code for plotting
To plot the function and save it in PNG format following code named `plot-sine-wave.py` can be used

```python
#	Import necessary packages
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredText


#	Define a function representing a sine wave
def swave(x, t):
	A = 1.5
	_lambda = 1
	k = 2 * np.pi / _lambda
	T = 1
	_omega = 2 * np.pi / T
	_varphi = 0
	y = A * np.sin(k * x - _omega *t + _varphi)
	return y


#	Use style
plt.style.use("seaborn-pastel")

#	Create figure with certain size in inch
fig = plt.figure(figsize=(2.5, 2.5))

#	Set x range
xmin = 0
xmax = 2
xrange = (xmin, xmax)

#	Set y range
ymin = -2
ymax = 2
yrange = (ymin, ymax)

# Set x and y axes
ax = plt.axes(xlim=xrange, ylim=yrange)

#	Set axes label
ax.set_xlabel("x")
ax.set_ylabel("y")

#	Set xtics
dx = 0.5
xtics = np.arange(xmin, xmax + dx, dx)
ax.set_xticks(xtics)

#	Set ytics
dy = 1
ytics = np.arange(ymin, ymax + dy, dy)
ax.set_yticks(ytics)

#	Get Line2D object representing plotted data
line, = ax.plot([], [], lw=3)

#	Show grid or with True
plt.grid()

#	Create data
t = 0
x = np.linspace(0, 4, 100)
y = swave(x, t)
line.set_data(x, y)

# Add time information
ts = "{:.2f}".format(t)
atext = AnchoredText("t = " + ts, loc=1)
ax.add_artist(atext)

#	Save plot as PNG image
plt.savefig("sine-t-" + ts + ".png")

# Show plot
plt.show()
```

where the full code with comments is available [here](https://github.com/butiran/butiran.github.io/blob/master/src/py/fi3201/vis-anim/plot-sine-wave.py). Actually, the four subfigures in Fig. <a href="#fig:pswp-sine-wave">1</a> are results of the code.


## exercises
1. Investigate the given code `plot-sine-wave.py` and change the sine wave to $y(x, t) = 0.2 \sin(2\pi x - \frac{1}{10}\pi t + \frac14\pi)$.
2. What is the meaning of `"{:.2f}".format(t)` in converting information of time $t$ represented with variable `t` to a string?
3. what does happen when you change the string `"seaborn-pastel"` and what other values that you can use?
4. There are the use of `plt.savefig()` and `plt.show()`. Explain the difference of them.
5. What is the purpose of `arange()` and `linspace()`? Explain in brief using examples.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Sine wave", Wikipedia, The Free Encyclopedia, 5 February 2021, 14:05 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1005006807> [20210212].
2. -, "Python Lambda", W3Schools, url https://www.w3schools.com/python/python_lambda.asp [20210212].


+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-02-12-plot-sine-wave-png.md)
