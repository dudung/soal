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

Using Eqn. \eqref{eqn:eflicf-electric-field-charge-distribution} and Fig. <a href="#fig:eflicf-electric-field-charge-distribution-front">2</a> we can have \
$\vec{r} - \vec{r}_j = [(b+l) - x] \hat{x}$. \
$\|\vec{r} - \vec{r}_j \| = \|(b+l) - x\|$. \
$\displaystyle \frac{\vec{r} - \vec{r}_j}{\|\vec{r} - \vec{r}_j \|} = \hat{x}$. \
$\|\vec{r} - \vec{r}_j \|^2 =[(b+l) - x]^2 = (b+l-x)^2$. \
$b - a = L$ or $b = a + L$.

And from Eqns. \eqref{eqn:eflicf-line-charge-density} and \eqref{eqn:eflicf-line-charge-density-qj} \
$dq_j = \lambda \ dx$. \
$q_j = \lambda L$.

Then using previous equations \
$\displaystyle d\vec{E}_j = k \ \frac{dq_j}{\|\vec{r} - \vec{r}_j \|^2} \ \frac{\vec{r} - \vec{r}_j}{\|\vec{r} - \vec{r}_j \|} = k \ \frac{\lambda dx}{(b+l-x)^2} \ \hat{x}$ \
$\displaystyle \vec{E}_j = \hat{x} k \lambda \int_a^b \frac{dx}{(b+l-x)^2}$.

From [list of integrals 0](/math/list-of-integrals-0#in-front-line-of-charge) we can have the solution \
$\displaystyle \vec{E}_j = \hat{x} k \lambda \frac{L}{l(L+l)} = k \ \frac{\lambda L}{l(L+l)} \ \hat{x} = k \ \frac{q_j}{l(L+l)} \ \hat{x}$.

If we set $l >> L$ then $L + l \approx l$ \
$\displaystyle \vec{E}_j \approx k \ \frac{q_j}{l^2} \ \hat{x}$, \
which gives an electric field of a point charge. From far away a finite line of charge will be seen as a point charge.


## at back of the other end of the line
What is the electric field of similar system shown in Fig. <a href="#fig:eflicf-electric-field-charge-distribution-back">2</a>? Do we need to calculate that? The result should be $\displaystyle \vec{E}_j = k \ \frac{q_j}{l(L+l)} \ (-\hat{x})$.
And we are going to show that.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/line/straight-line-charge-back.png)
<br />
Figure <a name="fig:eflicf-electric-field-charge-distribution-back">2</a> Electric field in front of line of charge (top) and contribution of differential charge element $dq_j$ to element of electric field $d\vec{E}_j$.
{: refdef}

Using Eqn. \eqref{eqn:eflicf-electric-field-charge-distribution} and Fig. <a href="#fig:eflicf-electric-field-charge-distribution-back">2</a> we can have \
$\vec{r} - \vec{r}_j = [(a-l) - x] \hat{x} = [x - (a-l)] (-\hat{x})$. $\leftarrow$ the form of (magnitude) (direction) \
$\|\vec{r} - \vec{r}_j \| = \|x - (a-l)\|$. \
$\displaystyle \frac{\vec{r} - \vec{r}_j}{\|\vec{r} - \vec{r}_j \|} = (-\hat{x})$. \
$\|\vec{r} - \vec{r}_j \|^2 =[(a-l) - x]^2 = (a-l-x)^2$. \
$b - a = L$ or $b = a + L$.

And from Eqns. \eqref{eqn:eflicf-line-charge-density} and \eqref{eqn:eflicf-line-charge-density-qj} \
$dq_j = \lambda \ dx$. \
$q_j = \lambda L$.

Then using previous equations \
$\displaystyle d\vec{E}_j = k \ \frac{dq_j}{\|\vec{r} - \vec{r}_j \|^2} \ \frac{\vec{r} - \vec{r}_j}{\|\vec{r} - \vec{r}_j \|} = k \ \frac{\lambda dx}{(a-l-x)^2} \ (-\hat{x})$ \
$\displaystyle \vec{E}_j = (-\hat{x}) k \lambda \int_a^b \frac{dx}{(a-l-x)^2}$.

From [list of integrals 0](/math/list-of-integrals-0#at-back-of-line-of-charge) we can have the solution \
$\displaystyle \vec{E}_j = (-\hat{x}) k \lambda \frac{L}{l(L+l)} = k \ \frac{\lambda L}{l(L+l)} \ (-\hat{x}) = k \ \frac{q_j}{l(L+l)} \ (-\hat{x})$, \
as predicted.


## along $x$, $y$, and $z$ directions
Along $x$ direction there were in front and at back of the line. There are also similar cases along $y$ dan $z$ direction. Fig. <a href="#fig:straight-line-charge-both-ends">3</a> show the six possible cases. Notice that the axis orientation is different in each row. 

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/line/straight-line-charge-both-ends.png)
<br />
Figure <a name="fig:straight-line-charge-both-ends">3</a> Electric field at both end of line of charge, which can be along $x$ axis (top), along $y$ axis (middle), and along $z$ axis (bottom).
{: refdef}

Electric field in Fig. <a href="#fig:straight-line-charge-both-ends">3</a> can be summerized as follow

**along axis of** | **negative end** | **positive end**
$x$ | $\displaystyle \vec{E}_{1-} = k \ \frac{\lambda_1 L_1}{(L_1 + l _{1-}) l _{1-}} \ (-\hat{x})$ | $\displaystyle \vec{E}_{1+} = k \ \frac{\lambda_1 L_1}{(L_1 + l _{1+}) l _{1+}} \ (+\hat{x})$
$y$ | $\displaystyle \vec{E}_{2-} = k \ \frac{\lambda_2 L_2}{(L_2 + l _{2-}) l _{2-}} \ (-\hat{y})$ | $\displaystyle \vec{E}_{2+} = k \ \frac{\lambda_2 L_2}{(L_2 + l _{2+}) l _{2+}} \ (+\hat{y})$
$z$ | $\displaystyle \vec{E}_{3-} = k \ \frac{\lambda_3 L_3}{(L_3 + l _{3-}) l _{3-}} \ (-\hat{z})$ | $\displaystyle \vec{E}_{3+} = k \ \frac{\lambda_3 L_3}{(L_3 + l _{3+}) l _{3+}} \ (+\hat{z})$

where the patterns are so clear to notice.


## superposition
Suppose that there are three line of charge in along each axis as given in following Fig. <a href="#fig:straight-line-charges-3-axes">4</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/line/straight-line-charges-3-axes.png)
<br />
Figure <a name="fig:straight-line-charges-3-axes">4</a> .
{: refdef}


## references
1. <a name="ref1"></a>Carl R. Nave, "Electric Field of Line Charge", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/electric/elelin.html> [20210125].
2. <a name="ref2"></a>Wikipedia contributors, "Charge density", Wikipedia, The Free Encyclopedia, 13 Jan 2021, 01:41 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1000006708#Homogeneous_charge_density> [20210125].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/electrostatics/2021-01-25-electric-field-line-charge-front.md)
