---
layout: post
author: viridi
title: horizontal stack of blocks
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["block"]
date: 2020-10-10 04:45:00 +07
permalink: /physics/horizontal-stack-of-blocks
---
Stack of blocks in horizontal arrangement pushed by a horizontal external force is an interested topic to discussed, e.g. for two blocks [[1](#ref1), [2](#ref2), [3](#ref3)] and three blocks [[4](#ref4), [5](#ref5), [6](#ref6), [7](#ref7), [8](#ref8), [9](#ref9)] moving on a frictionless floor or on a floor with friction [[10](#ref10)].


## System of four blocks
Since system of two and three blocks are already in common, we will discuss a system of four blocks in order to give a more general description about a horizontal stack of blocks system moving on a frictionless horizontal surface due to a horizontal external force.

<oo>
svg 400 120 #fafafa fig:hsb-4-m|On a frictionless horizontal surface four blocks pushed by a horizontal external force is moving from left to right.

# Horizontal floor
style lc:#000 ls:0 lw:2 lo:1
line 20 90 380 90

# Red block m1 = 3 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#faa fo:1
rect 100 30 60 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 65 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 132 70 1

# Green block m2 = 1 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#afa fo:1
rect 160 50 40 40
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 170 75 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 182 80 2

# Blue block m3 = 4 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#aaf fo:1
rect 200 20 70 70
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 230 60 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 242 65 3

# Yellow block m4 = 2 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#ffa fo:1
rect 270 40 50 50
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 285 70 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 297 75 4

# External force \vec{F}
style lc:#f88 ls:0 lw:3 lo:1 fc:#f88 fo:1
arrow 20 60 100 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 50 45 F
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 58 50 ext
</oo>

System of four bloks with mass $m_1$, $m_2$, $m_3$, and $m_4$, pushed by a horizontal external force $F$, moving on a frictionless horizontal surface $\mu_k = 0$, is given in Fig. <a href="#fig:hsb-4-m">1</a>.


## Free-body diagram
For each block we can draw a free-body diagram. Suppose that there an external force $F_{ext} = 10 \ \rm N$ and $m_1 = 3 \ \rm kg$, $m_2 = 1 \ \rm kg$, $m_3 = 4 \ \rm kg$, $m_4 = 2 \ \rm kg$.

<oo>
svg 400 130 #fafafa fig:hsb-4-m-fbd-m1|Free-body diagram of $m_1 = 3 \ \rm kg$.

# Red block m1 = 3 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#faa fo:1
rect 100 30 60 60

style lc:#f00 ls:0 lw:2 lo:1 fc:#f00 fo:1
arrow 130 60 130 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 55 w
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 132 60 1

style lc:#f00 ls:0 lw:2 lo:1 fc:#f00 fo:1
arrow 140 120 140 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 150 115 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 162 120 1

# External force F
style lc:#f88 ls:0 lw:3 lo:1 fc:#f88 fo:1
arrow 20 60 100 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 50 45 F
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 58 50 ext

# Normal force N12
style lc:#f88 ls:0 lw:3 lo:1 fc:#f88 fo:1
arrow 216 60 160 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 180 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 192 50 12
</oo>

<oo>
svg 400 130 #fafafa fig:hsb-4-m-fbd-m2|Free-body diagram of $m_2 = 1 \ \rm kg$.

# Green block m2 = 1 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#afa fo:1
rect 160 50 40 40

style lc:#0f0 ls:0 lw:2 lo:1 fc:#0f0 fo:1
arrow 180 70 180 80
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 170 65 w
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 182 70 2

style lc:#0f0 ls:0 lw:2 lo:1 fc:#0f0 fo:1
arrow 190 100 190 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 200 115 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 212 120 2

# Normal force N21
style lc:#8f8 ls:0 lw:3 lo:1 fc:#8f8 fo:1
arrow 104 60 160 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 132 50 21

# Normal force N23
style lc:#8f8 ls:0 lw:3 lo:1 fc:#8f8 fo:1
arrow 248 60 200 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 210 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 222 50 23
</oo>

<oo>
svg 400 130 #fafafa fig:hsb-4-m-fbd-m3|Free-body diagram of $m_3 = 4 \ \rm kg$.

# Blue block m3 = 4 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#aaf fo:1
rect 200 20 70 70

style lc:#00f ls:0 lw:2 lo:1 fc:#00f fo:1
arrow 235 55 235 95
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 230 50 w
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 242 55 3

style lc:#00f ls:0 lw:2 lo:1 fc:#00f fo:1
arrow 250 130 250 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 255 120 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 267 125 3

# Normal force N32
style lc:#88f ls:0 lw:3 lo:1 fc:#88f fo:1
arrow 152 60 200 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 170 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 182 50 32

# Normal force N34
style lc:#88f ls:0 lw:3 lo:1 fc:#88f fo:1
arrow 286 60 270 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 280 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 292 50 34
</oo>

<oo>
svg 400 130 #fafafa fig:hsb-4-m-fbd-m4|Free-body diagram of $m_4 = 2 \ \rm kg$.

# Yellow block m4 = 2 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#ffa fo:1
rect 270 40 50 50

style lc:#cc0 ls:0 lw:2 lo:1 fc:#cc0 fo:1
arrow 295 65 295 85
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 285 60 w
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 297 65 4

style lc:#cc0 ls:0 lw:2 lo:1 fc:#cc0 fo:1
arrow 305 110 305 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 310 120 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 322 125 4

# Normal force N43
style lc:#dd8 ls:0 lw:3 lo:1 fc:#dd8 fo:1
arrow 254 60 270 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 240 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 252 50 43
</oo>

Beside free-body diagram for each block in Figs. Fig. <a href="#fig:hsb-4-m-fbd-m1">2</a>, <a href="#fig:hsb-4-m-fbd-m2">3</a>, <a href="#fig:hsb-4-m-fbd-m3">4</a>, and <a href="#fig:hsb-4-m-fbd-m4">5</a>, we can also have a free-body diagram for the whole system.

<oo>
svg 400 150 #fafafa fig:hsb-4-m-fbd-m1234|Free-body diagram for the $m = m_1 + m_2 + m_3 + m_4 = 10 \ \rm kg$.

# Red block m1 = 3 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#faa fo:1
rect 100 30 60 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 65 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 132 70 1

# Green block m2 = 1 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#afa fo:1
rect 160 50 40 40
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 170 75 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 182 80 2

# Blue block m3 = 4 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#aaf fo:1
rect 200 20 70 70
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 230 60 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 242 65 3

# Yellow block m4 = 2 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#ffa fo:1
rect 270 40 50 50
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 285 70 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 297 75 4

# External force \vec{F}
style lc:#f88 ls:0 lw:3 lo:1 fc:#f88 fo:1
arrow 20 60 100 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 50 45 F
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 58 50 ext

# Whole block m1 + m2 + m3 + m4 = 10 kg
style lc:#f00 ls:4-4 lw:2 lo:1 fc:#f00 fo:0.2
rect 100 20 220 70
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 65 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 132 70 1

style lc:#a0f ls:0 lw:3 lo:1 fc:#a0f fo:1
arrow 215 55 215 115
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 210 50 w

style lc:#a0f ls:0 lw:3 lo:1 fc:#a0f fo:1
arrow 225 150 225 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 235 140 N
</oo>

Fig. <a href="#fig:hsb-4-m-fbd-m1234">6</a> can only be used when the whole system is moving as a unit and all block have the same acceleration.


## Newton's laws of motion
We will use 1st, 2nd, and 3rd Newton's laws of (linear) motion to solve the problem. The laws will be abbreviated as Nl-I, Nl-II, Nl-III.

### Block $m_1$
Let's see again the free-body diagram.

<oo>
svg 400 130 #fafafa fig:hsb-4-m-fbd-m1-nl|Free-body diagram of $m_1 = 3 \ \rm kg$.

# Red block m1 = 3 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#faa fo:1
rect 100 30 60 60

style lc:#f00 ls:0 lw:2 lo:1 fc:#f00 fo:1
arrow 130 60 130 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 55 w
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 132 60 1

style lc:#f00 ls:0 lw:2 lo:1 fc:#f00 fo:1
arrow 140 120 140 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 150 115 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 162 120 1

# External force F
style lc:#f88 ls:0 lw:3 lo:1 fc:#f88 fo:1
arrow 20 60 100 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 50 45 F
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 58 50 ext

# Normal force N12
style lc:#f88 ls:0 lw:3 lo:1 fc:#f88 fo:1
arrow 216 60 160 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 180 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 192 50 12
</oo>

Since $m_1$ does not move in $y$-direction, Nl-I will give

\begin{equation}
\label{eqn:hsb-m1-SFy}
\sum F_y = 0 \Rightarrow N_1 - w_1 = 0 \Rightarrow N_1 = w_1 = m_1 g.
\end{equation}

It moves with acceleration in $x$-direction, then Nl-II governs that

\begin{equation}
\label{eqn:hsb-m1-SFx}
\sum F_x = m_1 a_{1x} \Rightarrow F_{\rm ext} - N_{12} = m_1 a_{1x}.
\end{equation}

### Block $m_2$
Let's see again the free-body diagram.

<oo>
svg 400 130 #fafafa fig:hsb-4-m-fbd-m2-nl|Free-body diagram of $m_2 = 1 \ \rm kg$.

# Green block m2 = 1 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#afa fo:1
rect 160 50 40 40

style lc:#0f0 ls:0 lw:2 lo:1 fc:#0f0 fo:1
arrow 180 70 180 80
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 170 65 w
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 182 70 2

style lc:#0f0 ls:0 lw:2 lo:1 fc:#0f0 fo:1
arrow 190 100 190 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 200 115 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 212 120 2

# Normal force N21
style lc:#8f8 ls:0 lw:3 lo:1 fc:#8f8 fo:1
arrow 104 60 160 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 132 50 21

# Normal force N23
style lc:#8f8 ls:0 lw:3 lo:1 fc:#8f8 fo:1
arrow 248 60 200 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 210 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 222 50 23
</oo>

Since $m_2$ does not move in $y$-direction, Nl-I will give

\begin{equation}
\label{eqn:hsb-m2-SFy}
\sum F_y = 0 \Rightarrow N_2 - w_2 = 0 \Rightarrow N_2 = w_2 = m_2 g.
\end{equation}

It moves with acceleration in $x$-direction, then Nl-II governs that

\begin{equation}
\label{eqn:hsb-m2-SFx}
\sum F_x = m_2 a_{2x} \Rightarrow N_{21} - N_{23} = m_2 a_{2x}.
\end{equation}

### Block $m_3$
Let's see again the free-body diagram.

<oo>
svg 400 130 #fafafa fig:hsb-4-m-fbd-m3-nl|Free-body diagram of $m_3 = 4 \ \rm kg$.

# Blue block m3 = 4 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#aaf fo:1
rect 200 20 70 70

style lc:#00f ls:0 lw:2 lo:1 fc:#00f fo:1
arrow 235 55 235 95
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 230 50 w
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 242 55 3

style lc:#00f ls:0 lw:2 lo:1 fc:#00f fo:1
arrow 250 130 250 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 255 120 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 267 125 3

# Normal force N32
style lc:#88f ls:0 lw:3 lo:1 fc:#88f fo:1
arrow 152 60 200 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 170 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 182 50 32

# Normal force N34
style lc:#88f ls:0 lw:3 lo:1 fc:#88f fo:1
arrow 286 60 270 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 280 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 292 50 34
</oo>

Since $m_3$ does not move in $y$-direction, Nl-I will give

\begin{equation}
\label{eqn:hsb-m3-SFy}
\sum F_y = 0 \Rightarrow N_3 - w_3 = 0 \Rightarrow N_3 = w_3 = m_3 g.
\end{equation}

It moves with acceleration in $x$-direction, then Nl-II governs that

\begin{equation}
\label{eqn:hsb-m3-SFx}
\sum F_x = m_3 a_{3x} \Rightarrow N_{32} - N_{34} = m_3 a_{3x}.
\end{equation}

### Block $m_4$
Let's see again the free-body diagram.

<oo>
svg 400 130 #fafafa fig:hsb-4-m-fbd-m4-nl|Free-body diagram of $m_4 = 2 \ \rm kg$.

# Yellow block m4 = 2 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#ffa fo:1
rect 270 40 50 50

style lc:#cc0 ls:0 lw:2 lo:1 fc:#cc0 fo:1
arrow 295 65 295 85
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 285 60 w
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 297 65 4

style lc:#cc0 ls:0 lw:2 lo:1 fc:#cc0 fo:1
arrow 305 110 305 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 310 120 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 322 125 4

# Normal force N43
style lc:#dd8 ls:0 lw:3 lo:1 fc:#dd8 fo:1
arrow 254 60 270 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 240 45 N
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 252 50 43
</oo>

Since $m_3$ does not move in $y$-direction, Nl-I will give

\begin{equation}
\label{eqn:hsb-m4SFy}
\sum F_y = 0 \Rightarrow N_4 - w_4 = 0 \Rightarrow N_4 = w_4 = m_4 g.
\end{equation}

It moves with acceleration in $x$-direction, then Nl-II governs that

\begin{equation}
\label{eqn:hsb-m4-SFx}
\sum F_x = m_4 a_{4x} \Rightarrow N_{43} = m_4 a_{4x}.
\end{equation}

### Whole block $m = m_1 + m_2 + m_3 + m_4$
Let's see again the free-body diagram.

<oo>
svg 400 150 #fafafa fig:hsb-4-m-fbd-m1234-nl|Free-body diagram for the $m = m_1 + m_2 + m_3 + m_4 = 10 \ \rm kg$.

# Red block m1 = 3 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#faa fo:1
rect 100 30 60 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 65 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 132 70 1

# Green block m2 = 1 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#afa fo:1
rect 160 50 40 40
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 170 75 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 182 80 2

# Blue block m3 = 4 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#aaf fo:1
rect 200 20 70 70
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 230 60 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 242 65 3

# Yellow block m4 = 2 kg
style lc:#000 ls:0 lw:2 lo:1 fc:#ffa fo:1
rect 270 40 50 50
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 285 70 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 297 75 4

# External force \vec{F}
style lc:#f88 ls:0 lw:3 lo:1 fc:#f88 fo:1
arrow 20 60 100 60
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 50 45 F
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 58 50 ext

# Whole block m1 + m2 + m3 + m4 = 10 kg
style lc:#f00 ls:4-4 lw:2 lo:1 fc:#f00 fo:0.2
rect 100 20 220 70
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 120 65 m
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 132 70 1

style lc:#a0f ls:0 lw:3 lo:1 fc:#a0f fo:1
arrow 215 55 215 115
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 210 50 w

style lc:#a0f ls:0 lw:3 lo:1 fc:#a0f fo:1
arrow 225 150 225 90
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 235 140 N
</oo>

Since the whole system does not move in $y$-direction, Nl-I will give

\begin{equation}
\label{eqn:hsb-m1234SFy}
\sum F_y = 0 \Rightarrow N - w = 0 \Rightarrow N = w = m g.
\end{equation}

It moves with acceleration in $x$-direction, then Nl-II governs that

\begin{equation}
\label{eqn:hsb-m1234-SFx}
\sum F_x = m a_x \Rightarrow F_{\rm ext} = m a_x.
\end{equation}

And as whole system

\begin{equation}
\label{eqn:hsb-m1234-m}
m = m_1 + m_2 + m_3 + m_4
\end{equation}

and all are moving together

\begin{equation}
\label{eqn:hsb-m1234-a}
a_{1x} = a_{2x} = a_{3x} = a_{4x} = a_x.
\end{equation}

### Between blocks $m_1$ and $m_2$
According to Nl-III we can have

\begin{equation}
\label{eqn:hsb-m1-m2}
N_{21} = N_{12}.
\end{equation}

### Between blocks $m_2$ and $m_3$
According to Nl-III we can have

\begin{equation}
\label{eqn:hsb-m2-m3}
N_{32} = N_{23}.
\end{equation}

### Between blocks $m_3$ and $m_4$
According to Nl-III we can have

\begin{equation}
\label{eqn:hsb-m3-m4}
N_{43} = N_{34}.
\end{equation}


## Solution

Sum of Eqns. \eqref{eqn:hsb-m1-SFx}, \eqref{eqn:hsb-m2-SFx}, \eqref{eqn:hsb-m3-SFx}, and \eqref{eqn:hsb-m4-SFx} will produce

\begin{equation}
\label{eqn:hsb-SFx+1+2+3+4}
\begin{array}{rcl}
F_{\rm ext} - N_{12} & = & m_1 a_{1x} \newline
N_{21} - N_{23} & = & m_2 a_{2x} \newline
N_{32} - N_{34} & = & m_3 a_{3x} \newline
N_{43} & = & m_4 a_{4x} \newline
------------ & -- & --------- \newline
F_{\rm ext} & = & m_1 a_{1x} + m_2 a_{2x} + m_3 a_{3x} + m_4 a_{4x} \end{array}
\end{equation}

and subsitute Eqn. \eqref{eqn:hsb-m1234-a} into Eqn. \eqref{eqn:hsb-SFx+1+2+3+4}

\begin{equation}
\label{eqn:hsb-SFx+1+2+3+4-a}
a_x = \frac{F_{\rm ext}}{m_1 + m_2 + m_3 + m_4}.
\end{equation}

### Normal force $N_{12}$
Substitute Eqn. \eqref{eqn:hsb-SFx+1+2+3+4-a} into \eqref{eqn:hsb-m1-SFx} will give

\begin{equation}
\label{eqn:hsb-m1-SFx-N12}
N_{12} = F_{\rm ext} - m_1 a_x.
\end{equation}

### Normal force $N_{23}$
Substitute Eqn. \eqref{eqn:hsb-SFx+1+2+3+4-a} into \eqref{eqn:hsb-m2-SFx} will give

\begin{equation}
\label{eqn:hsb-m2-SFx-N23}
N_{23} = N_{21} - m_2 a_x,
\end{equation}

where $N_{21}$ is obtained from Eqn. \eqref{eqn:hsb-m1-SFx-N12} using Eqn. \eqref{eqn:hsb-m1-m2}.

### Normal force $N_{34}$
Substitute Eqn. \eqref{eqn:hsb-SFx+1+2+3+4-a} into \eqref{eqn:hsb-m3-SFx} will give

\begin{equation}
\label{eqn:hsb-m3-SFx-N34}
N_{34} = N_{32} - m_3 a_x,
\end{equation}

where $N_{32}$ is obtained from Eqn. \eqref{eqn:hsb-m2-SFx-N23} using Eqn. \eqref{eqn:hsb-m2-m3}.

### Normal force $N_{43}$
Substitute Eqn. \eqref{eqn:hsb-SFx+1+2+3+4-a} into \eqref{eqn:hsb-m4-SFx} will give

\begin{equation}
\label{eqn:hsb-m4-SFx-N43}
N_{43} = m_4 a_x.
\end{equation}

Eqn. \eqref{eqn:hsb-m4-SFx-N43} can also be obtained from Eqn. \eqref{eqn:hsb-m3-SFx-N34} using Eqn. \eqref{eqn:hsb-m3-m4}.


## Floor with friction
What will hapen when there is friction between all blocks and the floor? Suppose that between block $i$ and the floor the coefficient of kinetic friction is $\mu_{ki}$ with $i = 1, 2, 3, 4$. Then Eqn. \eqref{eqn:hsb-m1-SFx} will become

\begin{equation}
\label{eqn:hsb-m1-SFx-muk}
\sum F_x = m_1 a_{1x} \Rightarrow F_{\rm ext} - \mu_{k1} N_1 - N_{12} = m_1 a_{1x},
\end{equation}

Eqn. \eqref{eqn:hsb-m2-SFx} will become

\begin{equation}
\label{eqn:hsb-m2-SFx-muk}
\sum F_x = m_2 a_{2x} \Rightarrow N_{21} - \mu_{k2} N_2 - N_{23} = m_2 a_{2x}.
\end{equation}

Eqn. \eqref{eqn:hsb-m3-SFx} will become

\begin{equation}
\label{eqn:hsb-m3-SFx-muk}
\sum F_x = m_3 a_{3x} \Rightarrow N_{32} - \mu_{k3} N_3 - N_{34} = m_3 a_{3x}.
\end{equation}

and Eqn. \eqref{eqn:hsb-m4-SFx} will become

\begin{equation}
\label{eqn:hsb-m4-SFx-muk}
\sum F_x = m_4 a_{4x} \Rightarrow N_{43} - \mu_{k4} N_4 = m_4 a_{4x}.
\end{equation}

Using Eqns. \eqref{eqn:hsb-m1-SFx-muk}, \eqref{eqn:hsb-m2-SFx-muk}, \eqref{eqn:hsb-m3-SFx-muk}, \eqref{eqn:hsb-m4-SFx-muk} in Eqn. \eqref{eqn:hsb-SFx+1+2+3+4} will produce the solution.


## Quiz
Suppose there a system as in Fig. <a href="#fig:hsb-4-m">1</a> with $m_1 = 4 \ \rm kg$, $m_2 = 3 \ \rm kg$, $m_3 = 2 \ \rm kg$, $m_4 = 3 \ \rm kg$, and external force $F_{\rm ext} = 24 \ \rm N$.
1. Find $a_x$, $N_{12}$, $N_{21}$,  $N_{23}$,  $N_{32}$, $N_{34}$, and  $N_{43}$ if the floor is frictionless.
2. Find $a_x$, $N_{12}$, $N_{21}$,  $N_{23}$,  $N_{32}$, $N_{34}$, and  $N_{43}$ if there is friction between the floor and all blocks with $\mu_k = 0.1$.

+ [Submit answer](https://forms.office.com/Pages/ResponsePage.aspx?id=gxFu22VMXECCznzVP6bp3NGUp4ijN01Ks-VZMpTE-hpUNUUxRFBGUlVTR1ZRTlAxSzFLVFAwVzVaUi4u)

## References
1. <a name="ref1"></a>-, "A single horizontal force F...", toppr, url <https://www.toppr.com/ask/question/a-single-horizontal-force-f-is-applied-to-a-blockof-mass-displaystyle-m> [20201011].
2. <a name="ref2"></a>-, "A Force F Of 14N Acts On Two Blocks On A Frictionless...", Chegg Study,  url <https://www.chegg.com/homework-help/questions-and-answers/force-f-14n-acts-two-blocks-frictionless-surface-figure-1--part-acceleration-system-expres-q5157730> [20201011].
3. <a name="ref3"></a>Saif Rayyan, "Example 1: Pushing two boxes along a horizontal surface", Integrated Learning Environment for Mechanics, 14 Dec 2011, 21:30, url <https://scripts.mit.edu/~srayyan/PERwiki/index.php?title=Module_4_--_Objects_Constrained_to_Move_with_Equal_Acceleration> [20201011].
4. <a name="ref4"></a>Pablo, "Force exerted on three blocks", Physics StackExchange, 27 Nov 16, url <https://physics.stackexchange.com/questions/295185> [20201011].
5. <a name="ref5"></a>-, "Suppose Three Blocks Are In Contact With One An...", Chegg Study, url <https://www.chegg.com/homework-help/questions-and-answers/suppose-three-blocks-contact-one-another-frictionless-horizontal-surface-horizontal-force--q9708499> [20201011].
6. <a name="ref6"></a>-, "Three blocks on a frictionless horizontal surface in contact with each other, as shown in the...", Study.com, url <https://study.com/academy/answer/three-blocks-on-a-frictionless-horizontal-surface-in-contact-with-each-other-as-shown-in-the-figure-a-force-vec-f-is-applied-to-block-a-mass-ma-if-ma-mb-mc-18-0-kg-and-f-90-0-n-determine-a.html> [20201011].
7. <a name="ref7"></a>-, "Three blocks of masses 1 kg, 2kg and 3 kg are placed in contact with each other on a horizontal frictionless surface as shown in figure. A force of 12 N is applied as shown in figure.", Brainly, 8 Sept 2018, url <https://brainly.in/question/5567463> [20201011].
8. <a name="ref8"></a>Dale E. Gary, "Physics 111 Homework Solution, week 4, chapter 5, sec 1-7", New Jersey's Science & Technology University, 13 Feb 2013, p. 13, url <https://web.njit.edu/~gary/111/assets/HW4_sol.pdf> [20201011].
9. <a name="ref9"></a>-, " A)Determine The Net Force On Block A. Assume T...", Chegg Study, url <https://www.chegg.com/homework-help/questions-and-answers/determine-net-force-block--assume-possitive-x-axis-directed-right-express-answer-variables-q3710740> [20201011].
10. <a name="ref10"></a>The Organic Chemistry Tutor, "Contact Force Between Blocks With Kinetic Friction - Physics Problems & Examples", YouTube, 24 Oct 2016, url <https://www.youtube.com/watch?v=hTSzF4TVmfM> [20201011].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-10-11-horizontal-stack-of-blocks.md)
