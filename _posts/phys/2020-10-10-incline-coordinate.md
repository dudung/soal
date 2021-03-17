---
layout: post
author: viridi
title: incline coordinate
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["pulley"]
date: 2020-10-10 04:45:00 +07
permalink: /physics/incline-coordinate
---
On an incline [[1](#ref1)] we can choose a coordinate system that reduces complexity of the problem [[2](#ref2)].


## Angle of inclination
Angle of inclination is measured from $x$-axis in counterclockwise direction, which give values between $0^\circ$ and $180^\circ$ [[3](#ref3)], as shown in following Fig. <a href="#fig:ic-angle-of-inclination">1</a>.

<oo>
svg 200 200 #fafafa fig:ic-angle-of-inclination|Angle of inclination of a line, denoted by $\theta$.

style lc:#f00 ls:0 lw:style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 20 180 180 40 40

style lc:#000 ls:0 lw:1 lo:1
arrow 20 180 180 180
arrow 20 180 20 20

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 185 185 x
text 20 12 y

style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 15 197 0
text 55 197 1
text 95 197 2
text 135 197 3

text 5 185 0
text 5 145 1
text 5 105 2
text 5 65 3

style lc:#f00 ls:0 lw:2 lo:1 fc:#f00 fo:1
line 20 180 140 20

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 85 145 &theta;

style lc:#000 ls:8-4 lw:0.8 lo:1 fo:0
polyline 140 180 140 171 139 161 137 152 134 143 131 134 127 126 122 117 117 109 111 102 105 95 98 89 91 83
</oo>

Using this convention we can have following inclines, where the right if as in previous figure, but the left is also common.

<oo>
svg 400 150 #fafafa fig:ic-incline-angle|Angle of inclination of an incline, denoted by $\theta$.

style lc:#000 ls:0 lw:2 lo:1
line 180 130 20 20
line 220 130 380 20

style lc:#000 ls:8-4 lw:0.8 lo:1 fo:0
line 180 130 20 130
line 220 130 380 130

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 120 &theta;
text 260 120 &theta;
</oo>

Both angles $\theta$ in Fig. <a href="#fig:ic-incline-angle">2</a> are measured from horizontal line, where the left is measured in clockwise direction, while the right is measured in counterclockwise direction.


## Common coordinate system
Usually an incline in Fig. <a href="#fig:ic-incline-angle">2</a> (left) will have following coordinate system

<oo>
svg 200 190 #fafafa fig:ic-incline-downward-coordinate|Common coordinate system for downward incline (from left to right).

style lc:#000 ls:0 lw:1 lo:1
line 20 60 180 170

style lc:#000 ls:0 lw:2 lo:1 fc:#000 fo:1
arrow 20 60 60 87
arrow 20 60 47 20

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 5 60 o
text 55 20 y
text 65 80 x

style lc:#000 ls:8-4 lw:0.8 lo:1 fo:0
line 180 170 20 170

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 160 &theta;
</oo>

and for Fig. <a href="#fig:ic-incline-angle">2</a> (right) is as follow

<oo>
svg 240 150 #fafafa fig:ic-incline-upward-coordinate|Common coordinate system for upward incline (from left to right).

style lc:#000 ls:0 lw:1 lo:1
line 60 130 220 20

style lc:#000 ls:0 lw:2 lo:1 fc:#000 fo:1
arrow 60 130 100 103
arrow 60 130 33 90

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 45 135 o
text 95 95 x
text 35 80 y

style lc:#000 ls:8-4 lw:0.8 lo:1 fo:0
line 60 130 220 130

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 100 120 &theta;
</oo>

when we consider that the object is move from left to right. In the future, the axes are not necessarily drawn on the incline line, but could be a little bit off to give a clearer illustration, meanwhile the point $o$ (origint) is better put on the line (or the surface) of the incline. Arrow of the axes are showing the direction, while the point $o$ is indicating the $(0, 0)$ coordinates, a reference point.


## Uncommon coordinate system
We can also have an uncommon coordinate system, where we want to keep the $x$-axis is always parallel to earth surface and $y$-axis is perpendicular to earth surface (or parallel to earth gravitational acceleration $\vec{g}$). Using this uncommon coordinate system, system in Fig. <a href="#fig:ic-incline-downward-coordinate">3</a> and Fig. <a href="#fig:ic-incline-upward-coordinate">4</a> will be changed as follow.

<oo>
svg 400 190 #fafafa fig:ic-incline-uncommon-coordinate|Uncommon coordinate system for downward incline (left) and updward incline (right).

style lc:#000 ls:0 lw:2 lo:1
line 20 60 180 170

style lc:#000 ls:0 lw:2 lo:1 fc:#000 fo:1
arrow 160 100 200 100
arrow 160 100 160 60

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 205 100 x
text 155 50 y

style lc:#000 ls:8-4 lw:0.8 lo:1 fo:0
line 180 170 20 170

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 160 &theta;

style lc:#000 ls:0 lw:2 lo:1
line 220 170 380 60

style lc:#000 ls:8-4 lw:0.8 lo:1 fo:0
line 220 170 380 170

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 260 160 &theta;

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 200 40 g
style lc:#0e0 ls:0 lw:2 lo:1 fc:#0e0 fo:1
arrow 190 20 190 60

style lc:#000 ls:0 lw:2 lo:1 fc:#000 fo:1
circle 20 60 2
circle 220 170 2

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 15 50 o
text 215 160 o
</oo>

Note that in Fig. <a href="#fig:ic-incline-uncommon-coordinate">5</a> we put the points $o$ for each incline but only once draw the axes since it holds for both incline, $y$-axis parallel to $\vec{g}$ (but in opposite direction) and $x$-axis is perpendicular to $\vec{g}$ (with positive direction is to the right).


## Consequences
By choosing common or uncommon coordinate system (CS) there will be some consequences. Let's take only the downward incline as the examples. Assume that the plane is frictionless and there is not any external force other than force due to gravity $w$ and normal force $N$.

**Components** | **Common CS** | **Uncommon CS**
$x$-direction | $\sum F_x = m a_x$ (NLM) | $\sum F_x = m a_x$ (NLM)
| $w \sin \theta = m a_x$ | $N \sin \theta = m a_x$
$y$-direction | $\sum F_y = 0$ (ULM) | $\sum F_y = m a_y$ (NLM)
| $N - w \cos \theta = 0$ | $N \cos \theta - w = m a_y$

From previous table common CS will have uniform linier motion (ULM) in $y$-direction and non-uniform linear motion (NLM) in $x$-direction, while uncommon CS will have NLM in $x$ and $y$-directions. Which CS do you think that will more simplify the problem?

### Solution for common CS
For the common CS we have the solution of

\begin{equation}
\label{eqn:ic-common-cs-solution-x}
a_x = g \sin \theta
\end{equation}

for $x$-direction and

\begin{equation}
\label{eqn:ic-common-cs-solution-y}
a_y = 0
\end{equation}

for $y$-direction. From Eqns. \eqref{eqn:ic-common-cs-solution-x} and \eqref{eqn:ic-common-cs-solution-y} we can get $v_x(t)$, $v_y(t)$, $x(t)$, and $y(t)$ using kinematics.

### Solution for uncommon CS
But for uncommon CS it is not so easy to get the solution. From the table we can have

\begin{equation}
\label{eqn:ic-uncommon-cs-solution-xy}
a_x - a_y \tan \theta = g \tan \theta,
\end{equation}

which requires additional constraint to solve it. The constraint is

\begin{equation}
\label{eqn:ic-uncommon-cs-constraint-xy}
y = (-\tan \theta) x,
\end{equation}

where it is simply the incline that restricts the motion. Differentiate Eqn. \eqref{eqn:ic-uncommon-cs-constraint-xy} twice with respect to time $t$ will produce

\begin{equation}
\label{eqn:ic-uncommon-cs-constraint-axay}
a_y = (-\tan \theta) a_x.
\end{equation}

Substitution of Eqn. \eqref{eqn:ic-uncommon-cs-constraint-axay} into Eqn. \eqref{eqn:ic-uncommon-cs-solution-xy} will give

\begin{equation}
\label{eqn:ic-uncommon-cs-solution-ax}
a_x = g \sin \theta \cos \theta
\end{equation}

and

\begin{equation}
\label{eqn:ic-uncommon-cs-solution-ay}
a_y = -g \sin^2 \theta.
\end{equation}

Again, using Eqns. \eqref{eqn:ic-uncommon-cs-solution-ax} and \eqref{eqn:ic-uncommon-cs-solution-ay} with kinematics, solution for $v_x(t)$, $v_y(t)$, $x(t)$, and $y(t)$ can be found.


## Note
Detail of object motion on an incline will be discussed in another article. 


## Exercises
1. Draw a free-body diagram to obtain Eqns. \eqref{eqn:ic-common-cs-solution-x} and \eqref{eqn:ic-common-cs-solution-y}.
2. Using uncommon CS draw the free-body diagram and write the Newtons' 2nd law of the system.
3. Show how to obtain Eqns. \eqref{eqn:ic-uncommon-cs-solution-ax} and \eqref{eqn:ic-uncommon-cs-solution-ay}.


## References
1. <a name="ref1"></a>Wikipedia contributors, "Inclined plane", Wikipedia, The Free Encyclopedia, 29 Sep 2020, 20:12 UTC, <https://en.wikipedia.org/w/index.php?oldid=981018186> [20201010].
2. <a name="ref2"></a>H. Trevor Johnson-Steigelman, "Inclined Plane Coordinate System", physicsthisweek.com, a branch of  Coaches of Technology, Inc., 29 Sept 2014, url <https://www.physicsthisweek.com/physics-i/inclined-plane/inclined-plane-coordinate-system/> [20201010].
3. <a name="ref3"></a>Bruce Simmons, "Angle of Inclination of a Line", Mathwords: Terms and Formulas from Algebra I to Calculus, 19 Jul 2017, url <https://www.mathwords.com/a/angle_inclination.htm> [20201010].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-10-10-incline-coordinate.md)
