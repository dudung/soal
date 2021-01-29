---
layout: post
author: viridi
title: root bisection
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "root", "bisection"]
date: 2021-01-29 04:44:00 +07
permalink: /fi3201/root-bisection
---
One of the root finding algorithms is bisection method, which applies to any continuous functions that has values with opposite signs in the search range [[1](#ref1)]. It is an iterative method that divides previous internal into two subintervals and then evaluate which subintervals should be used, there the function still has value with opposite signs [[2](#ref2)]. There is a lot of use of similar principle in scientific works [[3](#ref3)].


## swap function
A swap function is a function that exchanges its two arguments value

\begin{equation}
\label{eqn:rb-swap-function}
{\rm swap}(\vec{r}) = (\vec{r} \cdot \hat{y})\hat{x} + (\vec{r} \cdot \hat{x})\hat{y},
\end{equation}

where $\vec{r} = x\hat{x} + y\hat{r}$ is used to store two values, i.e. $x$ and $y$, in single output. If $\vec{r} = 1.5\hat{x} - 7.2\hat{y}$ then ${\rm swap}(\vec{r})$ will produce $-7.2\hat{x} + 1.5\hat{y}$ or simply

\begin{equation}
\label{eqn:rb-swap-function-example}
(1.5, -7,2) \rightarrow (-7.2, 1.5).
\end{equation}

There is a built-in function in C++ standard template libray (STL) [[4](#ref4)] in the form of

```c++
swap(a, b)
```

with `a` and `b` are two mandatory parameters to be swapped. Manually there are some algorithms to perform the swap process without using a temporary variable but using arithmetic or bitwise operation or mixture of them [[5](#ref5)] or other ways [[6](#ref6)]. We will use this function in designing more readable algorithm for bisection method.


## algorithm
Let us assume that there is a function $f(x)$, which holds for $f(x_{\rm beg}) f(x_{\rm end}) < 0$, when $x \in [x_{\rm beg}, x_{\rm end}]$.

Algorithm <a name="alg:rb-bisection-method-algorithm">1</a> Bisection method. \
`I`: $f(x)$, $x_{\rm beg}$, $x_{\rm end}$, $\epsilon$. \
`O`: $x_{\rm root}$.
1. $n = 1$.
2. $x_n \leftarrow x_{\rm beg}$.
3. $x_{n+1} \leftarrow x_{\rm end}$.
4. $x_{n+2} \leftarrow \frac12 (x_{n+1} + x_n)$.
5. $f(x_{n+1}) f(x_{n+2}) < 0 \Rightarrow \color{blue}{\bf\scriptsize STEP} \ 7$.
6. ${\rm swap}(x_n, x_{n+1})$.
7. $\|f(x_{n+2})\| < \epsilon \Rightarrow \color{blue}{\bf\scriptsize STEP} \ 10$.
8. $n \leftarrow n + 1$.
9. $\color{blue}{\bf\scriptsize STEP} \ 4$.
10. $x_{\rm root} \leftarrow x_n$.


A function $f(x)$ as an example will be solved using Alg. <a href="#alg:rs-bisection-method-algorithm">1</a>.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Bisection method", Wikipedia, The Free Encyclopedia, 12 January 2021, 04:52 UTC, <https://en.wikipedia.org/w/index.php?oldid=999831078> [20210129].
2. <a name="ref2"></a>Eric W. Weisstein, "Bisection" from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/Bisection.html> [20210129].
3. <a name="ref3"></a>url <https://www.sciencedirect.com/topics/engineering/bisection-algorithm> [20210129].
4. <a name="ref4"></a>Prateek Sharma 7, "swap() in C++", GeeksforGeeks, 01 May 2019, url <https://www.geeksforgeeks.org/swap-in-cpp/> [20210129].
5. <a name="ref5"></a>GeeksforGeeks contributors (jit_t, mohit kumar 29, Chandan_Kumar, Code_Mech, ujjwalmittal, rathbhupendra, SHUBHAMSINGH10, Rajput-Ji, supershounak2001, yashbeersingh42, divyeshrabadiya07, bunnyram19, divyesh072019), "How to swap two numbers without using a temporary variable?", GeeksforGeeks, 11 Dec 2020, url <https://www.geeksforgeeks.org/swap-two-numbers-without-using-temporary-variable/> [20210129].
6. <a name="ref6"></a>Piyush Kochhar, "10 Ways To Swap Values In JavaScript", codeburst.io, 12 Aug 2020, url <https://codeburst.io/10-ways-to-swap-values-in-javascript-8a1d056352dd> [20210129].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-29-root-bisection.md)
