---
layout: post
author: viridi
title: root scanning
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "root", "scanning"]
date: 2021-01-27 06:34:00 +07
permalink: /fi3201/root-scanning
---
We can use scanning method in finding a root, even it is not listed in the list of root-finding algorithms [[1](#ref1)]. This method is not efficient, not accurate, and very step dependent.


## sign function
A signum function or sign function can be deined as [[2](#ref2)]

\begin{equation}
\label{eqn:rs-sign-function}
{\rm sign}(x) = \left\\{
\begin{array}{lr}
-1, & x < 0, \newline
0, & x = 0, \newline
1, & x > 0,
\end{array}
\right.
\end{equation}

or for $x \ne 0$ it can be approximated with

\begin{equation}
\label{eqn:rs-sign-function-non-zero}
{\rm sign}(x) = \frac{x}{\|x\|} = \frac{\|x\|}{x}.
\end{equation}

We will use the Eqn. \eqref{eqn:rs-sign-function-non-zero} instead of \eqref{eqn:rs-sign-function} only for simplicity.


## algorithm
Assume that a function $f(x)$ already exists and we would like to find $x$ as a root of the function. 

Algorithm <a name="alg:rs-scanning-method-algorithm">1</a> Scanning method. \
`I`: $f(x)$, $x_{\rm beg}$, $x_{\rm end}$, $\Delta x$ \
`O`: $x_{\rm root}$
1. $x \leftarrow x_{\rm beg}$.
2. $\displaystyle S_0 \leftarrow \frac{f(x)}{\|f(x)\|}$.
3. $x \leftarrow x + \Delta x$.
4. $\displaystyle S \leftarrow \frac{f(x)}{\|f(x)\|}$.
5. $S_0 S < 0 \Rightarrow \rm step\ 8$
6. $x > x_{\rm end} \Rightarrow \rm step\ 10$
7. $\Rightarrow step\ 3$
8. $x_{\rm r} \leftarrow x - \frac12 \Delta x$.
9. $\Rightarrow step\ 11$
10. $x_{\rm r} \notin  [x_{\rm beg}, x_{\rm end}]$.
11. $x_{\rm root} \leftarrow x_r$

## references
1. <a name="ref1"></a>Wikipedia contributors, "Root-finding algorithms", Wikipedia, The Free Encyclopedia, 15 January 2021, 23:25 UTC, <https://en.wikipedia.org/w/index.php?oldid=1000624440> [20210126].
2. <a name="ref1"></a>Wikipedia contributors, "Root-finding algorithms", Wikipedia, The Free Encyclopedia, 15 January 2021, 23:25 UTC, <https://en.wikipedia.org/w/index.php?oldid=1000624440> [20210126].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-26-root-scanning.md)
