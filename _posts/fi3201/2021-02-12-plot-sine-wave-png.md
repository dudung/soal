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

..


## references
1. <a name="ref1"></a>Wikipedia contributors, "Sine wave", Wikipedia, The Free Encyclopedia, 5 February 2021, 14:05 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1005006807> [20210212].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-02-12-plot-sine-wave-png.md)
