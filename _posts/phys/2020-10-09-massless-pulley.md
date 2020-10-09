---
layout: post
author: viridi
title: massless pulley
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["pulley"]
date: 2020-10-09 19:09:00 +07
permalink: /physics/massless-pulley
---
System of two masses and one pulley connected with a string is usually approximated using a massless, inextensible string and an ideal massless pulley as in Atwood machine [[1](#ref1)].


## System
Two masses $m_1$ and $m_2$ are connected with an ideal string passing an ideal pulley as shown in Fig. <a href="#fig:mp-system">1</a>

<oo>
svg 200 200 #fafafa fig:mp-system|An ideal pulley $\rm P$ connecting two masses $m_1$ and $m_2$ through an ideal string.

style lc:#000 ls:0 lw:2 lo:1 fc:#fff fo:1
circle 100 50 30
style lc:#000 ls:0 lw:2 lo:1 fc:#eee fo:1
rect 80 0 40 60
style lc:#000 ls:0 lw:2 lo:1 fc:#fff fo:1
circle 100 50 3
style lc:#000 ls:0 lw:2 lo:1 fc:#eee fo:1
rect 70 0 60 10
style lc:#000 ls:0 lw:2 lo:1 fc:#fff fo:1
line 70 50 70 130
line 130 50 130 130
rect 50 130 40 40
rect 110 130 40 40

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 60 155 m
text 120 155 m
text 30 40 g
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 72 160 1
text 132 160 2
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 100 100 P

style lc:#0e0 ls:0 lw:2 lo:1 fc:#0e0 fo:1
arrow 20 20 20 60
</oo>

In the system illustrated by Fig. <a href="#fig:mp-system">1</a> there are masses $m_1$ and $m_2$, pulley $\rm P$, ceiling where the pulley is attached on, and string connecting the two masses through the pulley. Here we consider an ideal pulley and an ideal string, and also that the pulley remains stationary, which leaves only the two masses to discuss. 


## Considered forces
For each mass there are only two cosidered forces, where the first is string tension $T$ and the second is

\begin{equation}
\label{eqn:mp-w=mg}
w = mg,
\end{equation}

the earth gravitational force near earth surface.


## Free-body diagram
Since Newtons' first and second laws deal with all forces working on an isolated object, we require to have a free-body diagrams for $m_1$ and $m_2$. Assuming that $m_2 > m_1$ than accelerations $\vec{a}$ are drawn for each mass as shown in Fig. <a href="#fig:mp-free-body-diagram">2</a>.

<oo>
svg 200 200 #fafafa fig:mp-free-body-diagram|Free-body diagrams of $m_1$ (left) and $m_2$ (right), with assumption that $m_2 > m_1$.

style lc:#000 ls:0 lw:2 lo:1 fc:#fff fo:1
line 50 20 50 80
line 150 20 150 80
rect 30 80 40 40
rect 130 80 40 40

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 40 95 m
text 140 95 m
text 100 40 g
text 40 160 w
text 140 175 w
text 5 120 a
text 180 95 a

style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 52 100 1
text 152 100 2
text 52 165 1
text 152 180 2
text 15 125 1
text 190 100 2

style lc:#0e0 ls:0 lw:2 lo:1 fc:#0e0 fo:1
arrow 90 20 90 60

style lc:#f00 ls:0 lw:2 lo:1 fc:#f00 fo:1
arrow 50 80 50 40
arrow 150 80 150 40

style lc:#00f ls:0 lw:2 lo:1 fc:#00f fo:1
arrow 50 105 50 145
arrow 150 105 150 160

style lc:#f0f ls:0 lw:2 lo:1 fc:#f0f fo:1
arrow 10 105 10 65
arrow 190 105 190 145
</oo>

Due to ideal string and pulley then as consequences

\begin{equation}
\label{eqn:mp-a1=a2=a}
a_1 = a_2 = a
\end{equation}

and

\begin{equation}
\label{eqn:mp-T1=T2=T}
T_1 = T_2 = T,
\end{equation}

which will be used later.


## Newtons' 2nd law
Using Fig. <a href="#fig:mp-free-body-diagram">2</a> we can write for the mass $m_1$ that

\begin{equation}
\label{eqn:mp-newton2-m1}
\begin{array}{rcl}
\sum F_1 & = & m_1 a_1 \newline
T_1 - w_1 & = & m_1 a_1 \newline
T_1 & = & w_1 + m_1 a_1
\end{array}
\end{equation}

and

\begin{equation}
\label{eqn:mp-newton2-m2}
\begin{array}{rcl}
\sum F_2 & = & m_2 a_2 \newline
w_2 - T_2 & = & m_2 a_2 \newline
w_2 - m_2 a_2& = & T_2.
\end{array}
\end{equation}

## Solution
Substitution of Eqns. \eqref{eqn:mp-w=mg}, \eqref{eqn:mp-a1=a2=a}, and \eqref{eqn:mp-T1=T2=T} into Eqns. \eqref{eqn:mp-newton2-m1} and \eqref{eqn:mp-newton2-m2}, will produce

\begin{equation}
\label{eqn:mp-newton2-m1-sol}
T = m_1 g + m_1 a
\end{equation}

and

\begin{equation}
\label{eqn:mp-newton2-m2-sol}
T = m_2 g - m_2 a
\end{equation}

Equating the last two equations, Eqns. \eqref{eqn:mp-newton2-m1-sol} and \eqref{eqn:mp-newton2-m2-sol} will give

\begin{equation}
\label{eqn:mp-newton2-m1-sol-a}
a = \left( \frac{m_2 - m_1}{m_2 + m_1} \right) g.
\end{equation}

We can also obtain

\begin{equation}
\label{eqn:mp-newton2-m1-sol-T}
T = \left( \frac{2 m_1 m_2}{m_1 + m_2} \right) g.
\end{equation}

by subtituting Eqn. \eqref{eqn:mp-newton2-m1-sol-a} into Eqn. \eqref{eqn:mp-newton2-m1-sol} or \eqref{eqn:mp-newton2-m2-sol}.


## Exercises
1. What are an ideal string and an ideal pulley? Explain in brief the criteria.
2. If Eqn. \eqref{eqn:mp-w=mg} is for earth gravitational force near earth surface, find the expression for more general gravitational force, which also holds for object far from earth surface.
3. Prove Eqn. \eqref{eqn:mp-newton2-m1-sol-a} from Eqns. \eqref{eqn:mp-newton2-m1-sol} and \eqref{eqn:mp-newton2-m2-sol}.
4. Show how to obtain Eqn. \eqref{eqn:mp-newton2-m1-sol-T}.


## References
1. <a name="ref1"></a>Wikipedia contributors, "Relative velocity", Wikipedia, The Free Encyclopedia, 16 Jul 2020, 17:36 UTC, <https://en.wikipedia.org/w/index.php?oldid=968011332> [20201009].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-10-09-massless-pulley.md)
