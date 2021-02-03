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
date: 2021-02-03 21:49:00 +07
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


## references
1. <a name="ref1"></a>Wikipedia contributors, "Root-finding algorithms", Wikipedia, The Free Encyclopedia, 15 January 2021, 23:25 UTC, <https://en.wikipedia.org/w/index.php?oldid=1000624440> [20210203].
2. <a name="ref2"></a>Wikipedia contributors, "Regula falsi", Wikipedia, The Free Encyclopedia, 29 January 2021, 23:01 UTC, <https://en.wikipedia.org/w/index.php?oldid=1003635041> [20210203].
3. <a name="ref3"></a>Eric W. Weisstein, "Method of False Position", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/RegulaFalsi.html> [20210203].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-02-03-root-regula-falsi.md)
