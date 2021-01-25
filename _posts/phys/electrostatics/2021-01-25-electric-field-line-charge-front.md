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


## references
1. <a name="ref1"></a>Carl R. Nave, "Electric Field of Line Charge", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/electric/elelin.html> [20210125].

{% comment %}
.


## electric field due to charge distribution
In real world it is difficult to have a point charge, but group of charges that can assemble a charge distribution $dq_j$, which illustation is given in Fig. <a ref="#fig:ef-electric-field-charge-distribution">5</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/electric-field-charge-distribution.png)
<br />
Figure <a name="fig:ef-electric-field-charge-distribution">5</a> Element of electric field $d\vec{E}_j$ due to element of charge distribution $q_j$.
{: refdef}

Instead of electric field $\vec{E}_j$ as in Eqn. \eqref{eqn:ef-electric-field-point-charge}, Fig. <a ref="#fig:ef-electric-field-charge-distribution">5</a> gives the element of electric field $d\vec{E}_j$ due to element of charge distribution $q_j$, which is formulated as

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
Element of charge distribution $dq_j$ in Eqn. \eqref{eqn:ef-electric-field-charge-distribution} can be in the form of line charge density $\lambda$, surface charge density $\sigma$, or volume charge density $\rho$ through

\begin{equation}
\label{eqn:ef-charge-distribution-line}
dq_j = \lambda dl,
\end{equation}

where $dl$ can be $dx$, $dy$, $dz$, $dr$, $rd\theta$, etc, 

\begin{equation}
\label{eqn:ef-charge-distribution-surface}
dq_j = \sigma dA,
\end{equation}

where $dA$ can be $(dx)(dy)$, $(dy)(dz)$, $(dx)(dz)$, $(dr)(dz)$, $(dr)(rd\theta)$, etc,

\begin{equation}
\label{eqn:ef-charge-distribution-volume}
dq_j = \rho dV,
\end{equation}

where $dV$ can be $(dx)(dy)(dz)$, $(dr)(rd\theta)(r\sin\theta d\phi)$, etc.

In general $\lambda$, $\sigma$, and $\rho$ are not constant and depend on coordinates. In case of constant the materials are homogeneous and isotropic [[8](#ref8)].


## exercises
1. At position $\vec{r}_j = (10\hat{x} + 10\hat{y} + 4\hat{z}) \ \rm \mu m$ there is a point charge $q_j = 25 \ \rm nC$. Find the electric field at position $\vec{r} = (6\hat{x} + 13\hat{y} + 4\hat{z}) \ \rm \mu m$. What is the magnitude and unit vector of the electric field?
2. At position $\vec{r}_j = (2\hat{x} + 6\hat{y} + 14\hat{z}) \ \rm \mu m$ there is a point charge $q_j = 20 \ \rm nC$. Find the electric field at position $\vec{r} = (10\hat{x} + 6\hat{y} + 8\hat{z}) \ \rm \mu m$. What is the magnitude and unit vector of the electric field?


## references
1. <a name="ref1"></a>The Editors of Encyclopaedia Britannica, Adam Augustyn, Erik Gregersen, Thinley Kalsang Bhutia, Deepti Mahajan, Dutta Promeet, "Electric field", Encyclopædia Britannica, 7 Jan 2019, url <https://www.britannica.com/science/electric-field> [20210113].
2. <a name="ref2"></a>Wikipedia contributors, "Electric field", Wikipedia, The Free Encyclopedia, 15 Dec 2020, 05:55 UTC, url <https://en.wikipedia.org/w/index.php?oldid=994341755> [20210113].
3. <a name="ref3"></a>-, "Electric Field", Circuit globe, url <https://circuitglobe.com/electric-field.html> [20210113].
4. <a name="ref4"></a>Carl R. Nave, "Electric Field", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/electric/elefie.html> [20210113].
5. <a name="ref5"></a>Willy McAllister, "Electric field", Khan Academy, url <https://www.khanacademy.org/science/electrical-engineering/ee-electrostatics/ee-electric-force-and-electric-field/a/ee-electric-field> [20210113].
6. <a name="ref6"></a>Edward Ball, "Electric field line simulator", Academo, url <https://academo.org/demos/electric-field-line-simulator/> [20210125].
7. <a name="ref7"></a>Tom Walsh, "Electric Field Vector Field", GeoGebra, url <https://www.geogebra.org/m/KMVuhygy> [20210125].
8. <a name="ref6"></a>Kate Becker, "What do 'homogeneity' and 'isotropy' mean? (Intermediate)", Ask an Astronomer, 27 Jun 2015, url <http://curious.astro.cornell.edu/about-us/101-the-universe/cosmology-and-the-big-bang/general-questions/574-what-do-homogeneity-and-isotropy-mean-intermediate> [20210124].
{% endcomment %}

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/electrostatics/2021-01-25-electric-field-line-charge-front.md)
