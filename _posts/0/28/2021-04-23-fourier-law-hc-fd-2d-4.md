---
layout: soal
author: viridi
title: "0284"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["heat conduction", "fourier's law", "steady state", "diffusivity", "2-d", "fi3201", "2020-2"]
date: 2021-04-23 09:20:00 +07
permalink: /0284
src: https://github.com/dudung/soal/commits/master/_posts/0/28/2021-04-22-fourier-law-hc-fd-2d-4.md
ref: https://www.eng.auburn.edu/~dmckwski/mech7210/condbook.pdf#page=94
---
Terdapat segiempat yang memiiki distribusi temperatur $T(x, y)$ yang bersyarat batasnya adalah

\begin{equation}\label{eqn:0283-0}
T(0, y) = T(x, 0) = T(L, y) = T_1, \ \ \ \ T(x, H) = T_2,
\end{equation}

dengan $0 \le x \le L$ dan $0 \le y \le H$, sebagaimana diilustrasikan dalam gambar berikut.

![]({{site.baseurl}}/assets/img/0/28/0282.png)

Persamaan (perambatan) panas atau heat equation dalam 2-d yang semula

\begin{equation}\label{eqn:0283-1}
\frac{\partial T}{\partial t} = \alpha \left( \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} \right),
\end{equation}

akan menjadi

\begin{equation}\label{eqn:0283-2}
\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0,
\end{equation}

untuk keadaan tunak (steady state) dengan syarat batas pada Persamaan \eqref{eqn:0283-0}. Koefisien $\alpha$ dalam Persamaan \eqref{eqn:0283-1} adalah difusivitas termal yang tersusun atas konduktivitas termal $\kappa$, massa jenis $\rho$, dan kalor jenis $c$. Agar dapat menggunakan separasi variabel temperatur $T(x, y)$ diasumsikan dapat berbentuk

\begin{equation}\label{eqn:0283-3}
T(x, y) = X(x) Y(y),
\end{equation}

yang akan membuat Persamaan \eqref{eqn:0283-2} dapat dituliskan menjadi

A | $\displaystyle -\frac1X \frac{d^2 X}{dx^2} = \frac1Y \frac{d^2 Y}{dy^2}$.
B | $\displaystyle \frac1X \frac{d^2 X}{dx^2} = \frac1Y \frac{d^2 Y}{dy^2}$.
C | $\displaystyle \frac1X \frac{d^2 X}{dx^2} - \frac1Y \frac{d^2 Y}{dy^2}$ = 0.
D | $\displaystyle Y \frac{d^2 X}{dx^2} - X \frac{d^2 Y}{dy^2}$ = 0.
E | bukan salah satu jawaban di atas.

{% comment %}
http://www.math.utah.edu/~gustafso/s2019/2270/projects-2019/submitted/kristenStewart/Determining%20Temperature%20Distribution%20of%20a%202D%20Heated%20Plate.pdf
{% endcomment %}
