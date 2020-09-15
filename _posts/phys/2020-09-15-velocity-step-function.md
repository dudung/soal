---
layout: post
author: viridi
title: velocity step function
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["topics"]
date: 2020-09-15 22:08:00 +07
permalink: /physics/velocity-step-function
---
There is a type of linear motion (LM) composed of some [uniform linear motions](uniform-linear-motion) (ULMs), which is different than the nonuniform linear motion (NULM). Velocity function $v(t)$ of this type of LM is simply a step function [[1](#ref1)]. Or it can said that each ULM is a boxcar function [[2](#ref2)].


## Boxcar function
A boxcar function has only non-zero value $A$ over a single interval, which can be described with

\begin{equation}
\label{eqn:vsf-boxcar-function}
{\rm boxcar}(x) =
\left\\{
\begin{array}{lc}
A, & a \le x \le b, \newline
0, & x < a \cup b < x.
\end{array}
\right.
\end{equation}

The invertal has lower boundary $a$ and upper boundary $b$.


## References
1. <a name="ref1"></a>Wikipedia contributors, "Step function", Wikipedia, The Free Encyclopedia, 21 Apr 2020, 04:27 UTC, <https://en.wikipedia.org/w/index.php?oldid=952221804> [20200915].
2. <a name="ref2"></a>Wikipedia contributors, "Boxcar function", Wikipedia, The Free Encyclopedia, 1 Aug 2020, 03:12 UTC, <https://en.wikipedia.org/w/index.php?oldid=852898903> [20200915].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-09-15-velocity-step-function.md)
