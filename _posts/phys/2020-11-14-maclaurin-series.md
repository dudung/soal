---
layout: post
author: viridi
title: maclaurin series
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["statics"]
date: 2020-11-14 18:23:00 +07
permalink: /physics/maclaurin-series
---
A function $f(x)$ can be approached using an infinite sum of terms that are expressed in terms of derivatives of the function at single point $x_0$, where this infinite sum of terms is known as Taylor series [[1](#ref1)]. If we choose that $x_0 = 0$, then the series known as Maclaurin series [[2](#ref2)].


## Notation
Suppose that there is a function $f(x)$, where its $n$-th derivative is

\begin{equation}
\label{eqn:maclaurin-series-nth-derivative}
f_n(x) = \frac{d^n f(x)}{dx^n} 
\end{equation}

and

\begin{equation}
\label{eqn:maclaurin-series-nth-derivative-x0}
f_n(x_0) = \left[ \frac{d^n f(x)}{dx^n} \right]_{x = x_0}
\end{equation}

is value of a term of derivatives of the function, when $x = x_0$. Let's take $f(x) = x^3$ as an example that gives $f_2(x) = 6x$ and $f_2(x_0) = 6 x_0$, or when $x_0 = 2$ then $ f_2(2) = 12$.


## Infinite sum of terms
An normal function $f(x)$ can expressed in Maclaurin series as

\begin{equation}
\label{eqn:maclaurin-series}
f(x) = \sum_{n = 0}^N f_n(0) \left( \frac{x^n}{n!} \right),
\end{equation}

with

\begin{equation}
\label{eqn:maclaurin-series-n!}
n! = n \cdot (n-1) \cdot (n-1) \cdot \ \dots \ \cdot 2 \cdot 1
\end{equation}

is the factorial of a positive integer $n$ [[3](#ref3)]. Remember that $0! = 1$. Using again previous example, we can have that

\begin{equation}
\label{eqn:maclaurin-series-example-1a}
\begin{array}{rclcrcl}
f_0(x) & = & x^3,  & \ \ \ \ f_0(0) & = & 0, \newline
f_1(x) & = & 3x^2, & \ \ \ \ f_1(0) & = & 0, \newline
f_2(x) & = & 6x,   & \ \ \ \ f_2(0) & = & 0, \newline
f_3(x) & = & 6,    & \ \ \ \ f_3(0) & = & 6, \newline
f_4(x) & = & 0,    & \ \ \ \ f_4(0) & = & 0. \newline
\end{array}
\end{equation}

Substitution of Eqn. \eqref{eqn:maclaurin-series-example-1a} to Eqn. \eqref{eqn:maclaurin-series} will produce

\begin{equation}
\label{eqn:maclaurin-series-example-1b}
\begin{array}{rcl}
f(x) & =  & \displaystyle f_0(0) \left( \frac{x^0}{0!} \right) + f_1(0) \left( \frac{x^1}{1!} \right) + f_2(0) \left( \frac{x^2}{2!} \right) + f_3(0) \left( \frac{x^3}{3!} \right) + f_4(0) \left( \frac{x^4}{4!} \right) + \dots \newline
& = & \displaystyle 0 \cdot \left( \frac{1}{1} \right) + 0 \cdot \left( \frac{x}{1} \right) + 0 \cdot \left( \frac{x^2}{2} \right) + 6 \cdot \left( \frac{x^3}{6} \right) + 0 \cdot \left( \frac{x^4}{24} \right) + \dots \newline
& = & x^3,
\end{array}
\end{equation}

which is the original function. Further derivative of $f(x)$, i.e. $n > 4$, will always zero since $f_4(x)$ is already a constant. You can test Eqn. \eqref{eqn:maclaurin-series} with another function and will get similar result as in Eqn. \eqref{eqn:maclaurin-series-example-1b} that gives the original function. If the series is infinite, then you must decide number of terms to be considered. More terms will give better approximation of the function $f(x)$.


## Infinite series
There are well-known infinite series for some function obtained using Maclaurin series, e.g.

\begin{equation}
\label{eqn:maclaurin-serie-sin-x}
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots,
\end{equation}

\begin{equation}
\label{eqn:maclaurin-serie-cos-x}
\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots,
\end{equation}

\begin{equation}
\label{eqn:maclaurin-serie-1/(1-x)}
\displaystyle \frac{1}{1 - x} = 1 + x + x^2 + x^3 + x^4 + x^5 + \dots,
\end{equation}

and

\begin{equation}
\label{eqn:maclaurin-serie-ln(1+x)}
\displaystyle \ln(1 + x) = x - \frac12 x^2 + \frac13 x^3 - \frac14 x^4 + \frac15 x^5 - \frac16 x^6 + \dots,
\end{equation}
 
where you can find their explicit forms and also other functions [[1](#ref1), [2](#ref2)].


## Application
In [simple harmonic motion](simple-harmonic-motion) for the case of simple pendulum, you will use small angle approximation or the approximation of $\sin \theta$, which is only the first term in Eqn. \eqref{eqn:maclaurin-serie-sin-x}, i.e. $\sin \theta \approx \theta$.


## References
1. <a name="ref1"></a>Wikipedia contributors, "Taylor series", Wikipedia, The Free Encyclopedia, 8 Nov 2020, 09:09 UTC, url <https://en.wikipedia.org/w/index.php?oldid=987632839> [20201114].
2. <a name="ref2"></a>Eric W. Weisstein, "Maclaurin Series", From MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/MaclaurinSeries.html> [20201114].
3. <a name="ref3"></a>Wikipedia contributors, "Factorial", Wikipedia, The Free Encyclopedia, 21 Oct 2020, 22:22 UTC, url <https://en.wikipedia.org/w/index.php?oldid=984755821> [20201114].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-11-14-maclaurin-series.md)
