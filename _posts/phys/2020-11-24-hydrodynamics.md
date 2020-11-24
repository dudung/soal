---
layout: post
author: viridi
title: hydrodynamics
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["statics"]
date: 2020-11-24 09:28:00 +07
permalink: /physics/hydrodynamics
---
Hydrodynamics is part of fluid concept [[1](#ref1)], which describes the flow of fluids (liquids and gases) [[2](#ref2)].


## Continuity equation
In steady flow along a chanell with only one inlet and one outlet amount of fluid flowing passed every point must be the same or the mass flow rate is constant, which is essentially a statement of the law of coservation of mass. Then, the formula of continuity is [[3](#ref3)]

\begin{equation}
\label{eqn:hdyn-continuity}
\rho_i A_i v_i = \rho_j A_j v_j,
\end{equation}

where $i$ and $j$ indicates two different regions in the chanell. For incompressible fluid density of fluid is always the same in all region, which simplifies Eqn. \eqref{eqn:hdyn-continuity} into

\begin{equation}
\label{eqn:hdyn-continuity-incompressible}
A_i v_i = A_j v_j.
\end{equation}

We can also write Eqn. \eqref{eqn:hdyn-continuity-incompressible} in the form of

\begin{equation}
\label{eqn:hdyn-continuity-incompressible-Q}
Q_i = Q_j.
\end{equation}

using the [volumetric flow rate](volumetric-flow-rate) term.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/hydrodynamics/vfr-constant-cross-section.png)
<br />
Figure <a name="fig:hdyn-continuity">1</a> A channel with one inlet and outlet has three different regions $n = 1, 2, 3$.
{: refdef}

The three different regions in Fig. <a href="#fig:hdyn-continuity">1</a> will have the same volumetric flow rate $Q$ according to continuity equation in Eqn. \eqref{eqn:hdyn-continuity-incompressible-Q} or simply that $Q_1 = Q_2 = Q3$ as shown in the figure.


## Bernoulli principle
There is relation between speed of fluid flow $v$, static pressure $p$, and fluid's potential energy $U$ through Bernoulli's equation

\begin{equation}
\label{eqn:hdyn-bernoulli-equation}
p_i + \frac12 \rho v_i^2 + \rho g y_i = p_j + \frac12 \rho v_j^2 + \rho g y_j,
\end{equation}

where $i$ and $j$ are two different regions. Note that Eqn. \eqref{eqn:hdyn-bernoulli-equation} is the form for incompressible flow.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/hydrodynamics/bernoulli-principle.png)
<br />
Figure <a name="fig:hdyn-bernoulli">2</a> Regions 1 and 2 are related through Bernoulli equation.
{: refdef}

The indices $i$ and $j$ in Eqn. \eqref{eqn:hdyn-bernoulli-equation} are set to be $1$ and $2$ in Fig. <a href="#fig:hdyn-bernoulli">2</a>. Note that the reference for calculating fluid's potential energy using $y_1$ and $y_2$ should be the same.


## References
1. <a name="ref1"></a>Carl R. Nave, "Fluids", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/fluid.html> [20201124].
2. <a name="ref2"></a>Wikipedia contributors, "Fluid dynamics", Wikipedia, The Free Encyclopedia, 19 Nov 2020, 07:11 UTC, url <https://en.wikipedia.org/w/index.php?oldid=989485057> [20201124].
3. <a name="ref3"></a> Gayle Towell, "Continuity Equation (Fluids): Definition, Forms & Examples", Sciencing, 29 Jan 2020, url <https://sciencing.com/continuity-equation-fluids-definition-forms-examples-13723387.html> [20201124].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-11-24-hydrodynamics.md)

{% comment %}
Fig. <a href="#fig:x">1</a.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/x.png)
<br />
Figure <a name="fig:x">1</a> ...
{: refdef}
{% endcomment %}
