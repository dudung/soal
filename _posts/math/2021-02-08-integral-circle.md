---
layout: post
author: viridi
title: integral circle
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["integral", "integration", "circle", "area", "arc", "circumference"]
date: 2021-02-08 09:51:00 +07
permalink: /math/integral-circle
---
Using polar coordinate system [[1](#ref1)], we can find length of arc and surface area of a circle, easier than using Cartesian coordinate in find the area [[2](#ref2)] and arc length in general [[3](#ref3)].


## polar coordinate system
Comparation of Cartesian and polar coordinates systems are given in Fig. <a href="#fig:ic-cs-xy-rtheta">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/cs/cs-xy-rtheta.png)
<br />
Figure <a name="fig:ic-cs-xy-rtheta">1</a> Cartesian coordinate system (left) and polar coordinate system (righ).
{: refdef}

In Cartesian coordinate system a position vector $\vec{r}$ is defined using two components $x$ and $y$, which are measured along $x$ and $y$ axes. The projection of $\vec{r}$ along each axis should be perpendicular to the axis. In polar coordinate a position vector is defined using two components $r$ and $\theta$, where the first is always along the vector itself, while the second is angle measured from a reference axis (normally $x$ axis) in a certain direction (normally counter clockwise direction). Some relations are

\begin{equation}
\label{eqn:ic-cs-x}
x = r \cos\theta,
\end{equation}

\begin{equation}
\label{eqn:ic-cs-y}
y = r \sin\theta
\end{equation}

and

\begin{equation}
\label{eqn:ic-cs-r}
r = \sqrt{x^2 + y^2},
\end{equation}

\begin{equation}
\label{eqn:ic-cs-theta}
\tan\theta = \frac{y}{x}.
\end{equation}


## elements of length and area
Length element $dl$ in polar coordinate system can be

\begin{equation}
\label{eqn:ic-cs-polar-length-element-radial}
dl = dr
\end{equation}

or

\begin{equation}
\label{eqn:ic-cs-polar-length-element-angular}
dl = r d\theta
\end{equation}

as shown in Fig. <a href="#fig:ic-cs-rtheta-element">2</a> (left).

{:refdef: style="text-align: center;"}
![..](/assets/img/math/cs/cs-rtheta-element.png)
<br />
Figure <a name="fig:ic-cs-rtheta-element">2</a> Elements of length (left) and area (right) in polar coordinate system.
{: refdef}

Then using Eqns. \eqref{eqn:ic-cs-polar-length-element-radial} and \eqref{eqn:ic-cs-polar-length-element-angular} we can have area element $dA$ for polar coordinate system

\begin{equation}
\label{eqn:ic-cs-polar-area-element}
dA = (dr)(r d\theta) = rdr d\theta
\end{equation}

as given in Fig. <a href="#fig:ic-cs-rtheta-element">2</a> (right), where the element is located at position $\vec{r}$.

### circumference
We can calculate circumference using Eqn. \eqref{eqn:ic-cs-polar-length-element-angular} through

\begin{equation}
\label{eqn:ic-cs-polar-circumference}
C = \int_0^{2\pi} Rd\theta = R \int_0^{2\pi} d\theta = R[\theta]_0^{2\pi} = R(2\pi - 0) = 2\pi R = \pi D,
\end{equation}

as we know [[4](#ref4)] with $D = 2R$. We use $r = R$ in Eqn. \eqref{eqn:ic-cs-polar-circumference} since $r$ is coordinate variable and $R$ is a value.

### area of circle
Using Eqn. \eqref{eqn:ic-cs-polar-area-element} we can have area of circle [[5](#ref5)]. To do that we use following equation

\begin{equation}
\label{eqn:ic-cs-polar-area-of-circle}
A = \int dA = \int_0^{R} \int_0^{2\pi} rdr d\theta = \int_0^{R}   rdr \int_0^{2\pi} d\theta.
\end{equation}

First term from the left in the most right side of Eqn. \eqref{eqn:ic-cs-polar-area-of-circle} gives

\begin{equation}
\label{eqn:ic-cs-polar-area-of-circle-part-r}
\int_0^R rdr = \left[ \frac12 r^2 \right]_0^R = \frac12 (R^2 - 0) = \frac12 R^2
\end{equation}

and the second produces

\begin{equation}
\label{eqn:ic-cs-polar-area-of-circle-part-theta}
\int_0^{2\pi} d\theta = [\theta]_0^{2\pi} = 2\pi - 0 = 2\pi.
\end{equation}

Substitution of Eqn. \eqref{eqn:ic-cs-polar-area-of-circle-part-r} and \eqref{eqn:ic-cs-polar-area-of-circle-part-theta} into Eqn. \eqref{eqn:ic-cs-polar-area-of-circle} will given

\begin{equation}
\label{eqn:ic-cs-polar-area-of-circle-proof}
A = \left( \frac12 R^2 \right) (2\pi) = \pi R^2.
\end{equation}

Results in Eqns. \eqref{eqn:ic-cs-polar-circumference} and \eqref{eqn:ic-cs-polar-area-of-circle-proof} are only to convince you with the prior knowledge about circumference [[4](#ref4)] and area of circle [[5](#ref5)], that the form of elements of length and area in polar coordinate system are as given in Eqns. \eqref{eqn:ic-cs-polar-length-element-radial}, \eqref{eqn:ic-cs-polar-length-element-angular}, and \eqref{eqn:ic-cs-polar-area-element}.


## some forms
Using Eqns. Eqns. \eqref{eqn:ic-cs-polar-length-element-radial}, \eqref{eqn:ic-cs-polar-length-element-angular}, and \eqref{eqn:ic-cs-polar-area-element} we can calculate arc and area of some forms.

### annulus
Area of an annulus can be obtained using [[6](#ref6)]

\begin{equation}
\label{eqn:ic-cs-polar-area-of-annulus}
A_{\rm annulus} = \pi (R_2^2 - R_1^2)
\end{equation}

with $R_1 < R_2$, where $R_1$ is inner radius and $R_2$ is outter radius. Fig. <a href="#fig:ic-cs-area-annulus">3</a> shows area of an annulus and annulus sector, where element of area in polar coordinate system is given in Fig. <a href="#fig:ic-cs-rtheta-element">2</a> (right).

{:refdef: style="text-align: center;"}
![..](/assets/img/math/cs/cs-area-annulus.png)
<br />
Figure <a name="fig:ic-cs-area-annulus">3</a> Area of an annulus (left) and annulus sector (right). 
{: refdef}

Can you see that when $R_1 = 0$ then area of an annulus becomes area of a circle?

### annulus sector
Use Eqn. \eqref{eqn:ic-cs-polar-area-of-circle} with $R_1$, $R_2$, $\theta_1$, and $\theta_2$

\begin{equation}
\label{eqn:ic-cs-polar-area-of-annulus-sector}
A = \int_{R_1}^{R_2} rdr \int_{\theta_1}^{\theta_2} d\theta = \frac12 (\theta_2 - \theta_1) (R_2^2 - R_1^2),
\end{equation}

which is an annulus sector [[7](#ref7)]. Eqn. \eqref{eqn:ic-cs-polar-area-of-annulus-sector} can turn into Eqn. \eqref{eqn:ic-cs-polar-area-of-annulus} when $\theta_2 - \theta_1 = 2\pi$ as in Eqn. \eqref{eqn:ic-cs-polar-area-of-circle-part-theta}, which is special case with $\theta_2 = 2\pi$ and $\theta_1 = 0$ as lower and upper bounds of the integral.


## exercises
1. How you can use Eqn. \eqref{eqn:ic-cs-polar-circumference} to calculate perimeter of a semicircle? Do not forget the diameter in this case.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Polar coordinate system", Wikipedia, The Free Encyclopedia, 6 Jan 2021, 13:02 UTC, url <https://en.wikipedia.org/w/index.php?oldid=998664169> [20210208].
2. <a name="ref2"></a>-, "Area of Part of a Circle", 18.01SC Single Variable Calculus, MIT OpenCourseWare, Fall 2010, url <https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/unit-4-techniques-of-integration/part-a-trigonometric-powers-trigonometric-substitution-and-completing-the-square/session-70-preview-of-trig-substitution-and-polar-coordinates/MIT18_01SCF10_Ses70a.pdf> [20210208].
3. <a name="ref3"></a>Justin Ko, " Using Integration to Find Arc Lengths and Surface Areas", MAT186 – Week 12, 26 November 2019, url <https://www.math.toronto.edu/jko/MAT186_week_12.pdf> [20210208].
4. <a name="ref4"></a>Wikipedia contributors, "Area of a circle", Wikipedia, The Free Encyclopedia, 2 Jan 2021, 19:55 UTC, url <https://en.wikipedia.org/w/index.php?oldid=997898869> [20210208].
5. <a name="ref5"></a>Wikipedia contributors, "Circumference", Wikipedia, The Free Encyclopedia, 1 Jan 2021, 22:56 UTC, url <https://en.wikipedia.org/w/index.php?oldid=997724428> [20210208].
6. <a name="ref6"></a>-, "Annulus", MathisFun, 2018, url <https://www.mathsisfun.com/geometry/annulus.html> [20210208].
7. <a name="ref7"></a>Jürgen Kummer, "Annulus Sector Calculator", Jumk.de Webprojects, url <https://rechneronline.de/pi/annulus-sector.php> [20210208].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/math/2021-02-08-integral-circle.md)

