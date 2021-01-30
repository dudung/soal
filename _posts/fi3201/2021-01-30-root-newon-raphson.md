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

## tangent
A tangent line to a curve at a certain point is a straight line that touches the curve at the point [[2](#ref2)]. If the curve is simply function of one variable, namely $x$, then we can have the curve as a function $f(x)$.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/line/line-tangent-1-d.png)
<br />
Figure <a name="fig:rnr-line-tangent-1-d">1</a> Tanget line of a curve $f(x)$ at point $x = x_1$. 
{: refdef}

If the point is $x = x_1$ then the tangent should pass the point $(x_1, f(x_1))$ and the gradient of the line is simply $f'(x_1)$ as shown in Fig. <a href="#fig:rnr-line-tangent-1-d">1</a>.


## equation of a line
A line with gradient $m$ and is passing point $(0, n)$ will have equation of

\begin{equation}
\label{eqn:rnr-equation-of-a-line}
y = mx + n,
\end{equation}

which is known as equation of a line [[3](#ref3)]. If we measure the angle between the line and $x$ axis as $\theta$ then

\begin{equation}
\label{eqn:rnr-gradient-tan-theta}
m = \tan \theta
\end{equation}

is the relation between gradient $m$ and the angle $\theta$.

Fig. <a href="#fig:rnr-line-gradient-theta-intercept">2</a> shows the relation between gradient $m$ and $\tan\theta$.


## derivation
The formula in Eqn. \eqref{eqn:rnr-newton-raphson-method} can be derived using equation of a line in Eqn. \eqref{eqn:rnr-equation-of-a-line}.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Newton's method", Wikipedia, The Free Encyclopedia, 9 January 2021, 08:37 UTC, <https://en.wikipedia.org/w/index.php?oldid=999264602> [20210130].
2. <a name="ref2"></a>Wikipedia contributors, "Tangent", Wikipedia, The Free Encyclopedia, 12 January 2021, 05:18 UTC, <https://en.wikipedia.org/w/index.php?oldid=999834620> [20210130].
3. <a name="ref3"></a>Wikipedia contributors, "Linear equation", Wikipedia, The Free Encyclopedia, 11 November 2020, 23:58 UTC, <https://en.wikipedia.org/w/index.php?oldid=988244807> [20210130].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-30-root-newton-raphson.md)
