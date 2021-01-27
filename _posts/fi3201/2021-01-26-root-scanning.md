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
f(x) = \left\\{
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
f(x) = \frac{x}{\|x\|} = \frac{\|x\|}{x}.
\end{equation}

We will use the Eqn. \eqref{eqn:rs-sign-function-non-zero} instead of \eqref{eqn:rs-sign-function} only for simplicity.


## algorithm
Assume that a function $f(x)$ already exists and we would like to find $x$ as a root of the function. 

Algorithm <a name="alg:rs-scanning-method-algorithm">1</a> Scanning method. \
`I`: $f(x)$, $x_{\rm beg}$, $x_{\rm end}$, $\Delta x$ \
`O`: $x_{\rm root}$
1. $x \leftarrow x_{\rm beg}$.
2. $\displaystyle S \leftarrow \frac{x}{\|x\|}$





## references
1. <a name="ref1"></a>Wikipedia contributors, "Root-finding algorithms", Wikipedia, The Free Encyclopedia, 15 January 2021, 23:25 UTC, <https://en.wikipedia.org/w/index.php?oldid=1000624440> [20210126].
2. <a name="ref1"></a>Wikipedia contributors, "Root-finding algorithms", Wikipedia, The Free Encyclopedia, 15 January 2021, 23:25 UTC, <https://en.wikipedia.org/w/index.php?oldid=1000624440> [20210126].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-26-root-scanning.md)



{% comment %}
## root of a function
If there is a function $f(x)$ then roots are values of $x$ that satisfy the condition [[2](#ref2), [3](#ref3), [4](#ref4)]

\begin{equation}
\label{eqn:root-function-zero}
f(x) = 0,
\end{equation}

where in general $x$ can also be a vector $\vec{r}$ or even a $n$-dimensional vector [[5](#ref5)]. Here we limit the discussion only to $x$.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/root/root-fx-0.png)
<br />
Figure <a name="fig:root-root-fx-0">1</a> A function $f(x)$ with three roots for $x \in [0, 10]$.
{: refdef}

Fig. <a href="#fig:root-root-fx-0">1</a> shows example of a function $f(x)$ that has roots of $1$, $5$, and $8$.


## another view
We can also view roots as solution when two functions has the same value, which satisfies

\begin{equation}
\label{eqn:root-two-function-equal}
g(x) = h(x),
\end{equation}

as illustrated in Fig. <a href="#fig:root-root-gx-hx">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/root/root-gx-hx.png)
<br />
Figure <a name="fig:root-root-gx-hx">1</a> Two functions $g(x)$ and $h(x)$ have the same value at two points for $x \in [0, 10]$.
{: refdef}

To satisfy Eqn. \eqref{eqn:root-two-function-equal} the roots are about $0$ and $6.5$ as shown in Fig. <a href="#fig:root-root-gx-hx">2</a>. Actually we can create a new function from Eqn. \eqref{eqn:root-two-function-equal} in the form of

\begin{equation}
\label{eqn:root-two-function-equal-one-function}
f(x) = h(x) - g(x) = 0
\end{equation}

to meet the condition in Eqn. \eqref{eqn:root-function-zero}.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/root/root-fx-gx-hx.png)
<br />
Figure <a name="fig:root-root-fx-gx-hx">3</a> The function $f(x) = h(x) - f(x) $ with two roots for $x \in [0, 10]$.
{: refdef}

The roots remain at about $x = 0$ and $x = 6.5$ when we use the relation in Eqn. \eqref{eqn:root-two-function-equal-one-function} as shown in Fig. <a href="#fig:root-root-fx-gx-hx">3</a>, where the blue curve is result of substration of green curve with red curve from Fig. <a href="#fig:root-root-gx-hx">2</a>. 


## a way to indicate root position
One way to indicate position of a root is using a graphical approach, which has been shown in Figs. <a href="#fig:root-root-fx-0">1</a>, <a href="#fig:root-root-gx-hx">2</a>, and <a href="#fig:root-root-fx-gx-hx">3</a>. This waay is fast but not accurate since the value depends on the grid size of the chart, where in last examples the value $6.5$ is only a guess, since it can be any number between $6$ and $7$. It is recommended to use this approach to isolate the range where the root lies, and then use other method to find the root with higher accuracy. We will not discuss about precision of the result since only use one attemp. These two terms have different meaning [[6](#ref6)].


## root finding algorithms
There are some algorithms in finding root of a function [[7](#ref7)], e.g.

+ bisection method
+ Newton's method
+ secant method

and also a not-accurate, not-so-efficient, and step-dependent method is [scanning method](fi3201/root-scanning).

For quadratic equation it is advised to used the [quadratic formula](/fi3201/quadratic-formula) instead of solved it numericallya, even it will work.
{% endcomment %}
