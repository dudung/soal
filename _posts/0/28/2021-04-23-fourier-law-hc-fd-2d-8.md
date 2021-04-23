---
layout: soal
author: viridi
title: "0288"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["spatial discretization", "grid", "2-d", "fi3201", "2020-2"]
date: 2021-04-23 18:36:00 +07
permalink: /0288
src: https://github.com/dudung/soal/commits/master/_posts/0/28/2021-04-23-fourier-law-hc-fd-2d-8.md
ref: https://www.eng.auburn.edu/~dmckwski/mech7210/condbook.pdf#page=94
---
Terdapat segiempat dengan panjang $L$ dan tinggi $H$ yang keempat titik sudutnya memiliki koordinat $(0, 0)$, $(L, 0)$, $(L, H)$, dan $(0, H)$, seperti diilustrasikan dalam gambar bagian kiri berikut.

![]({{site.baseurl}}/assets/img/0/28/0288a.png) | ![]({{site.baseurl}}/assets/img/0/28/0288b.png)

Dalam gambar sebelumnya, titik $(x, y)$ pada bagian kiri diwakilkan dengan $(x_i, x_j)$ pada bagian kanan. Dengan diskritisasi ruang pada arah $x$ dan $y$ masing-masing adalah $\Delta x$ dan $\Delta y$ dapat diperoleh bahwa

\begin{equation}\label{eqn:0288-0}
x_i = i \Delta x, \ \ \ \ i = 0, \dots, N
\end{equation}

dan

\begin{equation}\label{eqn:0288-1}
y_j = j \Delta y, \ \ \ \ j = 0, \dots, M.
\end{equation}

Perumusan $\Delta x$ dan $\Delta y$ dalam gambar sebelumnya adalah

A | $\displaystyle \frac{L}{N+1}$ dan $\displaystyle \frac{H}{M+1}$
B | $\displaystyle \frac{L}{N-1}$ dan $\displaystyle \frac{H}{M-1}$
C | $\displaystyle \frac{L}{N-1}$ dan $\displaystyle \frac{H}{M}$
D | $\displaystyle \frac{L}{N}$ dan $\displaystyle \frac{H}{M-1}$
E | $\displaystyle \frac{L}{N}$ dan $\displaystyle \frac{H}{M}$
