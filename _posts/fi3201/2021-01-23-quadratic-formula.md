---
layout: post
author: viridi
title: quadratic formula
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "quadratic", "formula"]
date: 2021-01-23 05:02:00 +07
permalink: /fi3201/quadratic-formula
---
One way to get the solution of a quadratic equation is using the quadratic formula [[1](#ref1)]. Here how the formula can be written in some programming languages are shown.

## equation and solution
For an unknown $x$, a general quadratic equation can be written in form of

\begin{equation}
\label{eqn:qf-quadratic-equation}
ax^2 + bx + c = 0,
\end{equation}

where $a$, $b$, and $c$ represent constants. Solution of Eqn. \eqref{eqn:qf-quadratic-equation} can be obtained using quadratic formula

\begin{equation}
\label{eqn:qf-quadratic-formula}
x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}

with $a \ne 0$. Note that a quadratic equation has two solutions, that is given by $x_1$ and $x_2$.

## algoritm
From Eqns. \eqref{eqn:qf-quadratic-equation} and \eqref{eqn:qf-quadratic-formula}, there are four input parameters $a$, $b$, $c$, and $x$, and there are two output values $x_1$ and $x_2$.

## references
1. <a name="ref1"></a>Wikipedia contributors, "Vector (mathematics and physics)", Wikipedia, The Free Encyclopedia, 22 August 2020, 14:24 UTC, <https://en.wikipedia.org/w/index.php?oldid=974354203> [20210123].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-23-quadratic-formula.md)

