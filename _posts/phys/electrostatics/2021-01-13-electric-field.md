---
layout: post
author: viridi
title: electric field
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["", "", "", ""]
date: 2021-01-24 11:40:00 +07
permalink: /electrostatics/electric-field
---
When charge, in any form, is present there will be an electric property associated with each point in space, where this property is known as electric field [[1](#ref1)], which is important in many areas of physics [[2](#ref2)]. Electric field can also be viewed as the region around the electric charge in which the stress or electric force act [[3](#ref3)].


## definition
Electric field is defined as the electric force per unit charge [[4](#ref4)], where at a location it indicates the force that would act on a unit positive test charge if placed at that location [[5](#ref5)]. It can be formulated as

\begin{equation}
\label{eqn:ef-electric-field}
\vec{E} = \frac{\vec{F}}{q_0}, 
\end{equation}

with $q_0$ is the unit positive test charge. When we review again [Coulomb force](/electrostatics/coulomb-force) on charge $q_i$ due to existence of charge $q_j$

\begin{equation}
\label{eqn:ef-coulomb's-law}
\vec{F} _{ij} = k \frac{q_i q_j}{r _{ij}^2} \ \hat{r} _{ij},
\end{equation}

and set the the unit positive test charge as $q_i$ then we have

\begin{equation}
\label{eqn:ef-coulomb's-law-electric-field}
\vec{E}_j = \frac{\vec{F} _{ij}}{q_i} = k \frac{q_j}{r _{ij}^2} \ \hat{r} _{ij} \equiv \vec{E}_j(\vec{r}_i),
\end{equation}

where the last term means "due to charge $q_j$ located at $\vec{r}_j$ there will be electric field observed at position $\vec{r}_i$".


## electric field due to point charge

By changing $\vec{r}_i$ to more general position $\vec{r}$ and using the [relative position](/physics/position#relative-position) we can write

\begin{equation}
\label{eqn:ef-electric-field-point-charge}
\vec{E}_j(\vec{r}) = k \frac{q_j}{\| \vec{r} - \vec{r}_j \|^3} \ (\vec{r} - \vec{r}_j),
\end{equation}

which is electric field at arbitraty position $\vec{r}$ due to existence of charge $q_j$ located at $\vec{r}_j$.



## references
1. <a name="ref1"></a>The Editors of Encyclopaedia Britannica, Adam Augustyn, Erik Gregersen, Thinley Kalsang Bhutia, Deepti Mahajan, Dutta Promeet, "Electric field", Encyclopædia Britannica, 7 Jan 2019, url <https://www.britannica.com/science/electric-field> [20210113].
2. <a name="ref2"></a>Wikipedia contributors, "Electric field", Wikipedia, The Free Encyclopedia, 15 Dec 2020, 05:55 UTC, url <https://en.wikipedia.org/w/index.php?oldid=994341755> [20210113].
3. <a name="ref3"></a>-, "Electric Field", Circuit globe, url <https://circuitglobe.com/electric-field.html> [20210113].
4. <a name="ref4"></a>Carl R. Nave, "Electric Field", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/electric/elefie.html> [20210113].
5. <a name="ref5"></a>Willy McAllister, "Electric field", Khan Academy, url <https://www.khanacademy.org/science/electrical-engineering/ee-electrostatics/ee-electric-force-and-electric-field/a/ee-electric-field> [20210113].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/electrostatics/2021-01-13-electric-field.md)

{% comment %}
Fig. <a href="#fig:x">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/x.png)
<br />
Figure <a name="fig:x">1</a> ...
{: refdef}
{% endcomment %}
