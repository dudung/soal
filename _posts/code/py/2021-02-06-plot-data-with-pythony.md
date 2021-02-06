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
date: 2021-02-06 06:45:00 +07
permalink: /code/py/plot-data-with-python
---
Inspired by [[1](#ref1)] how to plot a function will be described here in brief. 


## function to be plotted
Suppose that we have data of a sine function for plotting provided by following function

\begin{equation}
\label{eqn:sp-wave-function}
y(x, t) = A \sin(\omega t - kx + \varphi_0),
\end{equation}

which is actually expression of a travelling wave [[2](#ref2)]. We are interested to show the spatial profile at certain time. Then we must have the values of amplitude $A$, angular frequency $\omega$, time $t$, wavenumber $k$, and phase constant $\varphi_0$ [[3](#ref3)].

Let $A = 0.2 \ {\rm m}$, $T = 1 \ {\rm s}$, $\lambda = 1 \ {\rm m}$, $\varphi_0 = \pi \ {\rm rad}$. Then using the relation

\begin{equation}
\label{eqn:sp-angular-frequency}
\omega = \frac{2\pi}{T}
\end{equation}

and

\begin{equation}
\label{eqn:sp-wavenumber}
k = \frac{2\pi}{\lambda}
\end{equation}

we can have $\omega = 2\pi \ {\rm rad/s}$ and $k = 2\pi \ {\rm rad/m}$.

## code
Following code `plot-trav-wave-x.py` are used to plot Eqn. \eqref{eqn:sp-wave-function}.

```python
```

where the full code with comment can be obtained [here](https://github.com/butiran/butiran.github.io/blob/master/src/py/anim/plot-trav-wave-x.py).


## references
1. <a name="ref1"></a>John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team, "The double pendulum problem", Matplotlib Version 2.1.2, Feb 2018, url <https://matplotlib.org/gallery/animation/double_pendulum_animated_sgskip.html> [20210205].
2. <a name="ref2"></a>Carl R. Nave, "Plane Wave Expressions", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/Waves/wavsol.html#c5> [20210206].
3. <a name="ref3"></a>S. Hussain Ather, "How to Calculate Phase Constant", Sciencing, 28 Dec 2019, url <https://sciencing.com/calculate-phase-constant-8685432.html> [20210206].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/code/py/2021-02-06-plot-data-with-python.md)
