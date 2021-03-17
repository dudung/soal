---
layout: post
author: viridi
title: volumetric flow rate
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["flow rate", "debit"]
date: 2020-11-19 06:53:00 +07
permalink: /physics/volumetric-flow-rate
---
Volume of fluid which passes per unit time is known as volumetric flow rate (or volume flow rate, rate of fluid flow, volume velocity) with the symbol of $Q$ (or $\dot{V}$) [[1](#ref1)] or $\mathcal{F}$ which can also be generally expressed using effective velocity [[2](#ref2)].


## Definition
One of the definition of volume flow rate is

\begin{equation}
\label{eqn:volumetric-flow-rate-plane}
Q = \vec{v} \cdot \vec{A}
\end{equation}

vhere $\vec{v}$ is flow velocity and $\vec{A}$ is cross-sectional vector surface / area. Eqn. \eqref{eqn:volumetric-flow-rate-plane} holds for planar velocity profile. For general velocity profile

\begin{equation}
\label{eqn:volumetric-flow-rate-plane-integral}
Q = \int \vec{v} \cdot d\vec{A}
\end{equation}

is used, where $\vec{v} = \vec{v}(\vec{A})$ and $\vec{A} = \vec{A}(\vec{s})$ with $vec{s}$ is a coordinate along the flow direction.


## Illustration



## References
1. <a name="ref1"></a>Wikipedia contributors, "Volumetric flow rate", Wikipedia, The Free Encyclopedia, 20 Sep 2020, 07:49 UTC, url <https://en.wikipedia.org/w/index.php?oldid=979349383> [20201119].
2. <a name="ref2"></a>Carl R. Nave, "Effective Fluid Speed in a Tube", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/pfric.html#veff> [20201119].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-11-19-volumetric-flow-rate.md)

{% comment %}
Fig. <a href="#fig:x">1</a.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/x.png)
<br />
Figure <a name="fig:x">1</a> ...
{: refdef}
{% endcomment %}
