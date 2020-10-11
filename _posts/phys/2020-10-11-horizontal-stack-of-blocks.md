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
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:10px
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
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:10px
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
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:10px
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
