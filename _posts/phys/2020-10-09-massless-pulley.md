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


## References
1. <a name="ref1"></a>Wikipedia contributors, "Relative velocity", Wikipedia, The Free Encyclopedia, 16 Jul 2020, 17:36 UTC, <https://en.wikipedia.org/w/index.php?oldid=968011332> [20201009].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-10-09-massless-pulley.md)
