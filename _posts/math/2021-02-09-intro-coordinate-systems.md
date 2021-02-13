---
layout: post
author: viridi
title: intro coordinate systems
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["coordinate system", "coordinate", "intro"]
date: 2021-02-13 19:09:00 +07
permalink: /math/intro-coordinate-systems
---
Polar coordinate system [[1](#ref1)] and cylindrical coordinates system [[2](#ref2)] are in brief introduced and discussed here. As comparation cartesian coordinate system [[3](#ref3)] is also mentioned.


## rectangular coordinate systems
Cartesian coordinate system, also called rectangular coordinate system [[4](#ref4)], can be in two- or three-dimesion.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/cs/cs-cartesian-cartesian.png)
<br />
Figure <a name="fig:ics-cartesian-cartesian">1</a> Cartesian coordinate system in: 2-d (left) and 3-d (right).
{: refdef}

In 3-d system there are only $x$ and $y$ components, while in 3-d system we have additional $z$ component as illustrated in Fig. <a href="#fig:ics-cartesian-cartesian">1</a>. A vector is written in the form of

\begin{equation}
\label{eqn:ics-vector-2d}
\vec{r} = x \hat{x} + y \hat{y}
\end{equation}

for 2-d system and

\begin{equation}
\label{eqn:ics-vector-3d}
\vec{r} = x \hat{x} + y \hat{y} + z \hat{z}
\end{equation}

form 3-d system. Length of vector in Eqn. \eqref{eqn:ics-vector-2d} is $\sqrt{x^2 + y^2}$, while in Eqn. \eqref{eqn:ics-vector-3d} is $\sqrt{x^2 + y^2 + z^2}$.


## polar coordinate system
We can compare the Cartesian and polar coordinates systems as shown in Fig. <a href="#fig:ics-cs-xy-rtheta">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/cs/cs-xy-rtheta.png)
<br />
Figure <a name="fig:ics-cs-xy-rtheta">2</a> Cartesian coordinate system (left) and polar coordinate system (right).
{: refdef}

A position vector $\vec{r}$ in Cartesian coordinate system is defined using two components $x$ and $y$, where they are measured along $x$ and $y$ axes. The projection of $\vec{r}$ along each axis should be perpendicular to the axis. A position vector in polar coordinate is defined using two components $r$ and $\theta$, where the first component is always along the vector itself, while the second one is angle measured from a $x$ axis in counter clockwise direction. There are ome relations

\begin{equation}
\label{eqn:ics-cs-x}
x = r \cos\theta,
\end{equation}

\begin{equation}
\label{eqn:ics-cs-y}
y = r \sin\theta
\end{equation}

and

\begin{equation}
\label{eqn:ics-cs-r}
r = \sqrt{x^2 + y^2},
\end{equation}

\begin{equation}
\label{eqn:ics-cs-theta}
\tan\theta = \frac{y}{x}.
\end{equation}

And for unit vectors

\begin{equation}
\label{eqn:ics-cs-unit-r}
\hat{r} = \cos\theta \ \hat{x} + \sin\theta \ \hat{y}
\end{equation}

\begin{equation}
\label{eqn:ics-cs-unit-theta}
\hat{\theta} = -\sin\theta \ \hat{x} + \cos\theta \ \hat{y}
\end{equation}

You can obtain Eqns. \eqref{eqn:ics-cs-unit-r} and \eqref{eqn:ics-cs-unit-theta} using 

\begin{equation}
\label{eqn:ics-cs-r-vector}
\vec{r} = r \hat{r}.
\end{equation}

and the concept of [unit vector](/math/unit-vector).


## cylindrical coordinate system
We can see that the cylindrical coordinate system as extension of polar coordinate system with additional $z$ components as shown in in Fig. <a href="#fig:ics-cs-polar-cylindrical">2</a>. This is similar as illustration in Fig. <a href="#fig:ics-cartesian-cartesian">1</a> that relates 2-d Cartesian coordinate system with its 3-d.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/cs/cs-polar-cylindrical.png)
<br />
Figure <a name="fig:ics-cs-polar-cylindrical">2</a> Polar coordinate system (left) and cylindrical coordinate system (righ).
{: refdef}

A position vector in this coordinate system (CS) is defined as

\begin{equation}
\label{eqn:ics-cs-cylindrical-position}
\vec{r} = r \hat{r} + z \hat{z}.
\end{equation}

Component along $\hat{\theta}$ direction does not exist in position vector. It will arise in velocity vector. Do you still remember angular velocity? It is actuallya velocity component in angular or $\hat{\theta}$ direction.

We can also relate the Cartesian CS with cylindrical cs, where they are illustrated in Fig. <a href="#fig:ics-cartesian-cylindrical">3</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/cs/cs-cartesian-cylindrical.png)
<br />
Figure <a name="fig:ics-cs-cartesian-cylindrical">2</a> Cartesian coordinate system (left) and cylindrical coordinate system (right).
{: refdef}

Then there are relations

\begin{equation}
\label{eqn:ics-cs-cyl-car-r}
r = \sqrt{x^2 + y^2},
\end{equation}

\begin{equation}
\label{eqn:ics-cs-cyl-car-theta}
\tan\theta = \frac{y}{x},
\end{equation}

\begin{equation}
\label{eqn:ics-cs-cyl-car-z}
z = z,
\end{equation}

\begin{equation}
\label{eqn:ics-cs-cyl-car-x}
x = r \cos\theta
\end{equation}

\begin{equation}
\label{eqn:ics-cs-cyl-car-y}
y = r \sin\theta.
\end{equation}

Since $z$ in Cartesian and cylindrical CSs are actually the same, the relations are similar between polar and Cartesian (2-d) coordinate systems.


## spherical coordinate system
..

{:refdef: style="text-align: center;"}
![..](/assets/img/math/cs/cs-cartesian-spherical.png)
<br />
Figure <a name="fig:ics-cs-cartesian-spherical">2</a> Cartesian coordinate system (upper left) and spherical coordinate system (upper right).
{: refdef}


## exercises
1. Prove Eqn. \eqref{eqn:ics-cs-unit-r} using Eqn. \eqref{eqn:ics-cs-r-vector}, and length of a vector by implementing concept of [unit vector](/math/unit-vector).
2. Do you have idea how to get Eqn. \eqref{eqn:ics-cs-unit-theta}? Explain in brief.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Polar coordinate system", Wikipedia, The Free Encyclopedia, 6 Jan 2021, 13:02 UTC, url <https://en.wikipedia.org/w/index.php?oldid=998664169> [20210208].
2. <a name="ref2"></a>Eric W. Weisstein, "Cylindrical Coordinates", from MathWorld--A Wolfram Web Resource, url  <https://mathworld.wolfram.com/CylindricalCoordinates.html> [20210209].
3. <a name="ref3"></a>Carl R. Nave, "Rectangular Coordinates", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/coord.html#c2> [20210209].
4. <a name="ref4"></a>Nykamp DQ, "Cartesian coordinates", from Math Insight, url <http://mathinsight.org/cartesian_coordinates> [20210209].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/math/2021-02-09-intro-coordinate-systems.md)



{% comment %}
Diandra
mengapa arc = r d\theta

KInan
luas da dr?

Jonathan
asumsi menghitung luas persegi panjang

084 Dyezahra -- batas R mengapa dari nol

Kinanti --> arah theta koordinat polar.

Dzakwanil batas theta 0 - pi dan 2pi

Siti -- JOanathan sama

0829-an problem. Video tersimpan tapi Zoom putus.
{% endcomment %}
