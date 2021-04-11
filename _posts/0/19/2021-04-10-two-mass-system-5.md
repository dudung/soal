---
layout: soal
author: viridi
title: "0191"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["python", "plot", "mathplotlit", "numpy", "two-mass", "volvox", "ellipse", "fi3201", "2020-2"]
date: 2021-04-11 17:06:00 +07
permalink: /0191
src: https://github.com/dudung/soal/commits/master/_posts/0/19/2021-04-10-two-mass-system-5.md
ref: https://arxiv.org/abs/2001.02825
---
Sistem dua benda, yang dalam hal ini adalah dua koloni berbentuk bola dari genus Volvox, dapat disederhanakan menjadi dua buah partikel bermassa $m_1$, $m_2$, yang terletak pada posisi $\vec{r} _1$, $\vec{r} _2$. Dalam sistem koordinat pusat massa kedua posisi $\vec{r} _1$, $\vec{r} _2$ digantikan dengan $\vec{R}(X, Y, Z)$, $\vec{r}(r, \theta, \phi)$ yang menggambarkan posisi pusat massa sistem dan posisi relatif $m_2$ terhadap $m_1$. Sistem dua-massa dapat bergerak denga mode translasi (T), spin (S), dan roll (R), atau paduan dari dua atau ketiganya.

Mode | Gerak 
:-: | :-:
T | ![]({{site.baseurl}}/assets/img/0/19/0191a.png)
S | ![]({{site.baseurl}}/assets/img/0/19/0191b.png)
R | ![]({{site.baseurl}}/assets/img/0/19/0191c.png)

Dengan menggunakan sistem dua benda ini di mana nilai $\dot{r} = 0$ atau yang berarti jarak antar kedua koloni Volvox selalu bernilai sama, akan terapat lima variabel bebas yang perlu diberi nilai tertentu agar dapat berada pada mode gerak T, R, S ataupun T+R, T+S, R+S, T+R+S. Beberapa model disajikan dalam tabel berikut ini.

Mode | $\dot{X}$ | $\dot{Y}$ | $\dot{Z}$ | $\dot{\theta}$ | $\dot{\phi}$
:-: | :-: | :-: | :-: | :-: | :-:
I   | $\ne 0$ | $\ne 0$ | $\ne 0$ | $= 0$ | $= 0$  
II  | $= 0$ | $= 0$ | $= 0$ | $\ne 0$ | $= 0$
III | $= 0$ | $= 0$ | $= 0$ | $= 0$ | $\ne 0$
IV  | $= 0$ | $= 0$ | $= 0$ | $\ne 0$ | $\ne 0$
V   | $\ne 0$ | $\ne 0$ | $\ne 0$ | $\ne 0$ | $= 0$
VI  | $\ne 0$ | $\ne 0$ | $\ne 0$ | $= 0$ | $\ne 0$
VII | $\ne 0$ | $\ne 0$ | $\ne 0$ | $\ne 0$ | $\ne 0$

Mode T diberikan oleh mode

<ol type="A">
<li>I.
<li>II.
<li>III.
<li>IV.
<li>V.
