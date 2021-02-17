---
layout: post
author: viridi
title: polynomial interpolation
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "polynomial", "interpolation", "lagrange"]
date: 2021-02-17 11:23:00 +07
permalink: /fi3201/polynomial-interpolation
---
For polynomial interpolation Lagrange polynomial is used [[1](#ref1)], where it passes through all the $N$ given points [[2](#ref2)]. In years 2000-2007 it still discussed in some textbooks [[3](#ref3)]. You can explore it with online calculator [[4](#ref4)] or write the code in C++, Java, Python3, and C# [[5](#ref5)].


## difference with linear interpolation
Fig. <a href="#fig:pi-difference-with-linear-interpolation">1</a> shows the comparison between linear and polynomial interpolations. Note that in linear interpolation we use straight line in every range, but in polynomial interpolation curved line is used instead.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/intrpl/linear-interpolation-data-set.png) \
![..](/assets/img/math/intrpl/polynomial-interpolation.png)
<br />
Figure <a name="fig:pi-difference-with-linear-interpolation">1</a> Linear interpolation for data set (top) and polynomial interpolation for the same data set (bottom).
{: refdef}

If there are $N$ points then there will be $N-1$ equations of line or functions $f_n(x)$ with $n = 1, \dots, N-1$ when use linear interpolation

\begin{eqnarray}
\label{eqn:pi-linear-interpolation-functions}
\nonumber f_1(x) = m_1 x + n_1, \newline
\nonumber f_2(x) = m_2 x + n_2, \newline
\nonumber \dots, \newline
f_{N-1}(x) = m_{N-1} x + n_{N-1}.
\end{eqnarray}

But there will be only one function $f(x)$ in the form of polynomial function, when use the polynomial interpolation.

\begin{equation}
\label{eqn:pi-polynomial-interpolation}
f(x) = \sum_{n = 0}^{N-1} c_n x^n
\end{equation}

Eqn. \eqref{eqn:pi-polynomial-interpolation} will produce the curved line in every range between two successive points from the data set.

## lagrange polynomial
The polynomial function is

\begin{equation}
\label{eqn:pi-polynomial-interpolation-lagrange}
L(x) = \sum_{j = 1}^{N} y_j l_j(x),
\end{equation}

which is linear combination of Lagrange basis polynomial [[1](#ref1)]

\begin{equation}
\label{eqn:pi-polynomial-interpolation-lagrange-basis}
l_j(x) = \prod_{\begin{array}{c}m = 1\newline m \ne j\end{array}}^N \frac{x - x_m}{x_j - x_m}.
\end{equation}

### example
Let us try with example $(0, 1)$, $(1, 4)$, $(2, 5)$, $(3, 4)$, and $(4, 1)$. We can make following table

$j$ | 1 | 2 | 3 | 4 | 5
--- |---|---|---|---|---
$x$ | 0 | 1 | 2 | 3 | 4
$y$ | 1 | 4 | 5 | 4 | 1

\begin{equation}
\label{eqn:pi-li-1}
l_1(x) = \left(\frac{x - x_2}{x_1 - x_2} \right) \left( \frac{x - x_3}{x_1 - x_3} \right) \left( \frac{x - x_4}{x_1 - x_4} \right) \left( \frac{x - x_5}{x_1 - x_5} \right),
\end{equation}

\begin{equation}
\label{eqn:pi-li-2}
l_2(x) = \left(\frac{x - x_1}{x_2 - x_1} \right) \left( \frac{x - x_3}{x_2 - x_3} \right) \left( \frac{x - x_4}{x_2 - x_4} \right) \left( \frac{x - x_5}{x_2 - x_5} \right),
\end{equation}

\begin{equation}
\label{eqn:pi-li-3}
l_3(x) = \left(\frac{x - x_1}{x_3 - x_1} \right) \left( \frac{x - x_2}{x_3 - x_2} \right) \left( \frac{x - x_4}{x_3 - x_4} \right) \left( \frac{x - x_5}{x_3 - x_5} \right),
\end{equation}

\begin{equation}
\label{eqn:pi-li-4}
l_4(x) = \left(\frac{x - x_1}{x_4 - x_1} \right) \left( \frac{x - x_2}{x_4 - x_2} \right) \left( \frac{x - x_3}{x_4 - x_3} \right) \left( \frac{x - x_5}{x_4 - x_5} \right),
\end{equation}

\begin{equation}
\label{eqn:pi-li-5}
l_5(x) = \left(\frac{x - x_1}{x_5 - x_1} \right) \left( \frac{x - x_2}{x_5 - x_2} \right) \left( \frac{x - x_3}{x_5 - x_3} \right) \left( \frac{x - x_4}{x_5 - x_4} \right),
\end{equation}

and then

\begin{equation}
\label{eqn:pi-L}
L(x) = l_1(x) + l_2(x) + l_3(x) + l_4(x) + l_5(x)
\end{equation}

is the polynomial.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Lagrange polynomial", Wikipedia, The Free Encyclopedia, 28 Jan 2021, 21:48 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1003415092> [20210217].
2. <a name="ref2"></a>Branden Archer, Eric W. Weisstein, "Lagrange Interpolating Polynomial", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html> [20210217].
3. <a name="ref3"></a>-, "Lagrange Interpolation", ScienceDirect, url <https://www.sciencedirect.com/topics/mathematics/lagrange-interpolation> [20210217].
4. <a name="ref4"></a>-, "Lagrange Interpolating Polynomial: Lagrange Interpolation Calculator", DCode, url <https://www.dcode.fr/lagrange-interpolating-polynomial> [20210217].
5. <a name="ref5"></a>GeeksforGeeks, "GeeksforGeeks", GeeksforGeeks, 18 Feb 2020, url <https://www.geeksforgeeks.org/lagranges-interpolation/> [20210217].
