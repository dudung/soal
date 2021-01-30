---
layout: post
author: viridi
title: root newton-raphson
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "root", "newton", "newton-raphson"]
date: 2021-01-30 20:33:00 +07
permalink: /fi3201/root-newton-raphson
---
With a function, its derivative, and a initial guess of a root, root of a real-valued function can be approximated better successively using Newton-Raphson method [[1](#ref1)].


## formula
With initial guess of a root $x_n$, value of the function $f(x_n)$, and its derivative $f'(x_n)$, following iterative formula

\begin{equation}
\label{eqn:rnr-newton-raphson-method}
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\end{equation}

where $x_{n+1}$ is a better approximation of the root.


## derivation
The formula in Eqn. \eqref{eqn:rnr-newton-raphson-method} can be derived using equation of a line [[2](#ref2)].


## references
1. <a name="ref1"></a>Wikipedia contributors, "Newton's method", Wikipedia, The Free Encyclopedia, 9 January 2021, 08:37 UTC, <https://en.wikipedia.org/w/index.php?oldid=999264602> [20210130].
2. <a name="ref2"></a>Wikipedia contributors, "Linear equation", Wikipedia, The Free Encyclopedia, 11 November 2020, 23:58 UTC, <https://en.wikipedia.org/w/index.php?oldid=988244807> [20210130].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-30-root-newton-raphson.md)
