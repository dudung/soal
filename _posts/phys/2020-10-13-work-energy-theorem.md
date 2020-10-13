---
layout: post
author: viridi
title: work-energy theorem
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["tutorial"]
date: 2020-10-13 04:46:00 +07
permalink: /physics/work-energy-theorem
---
Here we will discuss about work-energy theorem [[1](#ref1)] and how it helps to solve a problem in easier way compared to the use of dynamics and [work](work) concepts together. [Kinetic energy](kinetic-energy) concept will also be used here.

## Change in kinetic energy
If at initial time $t_i$ a particle with mass $m$ has velocity of $v_i$ and at final time $t_f$ it has velocity of $v_f$ then change of particle's kinetic energy is

\begin{equation}
\label{eqn:wet-work-integral}
\Delta K = K_f - K_i = \frac12 m v_f^2 - \frac12 m v_i^2,
\end{equation}

where the subscript $i$ and $f$ can be any subscript provided by a problem.


## Work due to constant force in linear motion
In  this part we will limit the discussion to the work due to constant force only and for the case of linear motion. A start the force is also assumed to be always parallel to the trajectory $s$. If $F$ is the only force works on the object, then the work is simply

\begin{equation}
\label{eqn:wet-work}
W = F \Delta s,
\end{equation}

where $\Delta s$ is the displacement. In 1-d kinematics we are used to use $\Delta x = x_f - x_i$ instead of $\Delta s$.


## Work-energy theorem
The theorem states that the change in kinetic energy is equal to the work of net force

\begin{equation}
\label{eqn:wet-theorem}
W = \Delta K,
\end{equation}

where the work is

\begin{equation}
\label{eqn:wet-work-net-force}
W = (\Sigma F) \Delta s.
\end{equation}

According to Newtons' second law for linear motion

\begin{equation}
\label{eqn:wet-newton-2}
\Sigma F = ma.
\end{equation}

Subsitute Eqn. \eqref{eqn:wet-newton-2} ino Eqn. \eqref{eqn:wet-work-net-force}, and then the result into Eqn. \eqref{eqn:wet-theorem} will produce

\begin{equation}
\label{eqn:wet-theorem-proof}
ma \Delta x = \frac12 mv_f^2 - \frac12 mv_i^2.
\end{equation}

Multiply Eqn. \eqref with $2/m$ and rearrange the terms, we can have

\begin{equation}
\label{eqn:wet-theorem-proof-kinematics}
v_f^2 = v_i^2 + 2a(x_f - x_i),
\end{equation}

which is one of the well-known kinematics formula.


## Moving on a horizontal surface with friction
A block with mass $m$ is moving on a horizontal surface with friction $\mu_k$ and is continuously pulled with a constant force $F_{\rm ext}$ that has an angle $\theta$ with the horizontal in the direction of the motion. Observation is taken place at two points, $x_A$ and $x_B$, where the block passes them at time $t_A$ and $t_B$, respectively.

<oo>
svg 400 200 #fafafa fig:wet-horiz-surf-fric-fext|A block with mass $m$ is moving on a horizontal surface with friction $\mu_k$ and is pulled by a constant force $F_{\rm ext}$.

# Standard gravity
style lc:#0c0 ls:0 lw:2 lo:1 fc:#0c0 fo:1
arrow 20 30 20 70
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 15 20 g
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 30 20 = 10 m/s
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 87 15 2

# Horizontal floor
style lc:#000 ls:0 lw:2 lo:1
line 20 120 380 120
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 193 140 &mu;
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:10px
text 200 145 k
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 210 140 = 0.2

# Block at xA
style lc:#000 ls:0 lw:2 lo:1 fc:#ddd fo:1
rect 60 60 60 60
style lc:#000 ls:0 lw:2 lo:1 fc:#000 fo:1
circle 90 120 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 83 140 x
text 83 170 t
text 130 100 v
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:10px
text 90 145 A
text 90 175 A
text 137 105 A
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 100 140 = 4 m
text 100 170 = 2 s
text 147 100 = 7 m/s
style lc:#00f ls:0 lw:2 lo:1 fc:#00f fo:1
arrow 130 80 150 80

# Block at xB
style lc:#000 ls:4-2 lw:1 lo:1 fc:#eee fo:1
rect 280 60 60 60
style lc:#000 ls:0 lw:2 lo:1 fc:#000 fo:1
circle 310 120 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 303 140 x
text 303 170 t
text 350 100 v
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:10px
text 310 145 B
text 310 175 B
text 357 105 B
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 320 140 = 100 m
style lc:#00f ls:0 lw:2 lo:1 fc:#00f fo:1
arrow 350 80 380 80

# External force Fext
style lc:#f88 ls:0 lw:3 lo:1 fc:#f88 fo:1
arrow 120 60 160 30
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 140 20 F
text 140 57 &theta;
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 148 25 ext
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 165 20 = 100 N
style lc:#000 ls:4-2 lw:1 lo:1 fc:#000 fo:1
line 120 60 160 60
style lc:#f88 ls:4-2 lw:2 lo:1 fc:#f88 fo:1
arrow 340 60 380 30

# tan \theta
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 190 60 tan
text 225 60 = 3/4
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 212 60 &theta;

</oo>

Value of some physical quantities are given in Fig. <a href="#fig:wet-horiz-surf-fric-fext">1</a>. (a) Determine when the block passes point $B$ and its velocity at that point using dynamics and kinematics. (b) Find the kinetic energy at point $B$ using previous solution and using work-energy theorem.

### Free-body diagram
Free-body diagram of the block is as shown in Fig. <a href="#fig:wet-horiz-surf-fric-fext-fbd">2</a>

### Newtons' laws
Using Fig. <a href="#fig:wet-horiz-surf-fric-fext-fbd">2</a> we can have in $y$-direction

\begin{equation}
\label{eqn:wet-hsf-fext-fbd-y}
\begin{array}{rcl}
\sum F_y & = & 0 \newline 
F_{\rm ext} \ \sin \theta + N - w & = & 0 \newline
N & = & w - F_{\rm ext} \ \sin \theta
\end{array}
\end{equation}

and in $x$-direction

\begin{equation}
\label{eqn:wet-hsf-fext-fbd-x}
\begin{array}{rcl}
\sum F_x & = & m a_x \newline 
F_{\rm ext} \ \cos \theta - f_k & = & m a_x \newline
a_x & = & \displaystyle \frac{F_{\rm ext} \ \cos \theta - f_k}{m}.
\end{array}
\end{equation}

### Weight and kinetic friction
Weight of the block

\begin{equation}
\label{eqn:wet-hsf-fext-w}
w = mg
\end{equation}

and kinetic friction

\begin{equation}
\label{eqn:wet-hsf-fext-fk}
f_k = \mu_k N.
\end{equation}

Substitute Eqn. \eqref{eqn:wet-hsf-fext-w} into Eqn. \eqref{eqn:wet-hsf-fext-fbd-y}, then the result into Eqn. \eqref{eqn:wet-hsf-fext-fk}, finally into Eqn. \eqref{eqn:wet-hsf-fext-fbd-x}, will give

\begin{equation}
\label{eqn:wet-hsf-fext-fbd-solution}
a_x = \frac{F_{\rm ext}}{m}(\cos \theta + \mu_k \sin \theta) - \mu_k g.
\end{equation}


## Exercises
1. An object has initial velocity of $4 \ \rm m/s$ to a certain direction and final velocity of $(3 \hat{i} + 4 \hat{j}) \ \rm m/s$. Find its initial kinetic energy, final kinetic energy, and change in object's kinetic energy.
2. Show how to obtain Eqn. \eqref{eqn:wet-theorem-proof-kinematics} from Eqn. \eqref{eqn:wet-theorem}.
3. Consider a horizontal surface, where an object is moving on it with coefficient of kinetic friction $\mu_k$. While moves from point $A$ to point $B$ the object is also under influence of an external force $F_{\rm ext}$ besides the kinetic friction $f_k$. The object has mass $m$. Velocity at the points are $v_A$ and $v_B$, respectively. The distance between the points are $\Delta x = x_B - x_A$ and the time required to go from point $A$ to point $B$ is $\Delta t = t_B - t_A$. Show the relation between mentioned physical quantities.


## Quiz
Suppose that there is a particle with mass $m = 2 \ \rm kg$ moving on a horizontal surface with coefficient of kinetic friction 0.1. It has initial velocity of $5 \ \rm m/s$ and a constant force $F_1 = 4 \ \rm N$ parallel to the surfrace and in the direction of the velocity is always applied to the particle. The distance travel by the particle from initial to final position is $3 \ \rm m$. Find particle final velocity using (a) dynamics and then kinematics, (b) work-energy theorem, and (c) compare number of steps required to solve the problem and discuss which one is preferable.

+ [Submit answer](https://forms.office.com/Pages/ResponsePage.aspx?id=gxFu22VMXECCznzVP6bp3NGUp4ijN01Ks-VZMpTE-hpUN1VJQVRKMTNXNlM4TUwwMkxWMTJQTFZFVC4u)


## References
1. <a name="ref1"></a>-, "Work-Energy Theorem", in Boundless Physics, Lumen Learning, url <https://courses.lumenlearning.com/boundless-physics/chapter/work-energy-theorem/> [20201013].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-10-13-work-energy-theorem.md)
