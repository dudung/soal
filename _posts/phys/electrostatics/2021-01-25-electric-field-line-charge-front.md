---
layout: post
author: viridi
title: electric field line charge front
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["", "", "", ""]
date: 2021-01-25 11:51:00 +07
permalink: /electrostatics/electric-field-line-charge-front
---
Due to line of charge in the form of a straight line, electric field in front of the line can be calculated using electric field formulation due to charge distribution. It is not the same as when the observation point is on the side of the line [[1](#ref1)].


## line charge density
In system that can be considered as one-dimensional system since the other two dimensions are negligible compared to the first, we hava line charge density $\lambda$

\begin{equation}
\label{eqn:eflicf-line-charge-density}
\lambda = \frac{dq_j}{dl},
\end{equation}

where $dl$ is element of length, that can be $dx$, $dy$, $dz$, $rd\theta$, etc. Total charge of the system is simply

\begin{equation}
\label{eqn:eflicf-line-charge-density-qj}
q_j = \int dq_j = \int \lambda dl,
\end{equation}

where in general $\lambda = \lambda(l)$. If $\lambda \ne \lambda(l)$ then then $\lambda$ has constant value and the material is homogeneous [[2](#ref2)], which turns Eqn. \eqref{eqn:eflicf-line-charge-density-qj} into

\begin{equation}
\label{eqn:eflicf-line-charge-density-qj-homogeneous}
q_j = \lambda \int dl = \lambda l.
\end{equation}

### example
A line of charge, lies along $x$ axis from $x = a$ to $x = a + L$, has a homogenous charge density $\lambda = c_0$. Find length of the line of charge and its total charge $q_j$. If total charge of the system is $+Q$ find value of $c_0$.

$\displaystyle l = \int dl = \int_{x = a}^{a + L} dx = [x]_{x = a}^{a + L} = [(a + L) - a] = L$.

$\displaystyle q_j = \int dq_j = \int \lambda dl = \int_{x = a}^{a + L} c_0 dx = c_0 \int_{x = a}^{a + L} dx = c_0 L$.

$\displaystyle c_0 = \frac{q_j}{L} = \frac{+Q}{L}$.

$\displaystyle \lambda = \frac{+Q}{L}$.


## electric field due to charge distribution
A group of charges can assemble a charge distribution $dq_j$ as shown in Fig. <a href="#fig:eflicf-electric-field-charge-distribution">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/electric-field-charge-distribution.png)
<br />
Figure <a name="fig:eflicf-electric-field-charge-distribution">1</a> Element of charge distribution $q_j$ produces element of electric field $d\vec{E}_j$.
{: refdef}

The element of electric field $d\vec{E}_j$, due to differential element of charge distribution $dq_j$ shown in Fig. <a ref="#fig:eflicf-electric-field-charge-distribution">1</a>, is formulated as

\begin{equation}
\label{eqn:eflicf-electric-field-charge-distribution}
d\vec{E}_j(\vec{r}) = k \frac{dq_j}{\| \vec{r} - \vec{r}_j \|^3} \ (\vec{r} - \vec{r}_j),
\end{equation}

and integration will produce the electric field

\begin{equation}
\label{eqn:eflicf-electric-field-charge-distribution-int}
\vec{E}_j(\vec{r}) = \int d\vec{E}_j(\vec{r}),
\end{equation}

where $dq_j$ is given previouly in Eqn. \eqref{eqn:eflicf-line-charge-density}.


## in front of line of charge
For this case more specific illustration than the general in Fig. <a href="#fig:eflicf-electric-field-charge-distribution">1</a> is required and it will be given in following Fig. <a href="#fig:eflicf-electric-field-charge-distribution-front">2</a>. Top part of the figure shows the system where we want to obtain the electric charge due to line of charge where the observation point $o$ is located at a distance $l$ in front of the line.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/line/straight-line-charge-front.png)
<br />
Figure <a name="fig:eflicf-electric-field-charge-distribution-front">1</a> Electric field in front of line of charge (top) and contribution of differential charge element $dq_j$ to element of electric field $d\vec{E}_j$.
{: refdef}

Using Eqn. \eqref{eqn:eflicf-electric-field-charge-distribution} and Fig. <a href="#fig:eflicf-electric-field-charge-distribution-front">2</a> we can have

$\vec{r} - \vec{r}_j = [(b+l) - x] \hat{x}$. \
$\|\vec{r} - \vec{r}_j \| = \|(b+l) - x\|$. \
$\displaystyle \frac{\vec{r} - \vec{r}_j}{\|\vec{r} - \vec{r}_j \|} = \hat{x}$.
$\|\vec{r} - \vec{r}_j \|^2 =[(b+l) - x]^2$.


## references
1. <a name="ref1"></a>Carl R. Nave, "Electric Field of Line Charge", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/electric/elelin.html> [20210125].
2. <a name="ref2"></a>Wikipedia contributors, "Charge density", Wikipedia, The Free Encyclopedia, 13 Jan 2021, 01:41 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1000006708#Homogeneous_charge_density> [20210125].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/electrostatics/2021-01-25-electric-field-line-charge-front.md)
