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
date: 2021-01-24 10:53:00 +07
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
+ $q_i < 0$ and $q_j < 0$ (both charges are negative), or
+ $q_i > 0$ and $q_j > 0$ (both charges are positive),

as shwon in Figure <a name="fig:cf-coulomb-force-repulsive">4</a>

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/coulomb-force-repulsive.png)
<br />
Figure <a name="fig:cf-coulomb-force-repulsive">4</a> repulsive Coulomb force of between two charges: all negative (left) and all positive (right).
{: refdef}

while direction of attractive force holds for the case of $q_i q_j < 0$ and it can be one of the two condition
+ $q_i < 0$ and $q_j > 0$ (negative and positive), or
+ $q_i > 0$ and $q_j < 0$ (positive and negative)

as shwon in Figure <a name="fig:cf-coulomb-force-attractive">5</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/coulomb-force-attractive.png)
<br />
Figure <a name="fig:cf-coulomb-force-attractive">5</a> Attractive Coulomb force between two charges: negative-positive (left) and positive-negative (right).
{: refdef}

From the both cases we can have that like charges repel each other, while unlike charges attract each other  [[3](#ref3)].


## 2-d and 1-d examples
Consider two charges are located in $xy$ plane as shown in Fig. <a href="#fig:cf-coulomb-force-1n2-d">6</a>, where they have the same or opposite signs.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/coulomb-force-1n2-d.png)
<br />
Figure <a name="fig:cf-coulomb-force-1nd-d">6</a> System of two charges: negative-positive (left), positive-positive (center), and negative-negative (right). 
{: refdef}

Coordinates of $x$ and $y$ in Fig. <a href="#fig:cf-coulomb-force-1nd-d">6</a> are in $\rm \mu m$ and $q_1 = +1 \ \rm nC$, $q_2 = -25 \ \rm nC$, $q_3 = +4 \ \rm nC$, $q_4 = +8 \ \rm nC$, $q_5 = -2 \ \rm nC$, $q_6 = -0.5 \ \rm nC$. To calculate the electrostatic force we use Eqns. \eqref{eqn:cf-coulomb's-law} - \eqref{eqn:cf-relative-position-unit-vector}.

### force on $q_2$ due to existence of $q_1$
$\vec{r}_2 = (\hat{x} + 2\hat{y}) \ \rm \mu m$. \
$\vec{r}_1 = (5\hat{x} + 5\hat{y})  \ \rm \mu m$. \
$\vec{r} _{21} = \vec{r}_2 - \vec{r}_1 = (1-5)\hat{x} + (2-5)\hat{y} = (-4\hat{x} - 3\hat{y}) \ \rm \mu m$. \
$r _{21} = \| \vec{r} _{21} \| = \sqrt{\vec{r} _{21} \cdot \vec{r} _{21}} = \sqrt{(-4\hat{x} - 3\hat{y}) \cdot (-4\hat{x} - 3\hat{y})} = \sqrt{(-4)^2 + (-3)^2} = 5  \ \rm \mu m$. \
$\displaystyle \hat{r} _{21} = \frac{\vec{r} _{21}}{r _{21}} = \frac{-4\hat{x} - 3\hat{y}}{5} = (-0.8\hat{x} - 0.6\hat{y})$. \
$\displaystyle \hat{F} _{21} = k \frac{q_2 q_1}{r^2 _{21}} \hat{r} _{21} = (9\times 10^9) \frac{(-25\times 10^{-9})(+1\times 10^{-9})}{(5\times 10^{-6})^2} (-0.8\hat{x} - 0.6\hat{y}) = (9\times 10^3)(0.8\hat{x} + 0.6\hat{y}) \ \rm N$.

### force on $q_3$ due to existence of $q_4$
$\vec{r}_3 = (6\hat{x} + 2\hat{y}) \ \rm \mu m$. \
$\vec{r}_4 = (6\hat{x} + 10\hat{y})  \ \rm \mu m$. \
$\vec{r} _{34} = \vec{r}_3 - \vec{r}_4 = (6-6)\hat{x} + (2-10)\hat{y} = (-8\hat{y}) \ \rm \mu m$. \
$r _{34} = \| \vec{r} _{34} \| = \sqrt{\vec{r} _{34} \cdot \vec{r} _{34}} = \sqrt{(-8\hat{y}) \cdot (-8\hat{y})} = \sqrt{(-8)^2} = 8  \ \rm \mu m$. \
$\displaystyle \hat{r} _{34} = \frac{\vec{r} _{34}}{r _{34}} = \frac{-8\hat{y}}{8} = (-\hat{y})$. \
$\displaystyle \hat{F} _{34} = k \frac{q_3 q_4}{r^2 _{34}} \hat{r} _{34} = (9\times 10^9) \frac{(+4\times 10^{-9})(+8\times 10^{-9})}{(8\times 10^{-6})^2} (-\hat{y}) = (4.5\times 10^3)(-\hat{y}) \ \rm N$.

### force on $q_5$ due to existence of $q_6$
$\vec{r}_5 = (0.5\hat{x} + 2\hat{y}) \ \rm \mu m$. \
$\vec{r}_6 = (2.5\hat{x} + 2\hat{y})  \ \rm \mu m$. \
$\vec{r} _{56} = \vec{r}_5 - \vec{r}_6 = (0.5-2.5)\hat{x} + (2-2)\hat{y} = (-2\hat{x}) \ \rm \mu m$. \
$r _{56} = \| \vec{r} _{56} \| = \sqrt{\vec{r} _{56} \cdot \vec{r} _{56}} = \sqrt{(-2\hat{x}) \cdot (-2\hat{x})} = \sqrt{(-2)} = 2  \ \rm \mu m$. \
$\displaystyle \hat{r} _{56} = \frac{\vec{r} _{56}}{r _{56}} = \frac{-2\hat{x}}{2} = (-\hat{x})$. \
$\displaystyle \hat{F} _{56} = k \frac{q_5 q_6}{r^2 _{56}} \hat{r} _{56} = (9\times 10^9) \frac{(-2\times 10^{-9})(-0.5\times 10^{-9})}{(2\times 10^{-6})^2} (-\hat{x}) = (2.25\times 10^3)(-\hat{x}) \ \rm N$.


## 1-d, 2-d, and 3-d examples
Fig. <a href="#fig:cf-coulomb-force-2-charges-123-d">7</a> shows examples of 1-d, 2-d, and 3-d configuration of two charges. The difference than previous Fig. <a href="#fig:cf-coulomb-force-1n2-d">6</a> is that the position of one of the two charges might has additional $z$ component.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/coulomb-force-2-charges-123-d.png)
<br />
Figure <a name="fig:cf-coulomb-force-2-charges-123-d">7</a> System of two charges: 1-d positive-negative (left), 2-d positive-positive (center), and 3-d negative-negative (right). 
{: refdef}

Position of the charges are given as follow.

**charge** | $q_1 > 0$ | $q_2 < 0$ | $q_3 > 0$ | $q_4 < 0$   
**position** | $\vec{r}_1 = s_x \hat{x}$ | $\vec{r}_2 = s_x \hat{x} + s_y \hat{y}$ | $\vec{r}_3 = s_y \hat{y}$ | $\vec{r}_4 = s_z \hat{z}$

Using the provided information we can obtain values of $\vec{r} _{12}$, $\vec{r} _{13}$, and $\vec{r} _{24}$ in order to calculate $\vec{F} _{12}$, $\vec{F} _{13}$, and $\vec{F} _{24}$. Do it in the exercises 7-9.


## exercises
1. What is the definition of $\vec{F} _{ji}$? Modify the related sentence in the Coulomb's law section.
2. Write the first two sides from the left of Eqn. \eqref{eqn:cf-coulomb's-law} and try to get the right side of it using Eqn. \eqref{eqn:cf-relative-position-unit-vector}.
3. Open [[3](#ref3)] and find the four properties of the electric force for charges at rest. Explain it in brief whether those properties are already contained in the Eqn. \eqref{eqn:cf-coulomb's-law} or not.
4. Using the previous 2-d and 1-d examples in Fig. <a href="#fig:cf-coulomb-force-1nd-d">6</a>, caculate $\vec{F} _{12}$.
5. Repeat using Fig. <a href="#fig:cf-coulomb-force-1nd-d">6</a> to caculate $\vec{F} _{43}$.
6. Caculate $\vec{F} _{65}$ using Fig. <a href="#fig:cf-coulomb-force-1nd-d">6</a>.
7. If $s_x = s_y = s_z = 2 \ \rm \mu m$, $q_1 = +2 \ \rm nC$, and $q_2 = -1 \ \rm nC$, calculate $\vec{F} _{12}$ using Fig. <a href="#fig:cf-coulomb-force-2-charges-123-d">7</a>.
8. If $s_x = s_y = s_z = 2 \ \rm \mu m$, $q_1 = +2 \ \rm nC$, and $q_3 = +\sqrt{2} \ \rm nC$, calculate $\vec{F} _{13}$ using Fig. <a href="#fig:cf-coulomb-force-2-charges-123-d">7</a>.
9. If $s_x = s_y = s_z = 2 \ \rm \mu m$, $q_2 = -1 \ \rm nC$,
and $q_4 = -\sqrt{3} \ \rm nC$, calculate $\vec{F} _{24}$ using Fig. <a href="#fig:cf-coulomb-force-2-charges-123-d">7</a>.
10. Draw you own 2-d configuration and calculate electrostatic force on a charge due to existence of the other charge.


## references
1. <a name="ref1"></a>Carl R. Nave, "Coulomb's Law", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/electric/elefor.html> [20210123].
2. <a name="ref2"></a>Wikipedia-Autoren, "Coulombsches Gesetz", Wikipedia, Die freie Enzyklopädie, 29 Sep 2020, 08:15 UTC, url <https://en.wikipedia.org/w/index.php?oldid=204085948> [20210123].
3. <a name="ref3"></a>The Editors of Encyclopaedia Britannica, William L. Hosch, Parul Jain, Thinley Kalsang, Bhutia, Adam Augustyn, "Coulomb's law", Encyclopaedia Britannica, 11 Jan 2019, url <https://www.britannica.com/science/Coulombs-law> [20210123].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/electrostatics/2021-01-11-coulomb-force.md)
