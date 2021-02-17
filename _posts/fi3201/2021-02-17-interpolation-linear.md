---
layout: post
author: viridi
title: linear interpolation
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "linear", "interpolation"]
date: 2021-02-17 09:08:00 +07
permalink: /fi3201/linear-interpolation
---
If there is a discrete set of data points, to construct new data points within the range of the known data we can use a method of curve fitting using linear polynomials known as linear interpolation [[1](#ref1)]. Due its simplicity this method is still used in may areas nowadays [[2](#ref2)]. In binary diagram of mixture of two substances, where the horizontal axis represents concentration of one substance, it uses linear interpolation [[3](#ref3)]. You can use a spreadsheet, e.g. Microsoft Excel [[4](#ref4)], or an online calculator [[5](#ref5)] to perform an interpolation.


## in [0,1] range
In $y-x$ diagram, suppose that we have two points $(0, B)$ and $(1, A)$ and we want to get value of $y$ at certain value of $x \in [0, 1]$ as illustrated in Fig. <a href="#fig:li-linear-interpolation-0-1">1</a>

{:refdef: style="text-align: center;"}
![..](/assets/img/math/intrpl/linear-interpolation-0-1.png)
<br />
Figure <a name="fig:li-linear-interpolation-0-1">1</a> Linear interpolation to calculate fraction of mixture $x$ representing substance $A$.
{: refdef}

We can have that

\begin{equation}
\label{eqn:li-in-range-0-1}
y(x) = x A + (1-x) B,
\end{equation}

that produces $y(0) = B$ and $y(1) = A$ as desired with

\begin{equation}
\label{eqn:li-fraction-x}
x = \frac{\chi_A}{\chi_A + \chi_B},
\end{equation}

where $\chi$ can be mass, volume, or other properties of the substances, which gives that $x = 0$ is pure substance of $B$ and $x = 1$ is pure substance of $A$.


## in arbitrary range
Suppose we have two points $(x_1, y_1)$ and $(x_2, y_2)$ and want to have $y$ at certain value of $x \in [x_1, y1]$ as given in Fig. <a href="#fig:li-linear-interpolation-x1-x2">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/intrpl/linear-interpolation-x1-x2.png)
<br />
Figure <a name="fig:li-linear-interpolation-x1-x2">2</a> Linear interpolation to calculate $x \in[x_1, x_2]$.
{: refdef}

Gradient of line passing the two points $(x_1, y_1)$ and $(x_2, y_2)$ is

\begin{equation}
\label{eqn:li-gradient-x1-y1-x2-y2}
m = \frac{y_2 - y_1}{x_2 - x_1}
\end{equation}

and the equation of a line can be constructed using

\begin{equation}
\label{eqn:li-equation-of-a-line-x1-y1-x2-y2-construction}
y = m(x - x_1) + y_1 = m(x - x_2) + y_2,
\end{equation}

that gives

\begin{equation}
\label{eqn:li-equation-of-a-line-x1-y1-x2-y2}
y = \left( \frac{y_2 - y_1}{x_2 - x_1} \right) x + \left( \frac{y_1 x_2 - x_1 y_2}{x_2 - x_1} \right).
\end{equation}

Since we will deal with the linear interpolation using numerical approach, Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2-construction} is recommended to memorize since it is simpler than Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2}.


## data set
If there is data set consists of pairs of $(x_1, y_1)$, $(x_2, y_2)$, $\dots$, $(x_N, y_N)$, then we require to perform the linear interpolation in each range $x_{n} \le x \le x_{n+1}$, where there will be only $N-1$ ranges, that is assumed have equal interval for simplicity.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/intrpl/linear-interpolation-data-set.png)
<br />
Figure <a name="fig:li-linear-interpolation-data-set">3</a> Linear interpolation in each range with equal interval of a data set.
{: refdef}

Fig. <a href="#fig:li-linear-interpolation-data-set">3</a> shows linear interpolation for a data set. With equal interval we can obtain the range using

\begin{equation}
\label{eqn:li-range-determination}
n = 1 + \left\lfloor \frac{x - x_1}{\Delta x} \right\rfloor,
\end{equation}

where $\Delta x$ is the interval of each range. After get the value of $n$, we use

\begin{equation}
\label{eqn:li-linear-interpolation-data-set}
y = \left( \frac{y_{n+1} - y_n}{x_{n+1} - x_n} \right) x + \left( \frac{y_n x_{n+1} - x_n y_{n+1}}{x_{n+1} - x_n} \right),
\end{equation}

which is actually Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2} but for each range indicated with the index $n$.


## implementation
Using common programming language, e.g. C++, JavaScript, or Python you can implement Eqns. \eqref{eqn:li-range-determination} and \eqref{eqn:li-linear-interpolation-data-set} to do the interpolation. Array for the data set is required.


## exercises
1. If $x = 0.25$ find the fraction of $B$ and $A$ using Fig. <a href="#fig:li-linear-interpolation">1</a>.
2. Prove that center and right side of Eqn. {eqn:li-equation-of-a-line-x1-y1-x2-y2-construction} do produce the same results as in Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2}.
3. Test Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2} that it holds for the two points $(x1, y1)$ and $(x2, y2)$.
4. If we transform all $x$s to $x - x_1$ we can obtain Eqn. \eqref{eqn:li-in-range-0-1} from Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2} with $y_1 = B$ and $y_2 = A$. Show how to do that in a shortes way you are able to. You might need to define new $x$, which is dimensionless.
5. Prove that Eqn. \eqref{eqn:li-linear-interpolation-data-set} holds in its range for lower and upper bounds, $(x_n, y_n)$ and $(x_{n+1}, y_{n+1})$, respectively.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Linear interpolation", Wikipedia, The Free Encyclopedia, 2 Feb 2021, 04:04 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1004343292> [20210122].
2. <a name="ref2"></a>-, "Linear Interpolation", ScienceDirect, url <https://www.sciencedirect.com/topics/engineering/linear-interpolation> [20210217].
3. <a name="ref3"></a>Glenda Smith, Denise Watts, "Binary phase diagrams", PetroWiki, Society of Petroleum Engineers (SPE), 
Richardson, Texas 75080, 2 Jun 2015 at 11:53, url <https://petrowiki.spe.org/Binary_phase_diagrams> [20210217].
4. <a name="ref4"></a>-, "Linear Interpolation with Excel", Dagra Graph Digitizer, url <https://www.datadigitization.com/dagra-in-action/linear-interpolation-with-excel/> [20210217].
5. <a name="ref5"></a>-, "Linear interpolation and extrapolation with calculator", x-engineer.org, Engineering Tutorials, url <https://x-engineer.org/undergraduate-engineering/advanced-mathematics/numerical-methods/linear-interpolation-and-extrapolation-with-calculator/> [20210217].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-02-17-interpolation-linear.md)
