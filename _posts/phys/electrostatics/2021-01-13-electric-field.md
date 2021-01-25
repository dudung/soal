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
date: 2021-01-25 08:21:00 +07
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

Illustration to obtain electric field from a point charge $q_j$, where it can negative or positive, is given in Fig. <a href="#fig:ef-electric-field-from-force-point-charge">1</a>. Implicitly source charge $q_j$ and unit positive test charge $q_i$ are located at $\vec{r}_j$ and $\vec{r}_i$, respectively.


## electric field lines
By observing many points in space around a source charge, previous Fig. <a href="#fig:ef-electric-field-from-force-point-charge">1</a> could give help how we can draw electric field lines of a point charge. It should begin from a positive charge and end to a negative charge. For an isolated single positive change and also a single negative one, the electric field lines is given in Fig. <a href="#fig:ef-electric-field-lines-1-charge">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/electric-field-lines-1-charge.png)
<br />
Figure <a name="fig:ef-electric-field-lines-1-charge">2</a> Electric field lines of a point charge: out of a positive charge (left) and into a negative charge (right).
{: refdef}

For more point charges or chage distribution the electric field lines can be constructed as superposition of the two basic types, negative and positive charges.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/eletric-field-lines-line-point-charges.png)
<br />
Figure <a name="fig:ef-eletric-field-lines-line-point-charges">3</a> Electric field lines of negative line charge (left) and a positive point charge (right).
{: refdef}

Electric field lines in Fig. <a href="#fig:ef-eletric-field-lines-line-point-charges">3</a> is drawn illustratively, where it might has assumptions in drawing the lines. There are available visualization of two or more charges that can be used to see how the electric field lines drawn [[6](#ref6),[7](#ref7)].


## electric field due to point charge
By changing $\vec{r}_i$ to more general position $\vec{r}$ and using the [relative position](/physics/position#relative-position) we can write

\begin{equation}
\label{eqn:ef-electric-field-point-charge}
\vec{E}_j(\vec{r}) = k \frac{q_j}{\| \vec{r} - \vec{r}_j \|^3} \ (\vec{r} - \vec{r}_j),
\end{equation}

which is electric field at arbitraty position $\vec{r}$ due to existence of charge $q_j$ located at $\vec{r}_j$. Illustration of Eqn. \eqref{eqn:ef-electric-field-point-charge} is given in Fig. <a href="#fig:ef-electric-field-point-charge">4</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/electric-field-point-charge.png)
<br />
Figure <a name="fig:ef-electric-field-point-charge">4</a> Electric field $\vec{E}_j$ due to a point charge $q_j$.
{: refdef}

We can see from Fig. <a href="#fig:ef-electric-field-point-charge">4</a> that what matter related to position is only relative position of observation point $\vec{r}$ to the position of source charge $q_j$ located at $\vec{r}_j$ or simply $\vec{r} - \vec{r}_j$.

### example
At position $\vec{r}_j = (2\hat{x} + 3\hat{y} + 4\hat{z}) \ \rm \mu m$ there is a point charge $q_j = 169 \ \rm nC$. Find the electric field at position $\vec{r} = (5\hat{x} + 7\hat{y} + 16\hat{z}) \ \rm \mu m$. What is the magnitude and unit vector of the electric field?

$\vec{r} - \vec{r}_j = (5-2)\hat{x} + (7-3)\hat{y} + (16-4)\hat{z} = (3\hat{x} + 4\hat{y} + 12\hat{z}) \ \rm \mu m$. \
$\| \vec{r} - \vec{r}_j \| = \sqrt{(\vec{r} - \vec{r}_j)\cdot(\vec{r} - \vec{r}_j)} = \sqrt{(3\hat{x} + 4\hat{y} + 12\hat{z})\cdot(3\hat{x} + 4\hat{y} + 12\hat{z})}$ \
$ = \sqrt{(3)^2 + (4)^2 + (12)^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13 \ \rm \mu m$. \
$\displaystyle \vec{E}_j(\vec{r}) = (9\times 10^9) \frac{169\times 10^{-9}}{(13\times 10^{-6})^3} (3\hat{x} + 4\hat{y} + 12\hat{z}) \times 10^{-6} $ \
$ = (9\times 10^{12}) \left( \frac{3}{13}\hat{x} + \frac{4}{13}\hat{y} + \frac{12}{13}\hat{z} \right) \ \rm N/C$. \
Since $\vec{E}_j = E_j \ \hat{E}_j$, \
$E_j = \| \vec{E}_j \| = 9\times 10^{12} \ \rm N/C$, \
$\hat{E}_j = \vec{E}_j / E_j = \left( \frac{3}{13}\hat{x} + \frac{4}{13}\hat{y} + \frac{12}{13}\hat{z} \right)$.


## electric field due to charge distribution
In real world it is difficult to have a point charge, but group of charges that can assemble a charge distribution $dq_j$, which illustation is given in Fig. <a href="#fig:ef-electric-field-charge-distribution">5</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/electric-field-charge-distribution.png)
<br />
Figure <a name="fig:ef-electric-field-charge-distribution">5</a> Element of electric field $d\vec{E}_j$ due to element of charge distribution $dq_j$.
{: refdef}

Instead of electric field $\vec{E}_j$ as in Eqn. \eqref{eqn:ef-electric-field-point-charge}, Fig. <a href="#fig:ef-electric-field-charge-distribution">5</a> gives the element of electric field $d\vec{E}_j$ due to element of charge distribution $dq_j$, which is formulated as

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

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/electrostatics/2021-01-13-electric-field.md)
