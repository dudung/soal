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

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/electric-field-from-force-point-charge.png)
<br />
Figure <a name="fig:ef-electric-field-from-force-point-charge">1</a> Electric field $\vec{E}_j$ from a point charge: $q_j < 0$ (left) and $q_j > 0$ (right).
{: refdef}

Illustration to obtain electric field from a point charge $q_j$, where it can negative or positive, is given in Fig. <a ref="#fig:ef-electric-field-from-force-point-charge">1</a>. Implicitly source charge $q_j$ and unit positive test charge $q_i$ are located at $\vec{r}_j$ and $\vec{r}_i$, respectively.


## electric field due to point charge
By changing $\vec{r}_i$ to more general position $\vec{r}$ and using the [relative position](/physics/position#relative-position) we can write

\begin{equation}
\label{eqn:ef-electric-field-point-charge}
\vec{E}_j(\vec{r}) = k \frac{q_j}{\| \vec{r} - \vec{r}_j \|^3} \ (\vec{r} - \vec{r}_j),
\end{equation}

which is electric field at arbitraty position $\vec{r}$ due to existence of charge $q_j$ located at $\vec{r}_j$. Illustration of Eqn. \eqref{eqn:ef-electric-field-point-charge} is given in Fig. <a ref="#fig:ef-electric-field-point-charge">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/electric-field-point-charge.png)
<br />
Figure <a name="fig:ef-electric-field-point-charge">2</a> Electric field $\vec{E}_j$ due to a point charge $q_j$.
{: refdef}

We can see from Fig. <a ref="#fig:ef-electric-field-point-charge">2</a> that what matter related to position is only relative position of observation point $\vec{r}$ to the position of source charge $q_j$ located at $\vec{r}_j$ or simply $\vec{r} - \vec{r}_j$.


## electric field due to charge distribution
In real world it is difficult to have a point charge, but group of charges that can assemble a charge distribution $dq_j$, which illustation is given in Fig. <a ref="#fig:ef-electric-field-charge-distribution">3</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/electric-field-charge-distribution.png)
<br />
Figure <a name="fig:ef-electric-field-charge-distribution">3</a> Element of electric field $d\vec{E}_j$ due to element of charge distribution $q_j$.
{: refdef}

Instead of electric field $\vec{E}_j$ as in Eqn. \eqref{eqn:ef-electric-field-point-charge}, Fig. <a ref="#fig:ef-electric-field-charge-distribution">3</a> gives the element of electric field $d\vec{E}_j$ due to element of charge distribution $q_j$, which is formulated as

\begin{equation}
\label{eqn:ef-electric-field-charge-distribution}
d\vec{E}_j(\vec{r}) = k \frac{dq_j}{\| \vec{r} - \vec{r}_j \|^3} \ (\vec{r} - \vec{r}_j),
\end{equation}

and to get the electric field field from Eqn. \eqref{eqn:ef-electric-field-charge-distribution}

\begin{equation}
\label{eqn:ef-electric-field-charge-distribution-int}
\vec{E}_j(\vec{r}) = \int d\vec{E}_j(\vec{r}),
\end{equation}

simply do the integration.


## charge distribution
Element of charge distribution $dq_j$ in Eqn. \eqref{eqn:ef-electric-field-charge-distribution} can be in the form of


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
