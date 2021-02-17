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
date: 2021-02-17 09:23:00 +07
permalink: /fi3201/polynomial-interpolation
---
For polynomial interpolation Lagrange polynomial is used [[1](#ref1)], where it passes through all the $N$ given points [[2](#ref2)]. In years 2000-2007 it still discussed in some textbooks [[3](#ref3)]. You can explore it with online calculator [[4](#ref4)] or write the code in C++, Java, Python3, and C# [[45(#ref5)].


\begin{equation}
\label{eqn:pi-formulation}
y(x) = x A + (1-x) B,
\end{equation}

{:refdef: style="text-align: center;"}
![..](/assets/img/math/intrpl/linear-interpolation-0-1.png)
<br />
Figure <a name="fig:li-linear-interpolation-0-1">1</a> Linear interpolation to calculate fraction of mixture $x$ representing substance $A$.
{: refdef}


## references
1. <a name="ref1"></a>Wikipedia contributors, "Lagrange polynomial", Wikipedia, The Free Encyclopedia, 28 Jan 2021, 21:48 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1003415092> [20210217].
2. <a name="ref2"></a>Branden Archer, Eric W. Weisstein, "Lagrange Interpolating Polynomial", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html> [20210217].
3. <a name="ref3"></a>-, "Lagrange Interpolation", ScienceDirect, url <https://www.sciencedirect.com/topics/mathematics/lagrange-interpolation> [20210217].
4. <a name="ref4"></a>-, "Lagrange Interpolating Polynomial: Lagrange Interpolation Calculator", DCode, url <https://www.dcode.fr/lagrange-interpolating-polynomial> [20210217].
5. <a name="ref5"></a>GeeksforGeeks, "GeeksforGeeks", GeeksforGeeks, 18 Feb 2020, url <https://www.geeksforgeeks.org/lagranges-interpolation/> [20210217].
