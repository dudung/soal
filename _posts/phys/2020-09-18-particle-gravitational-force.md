---
layout: post
author: viridi
title: particle gravitational force
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["particle", "gravitation", "force"]
date: 2020-09-18 05:05:00 +07
permalink: /physics/particle-gravitational-force
---
Gravitational force (or gravity or gravitation) is the universal force of attraction acting between all matters [[1](#ref1)]. The gravitational force between two masses is often called the universal law of gravitation [[2](#ref2)] or Newton's law of universal gravitation [[3](#ref3)].


## Equation
Equation of the universal law of gravitation in [vector](vector) form is

\begin{equation}
\label{eqn:pgf-force-equation}
\vec{F}_{ij} = -G \frac{m_1 m_j}{r _{ij} ^2} \hat{r} _{ij},
\end{equation}

which gives the force acting on particle with mass $m_i$ due to existence of particle with mass $m_j$, where their separation distance is $r_{ij}$. And $G$ having value of

\begin{equation}
\label{eqn:pgf-gravitational-constant}
G = 6.672 59(85) \times 10^{-11} \ {\rm m}^3 \cdot {\rm kg}^{-1} \cdot {\rm s}^{-2}
\end{equation}

is gravitational constant [[4](#ref4)]. Using Eqn. \eqref{eqn:pgf-force-equation} direction of the force is already accomodated with the minus sign together with unit vector of relative position $\hat{r}_{ij}$, which gives that this force is always attractive. In the scalar form of the equation

\begin{equation}
\label{eqn:pgf-force-equation-scalar}
F_{ij} = G \frac{m_1 m_j}{r _{ij} ^2},
\end{equation}

the directon of the force must be first understood, because it gives only the magnitude of the force but not the direction. See the case of [particle electrostatic force](particle electrostatic force), where there are attractive and repulsive forces. 


## Relative position
Gravitational force works only along the line connected the two masses, $m_i$ and $m_j$ or force direction is parallel to this line. The direction is given by unit vector $\hat{r}_{ij}$, which is calculated from

\begin{equation}
\label{eqn:pgf-relative-position-unit}
\hat{r}_{ij} = \frac{\vec{r} _{ij}}{r _{ij}},
\end{equation}

where

\begin{equation}
\label{eqn:pgf-relative-position}
\vec{r}_{ij} = \vec{r}_i - \vec{r}_j
\end{equation}

is relative position or position of mass $m_i$ relative to position of mass $m_j$ and

\begin{equation}
\label{eqn:pgf-relative-position-magnitude}
r_{ij} = | \vec{r} _{ij} | = \sqrt{\vec{r} _{ij} \cdot \vec{r} _{ij}}
\end{equation}

is seperation distance between mass $m_i$ and $m_j$.


## Force components
Eqn. \eqref{eqn:pgf-force-equation} can also be written using its components in each direction, $x$, $y$, and $z$,

\begin{equation}
\label{eqn:pgf-force-equation-component}
\vec{F}_{ij} = F _{ij,x} \ \hat{x} + F _{ij,y} \ \hat{y} + F _{ij,z} \ \hat{z},
\end{equation}

with

$$
\begin{eqnarray}
\label{eqn:pgf-force-equation-components-x}
F _{ij,x} & = & -G \left( \frac{m_i m_j}{x _{ij}^2 + y _{ij}^2 + z _{ij}^2} \right) \left( \frac{x_{ij}}{\sqrt{x_{ij}^2 + y_{ij}^2 + z _{ij}^2}} \right), \\[0.5em]
\label{eqn:pgf-force-equation-components-y}
F _{ij,y} & = & -G \left( \frac{m_i m_j}{x _{ij}^2 + y _{ij}^2 + z _{ij}^2} \right) \left( \frac{y_{ij}}{\sqrt{x_{ij}^2 + y_{ij}^2 + z _{ij}^2}} \right), \\[0.5em]
\label{eqn:pgf-force-equation-components-z}
F _{ij,z} & = & -G \left( \frac{m_i m_j}{x _{ij}^2 + y _{ij}^2 + z _{ij}^2} \right) \left( \frac{z_{ij}}{\sqrt{x_{ij}^2 + y_{ij}^2 + z _{ij}^2}} \right).
\end{eqnarray}
$$

And similar to Eqn. \eqref{eqn:pgf-relative-position}

$$
\begin{eqnarray}
\label{eqn:pgf-relative-position-x}
x_{ij} & = & x_i - x_j, \\[0.5em]
\label{eqn:pgf-relative-position-y}
y_{ij} & = & y_i - y_j, \\[0.5em]
\label{eqn:pgf-relative-position-z}
z_{ij} & = & z_i - z_j.
\end{eqnarray}
$$

Note hat we use $\hat{x}$, $\hat{y}$, and $\hat{z}$ instead of $\hat{i}$, $\hat{j}$, and $\hat{k}$ in Eqn. \eqref{eqn:pgf-force-equation-component} to avoid confusion with particle index $i$ and $j$.


## Exercises
1. By equating Eqns. \eqref{eqn:pgf-force-equation} and \eqref{eqn:pgf-force-equation-component}, show the steps to produce Eqns. \eqref{eqn:pgf-force-equation-components-x} - \eqref{eqn:pgf-force-equation-components-z}.
2. Give your comments, which equation is easier to implement in programming, Eqn. \eqref{eqn:pgf-force-equation} or \eqref{eqn:pgf-force-equation-component}, when you use conventional programming and when you use object oriented programming (OOP).


## References
1. <a name="ref1"></a>James E. Faller, Alan H. Cook, Kenneth L. Nordtvedt, Vivek Abhinav, Adam Augustyn, Yamini Chauhan, Erik Gregersen, Parul Jain, William L. Hosch, Gloria Lotha, Richard Pallardy, Marco Sampaolo, Veenu Setia, Shiveta Singh, Amy Tikkanen, Grace Young, and The Editors of Encyclopaedia Britannica, "Gravity", Encyclopædia Britannica, 20 Jun 2019, url <https://www.britannica.com/science/gravity-physics> [20200918].
2. <a name="ref2"></a>Carl R. Nave, "Gravity", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/grav.html> [20200918].
3. <a name="ref3"></a>Wikipedia contributors, "Step function", Wikipedia, The Free Encyclopedia, 17 Sep 2020, 20:12 UTC, <https://en.wikipedia.org/w/index.php?oldid=978934382> [20200918].
4. <a name="ref4"></a>A. D. McNaught, A. Wilkinson (eds.), "Compendium of Chemical Terminology (IUPAC Gold Book)", Blackwell Scientific Publications, Oxford, 2nd edition, Dec 1997, url <https://isbnsearch.org/isbn/9780865426849>; S. J. Chalk, online version (2019-), ISBN 0-9678550-9-8, url <https://doi.org/10.1351/goldbook.G02695>.

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-09-18-particle-gravitational-force.md)
