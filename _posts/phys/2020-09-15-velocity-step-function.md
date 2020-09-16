---
layout: post
author: viridi
title: velocity step function
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["topics"]
date: 2020-09-15 22:08:00 +07
permalink: /physics/velocity-step-function
---
There is a type of linear motion (LM) composed of some [uniform linear motions](uniform-linear-motion) (ULMs), which is different than the nonuniform linear motion (NULM). Velocity function $v(t)$ of this type of LM is simply a step function [[1](#ref1)]. Or it can said that each ULM is a boxcar function [[2](#ref2)].


## Boxcar function
A boxcar function has only non-zero value $A$ over a single interval, which can be described with

\begin{equation}
\label{eqn:vsf-boxcar-function}
{\rm boxcar}(x) =
\left\\{
\begin{array}{lc}
A, & a \le x < b, \newline
0, & x < a \cup b \le x,
\end{array}
\right.
\end{equation}

where the interval has lower boundary $a$ and upper boundary $b$.

<oo>
svg 400 200 #fafafa fig:vsf-boxchar|A boxchar function $f_{\rm BC}(x)$ with lower boundary $a$ and upper boundary $b$.

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 20 380 180 40 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 20 180 380 180
arrow 20 180 20 20
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 20 180 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 386 183 x
text 18 14 f
text 5 65 A
text 135 197 a
text 255 197 b
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 24 16 BC

style lc:#f44 ls:6-4-2-4 lw:1 lo:1
line 20 60 380 60
line 140 180 140 60
line 260 180 260 60
style lc:#f00 ls:0 lw:2 lo:1
line 140 60 260 60
style lc:#f00 ls:0 lw:1 lo:1 fc:#f00
circle 140 60 4
style lc:#f00 ls:0 lw:1 lo:1 fc:#fff
circle 260 60 4
</oo>

Solid red circle in Fig. <a href="#fig:fig:vsf-boxchar">1</a> means that $f_{\rm BC}$ has value of $A$ at that position, while empty or white circle means that $f _{\rm BC}$ does not have value of $A$.


## Step function
Function composed of several functions boxcar $f_{\rm BC}(x)$ is a step function $f_{\rm S}(x)$. Or we can say that a step function $f_{\rm S}(x)$ is a finite linear combination of boxcar functions $f_{\rm BC}(x)$ of intervals, which is simply

\begin{equation}
\label{eqn:vsf-step-function}
{\rm step}(x) = \sum_{i = 1}^N f_{ {\rm BC}, i}(x),
\end{equation}

where each $f_{ {\rm BC}, i}(x)$ has its own values of $A_i$, $a_i$, and $b_i$.


## Exercises
1. Suppose that there are two boxcar function with $A_1 = 2$, $a_1 = 1$, $b_1 = 2$ and $A_1 = -2$, $a_1 = 2$, $b_1 = 3$, 


## References
1. <a name="ref1"></a>Wikipedia contributors, "Step function", Wikipedia, The Free Encyclopedia, 21 Apr 2020, 04:27 UTC, <https://en.wikipedia.org/w/index.php?oldid=952221804> [20200915].
2. <a name="ref2"></a>Wikipedia contributors, "Boxcar function", Wikipedia, The Free Encyclopedia, 1 Aug 2020, 03:12 UTC, <https://en.wikipedia.org/w/index.php?oldid=852898903> [20200915].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-09-15-velocity-step-function.md)
