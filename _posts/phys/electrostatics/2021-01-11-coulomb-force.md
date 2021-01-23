---
layout: post
author: viridi
title: coulomb force
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["", "", "", ""]
date: 2021-01-11 21:01:00 +07
permalink: /electrostatics/coulomb-force
---
When there are two charges in space, they will interact through electrostatic force formulated by Coulomb's law [[1](#ref1)]. In the case of attractive force between two point charges Coulomb force does behave like the gravitational force between two point masses [[2](#ref2)].


## coulomb's law
Suppose that there are two charges $q_i$ and $q_j$ in space, where each is located at position $\vec{r}_i$ and $\vec{r}_j$, respectively, as shown in Fig. <a href="#fig:cf-coulomb-force">1</a>. We use the definition that $\vec{F} _{ij}$ is an electrostatic force acted upon charge $q_i$ due to the presence of charge $q_j$ and vice versa.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/coulomb-force.png)
<br />
Figure <a name="fig:cf-coulomb-force">1</a> Coulomb force between two charges $q_i$ and $q_j$.
{: refdef}

In vector form Coulomb's law is

\begin{equation}
\label{eqn:cf-coulomb's-law}
\vec{F} _{ij} = k \frac{q_i q_j}{r _{ij}^2} \ \hat{r} _{ij} = k \frac{q_i q_j}{r _{ij}^3} \ \vec{r} _{ij}
\end{equation}

with

\begin{equation}
\label{eqn:cf-coulomb's-constant}
k = \frac{1}{4 \pi \epsilon_0} \approx 9 \times 10^9 \ {\rm N \cdot m^2 / C^2}
\end{equation}

is Coulomb's constant.


## detail use
Notation of $\vec{r} _{ij}$ in Eqn. \eqref{eqn:cf-coulomb's-law} stands for [relative position](/physics/position#relative-position) of charge $q_i$ relative to charge $q_j$

\begin{equation}
\label{eqn:cf-relative-position}
\vec{r} _{ij} = \vec{r}_i - \vec{r}_j.
\end{equation}

And the [distance](/physics/position#distance) between two charges is

\begin{equation}
\label{eqn:cf-distance-two-charges}
r_{ij} = \| \vec{r} _{ij} \| =  \sqrt{\vec{r} _{ij} \cdot \vec{r} _{ij}}.
\end{equation}

Unit vector $\hat{r} _{ij}$ is related to relative positiion $\vec{r} {ij}$ and distance $r _{ij}$ through

\begin{equation}
\label{eqn:cf-relative-position-unit-vector}
\hat{r} _{ij} = \frac{\vec{r} _{ij}}{r _{ij}}.
\end{equation}

Eqn. \eqref{eqn:cf-relative-position-unit-vector} explains the relation between middle site and right side of Eqn. \eqref{eqn:cf-coulomb's-law}.


## case of $q_i q_j > 0$
Let us simplify the illustration in previous Fig. <a href="#fig:cf-coulomb-force">1</a> with two-dimensional projection as shown in Fig. <a href="#fig:cf-coulomb-force-1">2</a> for the case of $q_i q_j > 0$. We will concentrate on $q_i$ firs, since it will be the same for $q_j$.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/coulomb-force-qiqj-gt0.png)
<br />
Figure <a name="fig:cf-coulomb-force-1">2</a> Coulomb force on $q_i$ due to existence of $q_j$ for $q_i q_j > 0$.
{: refdef}

From Fig. <a href="#fig:cf-coulomb-force-1">2</a> we can have relative position of charge $q_i$ to charge $q_j$, which is denoted as $\vec{r} _{ij}$ as given previously in Eqn. \eqref{eqn:cf-relative-position}. Then using Eqn. \eqref{eqn:cf-distance-two-charges}, which is always positive since it is length of a vector, and Eqn. \eqref{eqn:cf-relative-position-unit-vector} we can have the unit vector $\hat{r} _{ij}$ to be used in Eqn. \eqref{eqn:cf-coulomb's-law}. Vector $\vec{r} _{ij}$, scalar $r _{ij}$, and vector $\hat{r} _{ij}$ are shown in Fig. <a href="#fig:cf-coulomb-force-1">2</a> (center). And the last term direction is toward charge $q_i$ from charge $q_j$. Combining all terms in Eqn. \eqref{eqn:cf-coulomb's-law} we can have that what determines direction of $\vec{F} _{ij}$ is the term $q_i q_j$ since $r _ij$ and $k$ are already positive. For this case $q_i q_j > 0$ then $\vec{F} _{ij}$ will have the same direction with $\hat{F} _{ij}$ or the force on $q_i$ will have direction away from $q_j$ (and also vice versa), which is showing a repulsive force.


## case of $q_i q_j < 0$
Now we consider the case of $q_i q_j < 0$ as given in Fig. <a href="#fig:cf-coulomb-force-2">3</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/coulomb-force-qiqj-lt0.png)
<br />
Figure <a name="fig:cf-coulomb-force-2">3</a> Coulomb force on $q_i$ due to existence of $q_j$ for $q_i q_j < 0$.
{: refdef}

Similar to the previous discussion direction of $\vec{F} _{ij}$ will be determined by value of $q_i q_j$ which is negative in this case. Then $\vec{F} _{ij}$ will have an opposite direction compated to $\hat{r} _{ij}$ direction, which is shown as red arrow in Fig. <a href="#fig:cf-coulomb-force-2">3</a> (right). This is a direction of an attractive force.


## the two cases
Direction of repulsive force holds for the case of $q_i q_j > 0$ and it can be one of the two condition
+ $q_i > 0$ and $q_j > 0$ (both charges are positive), or
+ $q_i < 0$ and $q_j < 0$ (both charges are negative),

while direction of attractive force holds for the case of $q_i q_j < 0$ and it can be one of the two condition
+ $q_i < 0$ and $q_j > 0$ (negative and positive), or
+ $q_i > 0$ and $q_j < 0$ (positive and negative).


## exercises
1. What is the definition of $\vec{F} _{ji}$? Modify the related sentence in the Coulomb's law section.
2. Write the first two sides from the left of Eqn. \eqref{eqn:cf-coulomb's-law} and try to get the right side of it using Eqn. \eqref{eqn:cf-relative-position-unit-vector}.


## references
1. <a name="ref1"></a>Carl R. Nave, "Coulomb's Law", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/electric/elefor.html> [20210123].
2. <a name="ref2"></a>Wikipedia-Autoren, "Coulombsches Gesetz", Wikipedia, Die freie Enzyklopädie, 29 Sep 2020, 08:15 UTC, url <https://en.wikipedia.org/w/index.php?oldid=204085948> [20210123].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/electrostatics/2021-01-11-coulomb-force.md)
