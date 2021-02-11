---
layout: post
author: viridi
title: system of linear equations examples
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "linear", "equation", "system"]
date: 2021-02-11 18:37:00 +07
permalink: /fi3201/sle-examples
---
Even today we can solve system of linear equations (SLE) online, eg. for four equations [[1](#ref1)], it is still interesting to study the SLE especially when you try to find the solution for inconsistent system [[2](#ref2)]. Solution of an SLE must satisfy all equations in the system, which are considered collectively, not individually [[3](#ref3)]. We propose some systems in physics and how we can get the SLE from them.


## observing non-uniform linear motion
In a non-uniform linear motion position of particle $x$ is given by

\begin{equation}
\label{eqn:slee-non-uniform-linear-motion}
x = x_0 + v_0 t + \frac12 at^2,
\end{equation}

where $x_0$ and $v_0$ are initial position and velocity, respecttively, at $t = 0$ and $a$ is acceleration. Suppose that there are three observations at different time $t = t_1$, $t = t_2$, and $t = t_3$ as shown in Fig. <a href="#fig:slee-non-uniform-linear-motion">1</a>. The initial conditions at $t = 0$ for position $x_0$ and velocity $v_0$ are unknown. Acceleration $a$ is also unknown.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/sle/non-uniform-linear-motion.png)
<br />
Figure <a name="fig:slee-non-uniform-linear-motion">1</a> An object drawn as red circle is moving from left to right with initial position $x_0$ and velocity $v_0$ at $t = 0$ are unknown.
{: refdef}

From the observations we can have

\begin{eqnarray}
\label{eqn:slee-non-uniform-linear-motion-t1}
x_1 = x_0 + v_0 t_1 + \frac12 a t_1^2, \newline
\label{eqn:slee-non-uniform-linear-motion-t2}
x_2 = x_0 + v_0 t_2 + \frac12 a t_2^2, \newline
\label{eqn:slee-non-uniform-linear-motion-t3}
x_3 = x_0 + v_0 t_3 + \frac12 a t_3^2,
\end{eqnarray}

that can be rewritten in the form of

\begin{equation}
\label{eqn:slee-non-uniform-linear-motion-sle}
\left(
\begin{array}{ccc}
1 & t_1 & \frac12 t_1^2 \newline
1 & t_2 & \frac12 t_2^2 \newline
1 & t_3 & \frac12 t_3^2 
\end{array}
\right)
\left(
\begin{array}{c}
x_0 \newline
v_0 \newline
a
\end{array}
\right)
=
\left(
\begin{array}{c}
x_1 \newline
x_2 \newline
x_3
\end{array}
\right),
\end{equation}

which is matrix representation of a LSE [[4](#ref4)] for uknowns of $x_0$, $v_0$, and $a$.


## speed up and slow down in a linear motion
Still observing one-dimensional motion, an object can move in three different types of motion. Let make the first is non-uniform linear motion with positive acceleration, the second is linear motion, and the third is non-uniform linear motion but with negative acceleration. Assume that this system represents a block moving on a level ground with various kinetic frictions $f_1$, $f_2$, $f_3$ and a constant force $F_1$ is applied during $0 < t < t_1$, $F_2$ is applied during $t_1 < t < t_2$, and $F_3$ is applied during $t_2 < t < t_3$, that makes the velocity functions is as in Fig. <a href="#fig:slee-kinematics-1d-nlm-lm-nlm">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/sle/kinematics-1d-nlm-lm-nlm.png)
<br />
Figure <a name="fig:slee-kinematics-1d-nlm-lm-nlm">2</a> Velocity of a block moving on a rough level ground where different horizontal force is applied at different time ranges ($0 < t < t_1$, $t_1 < t < t_2$, and $t_2 < t < t_3$).
{: refdef}

Since $a_1 = v_{\max} / \Delta t_1$, $a_2 = 0$, and $a_3 = - v_{\max} / \Delta t_3$ with $\Delta t_1 = t_1 - 0$, $\Delta t_2 = t_2 - t_1$, and $\Delta t_3 = t_3 - t_2$, we can have that $F_1 = m\frac{v_{\max}}{\Delta t_1} + f_k$, $F_2 = f_k$, and $F_3 = -m\frac{v_{\max}}{\Delta t_2} + f_k$. Then


\begin{equation}
\label{eqn:slee-nlm-lm-nlm-Wext}
W_{\rm ext} = \frac12 v_{\max} f_1 \Delta t_1 + v_{\max} f_2 \Delta t_2 + \frac12 v_{\max} f_3 \Delta t_3
\end{equation}

is the total work by external forces. Total time is

\begin{equation}
\label{eqn:slee-nlm-lm-nlm-Dt-total}
\Delta t_{\rm tot} = \Delta t_1 + \Delta t_2 + \Delta t_3
\end{equation}

and 

\begin{equation}
\label{eqn:slee-nlm-lm-nlm-S-total}
\Delta s_{\rm tot} = \frac12 v_{\max} \Delta t_1 + v_{\max} \Delta t_2 + \frac12 v_{\max} \Delta t_3
\end{equation}

is the total distance travelled by the object. We can rewrite Eqns. \eqref{eqn:slee-nlm-lm-nlm-Wext}, \eqref{eqn:slee-nlm-lm-nlm-Dt-total}, and \eqref{eqn:slee-nlm-lm-nlm-S-total} in the form of

\begin{equation}
\label{eqn:slee-nlm-lm-nlm-sle}
\left(
\begin{array}{ccc}
\frac12 v_{\max} f_1 & v_{\max} f_2 & \frac12 v_{\max} f_3 \newline
1 & 1 & 1 \newline
\frac12 v_{\max} & v_{\max} & \frac12 v_{\max} 
\end{array}
\right)
\left(
\begin{array}{c}
\Delta t_1 \newline
\Delta t_2 \newline
\Delta t_3
\end{array}
\right)
=
\left(
\begin{array}{c}
W_{\rm ext} \newline
\Delta t_{\rm tot} \newline
\Delta s_{\rm tot}
\end{array}
\right),
\end{equation}

which is, again, the SLE matrix representation for uknowns of $\Delta t_1$, $\Delta t_2$, and $\Delta t_3$.


## battery resistor dc circuit with three loops
Other topic in physics than kinematics can be also as example of LSE, e.g. dc circuit containing resistors and batteries as shown in Fig. <a href="#fig:slee-dc-er-circuit-3-loops">3</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/sle/dc-er-circuit-3-loops.png)
<br /> 
Figure <a name="fig:slee-dc-er-circuit-3-loops">3</a> A DC circuit with three loops containing resistors and batteries.
{: refdef}

The Kirchhof first law is not required for the system since we have already write the relation between current at points $a$, $b$, $c$, and $d$. Then we will apply the Kirchhof second law in the $a-b-c$

\begin{equation}
\label{eqn:slee-dc-er-circuit-3-loops-abc}
R_1 I_1 + R_3 (I_1 + I_2) + R_4 (I_1 - I_3) = \varepsilon_1,
\end{equation}

$a-b-d$,

\begin{equation}
\label{eqn:slee-dc-er-circuit-3-loops-abd}
R_2 I_2 + R_3 (I_1 + I_2) + R_5 (I_2 + I_3) = \varepsilon_2,
\end{equation}

and $c-b-d$

\begin{equation}
\label{eqn:slee-dc-er-circuit-3-loops-cbd}
 -R_4 (I_1 - I_3) + R_5 (I_2 + I_3) + (R_6 + R_8 + R_7) I_3 = \varepsilon_3
\end{equation}

loops. Finally, we have

\begin{equation}
\label{eqn:slee-dc-er-circuit-3-loops-sle}
\left(
\begin{array}{ccc}
1 & t_1 & \frac12 t_1^2 \newline
1 & t_2 & \frac12 t_2^2 \newline
1 & t_3 & \frac12 t_3^2 
\end{array}
\right)
\left(
\begin{array}{c}
x_0 \newline
v_0 \newline
a
\end{array}
\right)
=
\left(
\begin{array}{c}
x_1 \newline
x_2 \newline
x_3
\end{array}
\right),
\end{equation}

as the SLE matrix representation for uknowns of $I_1$, $I_2$, and $I_3$.


## references
1. <a name="ref1"></a>-, "Online Systems of Equations Solver: Solve equations and systems of equations with Wolfram\|Alpha", Wolfram Alpha, 2021, url <https://www.wolframalpha.com/calculators/system-equation-calculator> [20210211].
2. <a name="ref2"></a>Elizabeth Stapel, "Systems of Linear Equations" Purple Math, 2020, url <https://www.purplemath.com/modules/systlin1.htm> [20210211].
3. <a name="ref3"></a>Wikipedia contributors, "System of linear equations", Wikipedia, The Free Encyclopedia, 17 January 2021, 17:30 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1000977892> [20210211].
4. <a name="ref4"></a>-, "Representing Systems of Linear Equations using Matrices", Hotmath, Varsity Tutors, url <https://www.varsitytutors.com/hotmath/hotmath_help/topics/representing-systems-of-linear-equations-using-matrices> [20210211].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-02-11-sle-examples.md)
