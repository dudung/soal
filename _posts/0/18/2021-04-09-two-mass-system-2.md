---
layout: soal
author: viridi
title: "0188"
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
date: 2021-04-10 07:46:00 +07
permalink: /0188
src: https://github.com/dudung/soal/commits/master/_posts/0/18/2021-04-09-two-mass-system-2.md
ref: https://arxiv.org/abs/2001.02825
---
Sistem dua benda, yang dalam hal ini adalah dua koloni berbentuk bola dari genus Volvox, dapat disederhanakan menjadi dua buah partikel bermassa $m_1$, $m_2$, yang terletak pada posisi $\vec{r} _1$, $\vec{r} _2$. Dalam sistem koordinat pusat massa kedua posisi $\vec{r} _1$, $\vec{r} _2$ digantikan dengan $\vec{R}$, $\vec{r}$ yang menggambarkan posisi pusat massa sistem dan posisi relatif $m_2$ terhadap $m_1$.

![]({{site.baseurl}}/assets/img/0/18/0188.png)

Umumnya dapat digunakan sistem koordinat (SK) lab dan pusat massa atau center of mass (com)

Besaran | SK-Lab | SK-pm
:-: | :-: | :-:
$\vec{r}_1$ | $x_1$ | $x - \beta (r \sin\theta \cos\phi)$
| $y_1$ | $x - \beta (r \sin\theta \sin\phi)$
| $z_1$ | $x - \beta (r \cos\theta)$
$\vec{r}_2$ | $x_2$ | $x + (1-\beta) (r \sin\theta \cos\phi)$
| $y_2$ | $x + (1-\beta) (r \sin\theta \sin\phi)$
| $z_2$ | $x + (1-\beta) (r \cos\theta)$

dengan
$\vec{R} = x \ \hat{x} + y \ \hat{y} + z \ \hat{z}$,
$x = (m_1 x_1 + m_2 x_2) / (m_1 + m_2)$,
$y = (m_1 y_1 + m_2 y_2) / (m_1 + m_2)$,
$z = (m_1 z_1 + m_2 z_2) / (m_1 + m_2)$,
$\beta = m_2 / (m_1 + m_2)$, dan $(1 - \beta) = m_1 / (m_1 + m_2)$, serta $r = \sqrt{ (x_2 - x_1) ^2 + (y_2 - x_1) ^2 + (z_2 - z_1) ^2} $.

Bila sistem dua-massa di atas bergerak bergerak dengan mode translasi murni, pernyataan yang benar adalah

<ol type="A">
<li>$\dot{\theta} = 0$, $\dot{\phi} = 0$, $\dot{x} = 0$, $\dot{y} = 0$, $\dot{z} = 0$.
<li>$\dot{\theta} \ne 0$, $\dot{\phi} = 0$, $\dot{x} = 0$, $\dot{y} = 0$, $\dot{z} = 0$.
<li>$\dot{\theta} = 0$, $\dot{\phi} \ne 0$, $\dot{x} = 0$, $\dot{y} = 0$, $\dot{z} = 0$.
<li>$\dot{\theta} \ne 0$, $\dot{\phi} \ne 0$, $\dot{x} \ne 0$, $\dot{y} \ne 0$, $\dot{z} \ne 0$.
<li>$\dot{\theta} = 0$, $\dot{\phi} = 0$, $\dot{x} \ne 0$, $\dot{y} \ne 0$, $\dot{z} \ne 0$.

