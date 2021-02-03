---
layout: post
author: viridi
title: root secant
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "root", "newton", "newton-raphson"]
date: 2021-02-03 09:20:00 +07
permalink: /fi3201/root-secant
---
Not like the [Newton-Raphson method](/fi3201/root-newton-raphson) that requires a function and its derivative, secant method approximates the derivative with finite-difference method, even it is said that this method actually predates the Newton-Raphson method [[1](#ref1)]. With the approximation it will save large amount of CPU time for machine calculations or considerable amount of effort to do hand calculations if the function has complicated expression, and it gives also a method that converges as fast as the Newton-Raphson method [[2](#ref2)]. This method has still been used in engineering [[3](#ref3)] and improved in mathematics [[4](#ref4)]. This method can be used in Wolfram Languange with `SecantMethodList` [[5](#ref5)] and there is example of implementation of this method in Python [[6](#ref6)].


## formula
Secant method has the formula of

\begin{equation}
\label{eqn:rs-secant-method}
x_{n+2} = x_{n+1} - f(x_{n+1}) \left[ \frac{x_{n+1} - x_n}{f(x_{n+1}) - f(x_n)} \right],
\end{equation}

where $x_{n+1} = x_n + \Delta x$.


## finite difference
We can use finite difference as an approximation of derivative [[7](#ref7)]

\begin{equation}
\label{rs-derivative-finite-difference}
f'(x) \approx \frac{f(x+\Delta x) - f(x)}{\Delta x},
\end{equation}

which will substitute the derivative term $f'(x)$ in Newton-Raphson method

\begin{equation}
\label{eqn:rs-newton-raphson-method}
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\end{equation}

and procude Eqn. \eqref{eqn:rs-secant-method}.


## algorithm
Eqn. \eqref{eqn:rs-secant-method} can be described in following algorithm. We assume that at least one root does exist for $f(x)$.

Algorithm <a name="alg:rs-secant-method-algorithm">1</a> Secant method. \
`I`: $f(x)$, $x_1$, $x_2$, $\epsilon$. \
`O`: $x_{\rm root}$.
1. $n = 1$.
2. $\displaystyle x_{n+2} \leftarrow x_{n+1} - \frac{f(x_{n+1})(x_{n+1} - x_n)}{f(x_{n+1}) - f(x_n)}$.
3. $\|f(x_{n+2})\| < \epsilon \Rightarrow \color{blue}{\bf\scriptsize STEP} \ 6$.
4. $n = n + 2$.
5. $\Rightarrow \color{blue}{\bf\scriptsize STEP} \ 2$.
6. $x_{\rm root} = x_{n+2}$.

Notice that different than Newton-Raphson method, $f'(x)$ is not required but we need also $x_2$ instead of only $x_1$ as the initial guess. And as always there might be many another variations of algorithm than shown in Alg. <a href="#alg:rs-secant-method-algorithm">1</a>.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Secant method", Wikipedia, The Free Encyclopedia, 4 January 2021, 18:18 UTC, <https://en.wikipedia.org/w/index.php?oldid=998290429> [20210103].
2. <a name="ref2"></a>Sanyasiraju V. S. S. Yedida, "Secant Method", Department of Mathematics, Indian Institute of Technology Madras, Chennai, url <https://mat.iitm.ac.in/home/sryedida/public_html/caimna/transcendental/iteration%20methods/secant/secant.html> [20210103].
3. <a name="ref3"></a>-, "Secant Method", url <https://www.sciencedirect.com/topics/engineering/secant-method> [20210203].
4. <a name="ref4"></a>-, "Secant Method", url <https://www.sciencedirect.com/topics/mathematics/secant-method> [20210203]. 
5. <a name="ref5"></a>Eric W. Weisstein, "Secant Method" from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/SecantMethod.html> [20210203].
6. <a name="ref7"></a>Patrick Walls, "Secant Method", Mathematical Python, Department of Mathematics, the University of British Columbia, Wed 4 Dec 2019 17:20:04 PST, url <https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/secant/> [20210203].
7. <a name="ref7"></a>Wikipedia contributors, "Finite difference", Wikipedia, The Free Encyclopedia, 22 January 2021, 00:28 UTC, <https://en.wikipedia.org/w/index.php?oldid=1001922880> [20210103]

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-02-03-root-secant.md)
