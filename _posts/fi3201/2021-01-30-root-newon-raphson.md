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

{:refdef: style="text-align: center;"}
![..](/assets/img/math/line/line-equation-1-d.png)
<br />
Figure <a name="fig:rnr-line-equation-1-d">2</a> A line passing $(x_1, y_1)$ has gradient of $m$ and $y$ is $n$. 
{: refdef}

Fig. <a href="#fig:fig:rnr-line-equation-1-d">2</a> shows the relation between gradient $m$ and $\theta$ through Eqn. \eqref{eqn:rnr-gradient-tan-theta}.

The $y$ intercept is obtained when we set $x = 0$. And there also another way to get the equation when we know that the function is passing a point, namely $(x_1, y_1)$, through

\begin{equation}
\label{eqn:rnr-line-x1-y1}
y = m(x - x_1) + y_1,
\end{equation}

when we know the gradient $m$ and

\begin{equation}
\label{eqn:rnr-line-x1-y1-n}
n = y_1 - m x_1
\end{equation}

is the relation between $n$ and the point $(x_1, y_1)$, obtained by equating Eqn. \eqref{eqn:rnr-equation-of-a-line} with Eqn. \eqref{eqn:rnr-line-x1-y1}.


## derivation
The formula in Eqn. \eqref{eqn:rnr-newton-raphson-method} can be derived using equation of a line in Eqn. \eqref{eqn:rnr-equation-of-a-line}.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/root/root-newton-raphson.png)
<br />
Figure <a name="fig:rnr-root-newton-raphson">3</a> Steps performed in Newton-Raphson method in obtaning $x_1$, $x_2$, until it gets $x_\infty$ with certain accurary. 
{: refdef}

Let $x_1$ is the initial guess, then point on the function is $(x_1, f_1)$ where $f_1 = f(x_1)$ and gradient of the tangent is $f_1' = f_1'(x_1)$. Using this information we can have equation of the first tangent line using Eqn. \eqref{eqn:rnr-line-x1-y1}

\begin{equation}
\label{eqn:rnr-tangent-line-1}
y_1^{\tan} = f_1' (x - x_1) + f_1.
\end{equation}

To find $x$ intercept of Eqn. \eqref{eqn:rnr-tangent-line-1} we set $y_1^{\tan} = 0$

\begin{equation}
\label{eqn:rnr-tangent-line-1-step-by-step}
\begin{array}{rcl}
0 & = & f_1' (x - x_1) + f_1 \newline
0 & = & f_1' x - f_1' x_1 + f_1 \newline
f_1' x_1 & = & f_1' x  + f_1 \newline
f_1' x_1 - f_1 & = & f_1' x \newline
f_1' x & = & f_1' x_1 - f_1 \newline
x & = & \displaystyle x_1 - \frac{f_1}{f_1'} \newline
x_2 & = & \displaystyle x_1 - \frac{f(x_1)}{f'(x_1)}
\end{array}
\end{equation}

and name the solution as $x_2$. We can repeat it for using $x_2$ as updated guess

\begin{equation}
\label{eqn:rnr-tangent-line-2}
y_2^{\tan} = f_2' (x - x_2) + f_2.
\end{equation}

Then following similar steps we can have

\begin{equation}
\label{eqn:rnr-tangent-line-2-step-by-step}
\begin{array}{rcl}
0 & = & f_2' (x - x_2) + f_2 \newline
0 & = & f_2' x - f_2' x_2 + f_2 \newline
f_2' x_2 & = & f_2' x  + f_2 \newline
f_2' x_2 - f_2 & = & f_2' x \newline
f_2' x & = & f_2' x_2 - f_2 \newline
x & = & \displaystyle x_2 - \frac{f_2}{f_2'} \newline
x_3 & = & \displaystyle x_2 - \frac{f(x_2)}{f'(x_2)}
\end{array}
\end{equation}

and name the solution as $x_3$. By observing the relation pattern between $x_2$ and $x_1$ in Eqn. \eqref{eqn:rnr-tangent-line-1-step-by-step} and between $x_3$ and $x_2$ in Eqn. \eqref{eqn:rnr-tangent-line-2-step-by-step} we can have Eqn. \eqref{eqn:rnr-newton-raphson-method} that relates $x_{n+1}$ with $x_n$ using $f(x_n)$ and $f'(x_n)$.

## algorithm
Eqn. \eqref{eqn:rnr-newton-raphson-method} can be described in following algorithm. We assume that at least one root does exist for $f(x)$.

Algorithm <a name="alg:rnr-newton-raphson-method-algorithm">1</a> Newton-Raphson method. \
`I`: $f(x)$, $f'(x)$, $x_1$, $\epsilon$. \
`O`: $x_{\rm root}$.
1. $n = 1$.
2. $\displaystyle x_{n+1} \leftarrow x_n - \frac{f(x_n)}{f'(x_n)}$.
3. $\|f(x_{n+1})\| < \epsilon \Rightarrow \color{blue}{\bf\scriptsize STEP} \ 6$.
4. $n = n + 1$.
5. $\Rightarrow \color{blue}{\bf\scriptsize STEP} \ 2$.
6. $x_{\rm root} = x_{n+1}$.

There might be many another variations of algorithm than shown in Alg. <a href="#alg:rnr-newton-raphson-method-algorithm">1</a>.


## flowchart
As alternative to Alg. <a href="#alg:rnr-newton-raphson-method-algorithm">1</a> we can also have following flowchart for Eqn. \eqref{eqn:rnr-newton-raphson-method}.


## exercises
1. Study Eqns. \eqref{eqn:rnr-tangent-line-1} - \eqref{eqn:rnr-tangent-line-2} in obtaining the relation in Eqn. \eqref{eqn:rnr-newton-raphson-method}, then use it in a spreadsheet to see how it works in producing root of $x^2 - 9 = 0$ when $x_1 = 2$. What is the answer when $x_1 = -4$? Explain results difference due to the choice of initial guess.
2. Create another variation of Alg. <a href="#alg:rnr-newton-raphson-method-algorithm">1</a>, e.g. change the order of checking $\|f(x_{n+1})\|$ and incresing $n$.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Newton's method", Wikipedia, The Free Encyclopedia, 9 January 2021, 08:37 UTC, <https://en.wikipedia.org/w/index.php?oldid=999264602> [20210130].
2. <a name="ref2"></a>Wikipedia contributors, "Tangent", Wikipedia, The Free Encyclopedia, 12 January 2021, 05:18 UTC, <https://en.wikipedia.org/w/index.php?oldid=999834620> [20210130].
3. <a name="ref3"></a>Wikipedia contributors, "Linear equation", Wikipedia, The Free Encyclopedia, 11 November 2020, 23:58 UTC, <https://en.wikipedia.org/w/index.php?oldid=988244807> [20210130].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-30-root-newton-raphson.md)
