---
layout: soal
author: viridi
title: "0285"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["heat conduction", "fourier's law", "steady state", "separation of variable", "harmonic", "exponential", "2-d", "fi3201", "2020-2"]
date: 2021-04-23 09:39:00 +07
permalink: /0285
src: https://github.com/dudung/soal/commits/master/_posts/0/28/2021-04-23-fourier-law-hc-fd-2d-5.md
ref: https://www.eng.auburn.edu/~dmckwski/mech7210/condbook.pdf#page=94
---
Terdapat segiempat yang memiiki distribusi temperatur $T(x, y)$ yang bersyarat batasnya adalah

\begin{equation}\label{eqn:0284-0}
T(0, y) = T(x, 0) = T(L, y) = T_1, \ \ \ \ T(x, H) = T_2,
\end{equation}

dengan $0 \le x \le L$ dan $0 \le y \le H$, sebagaimana diilustrasikan dalam gambar berikut.

![]({{site.baseurl}}/assets/img/0/28/0282.png)

Persamaan (perambatan) panas atau heat equation dalam 2-d yang semula

\begin{equation}\label{eqn:0284-1}
\frac{\partial T}{\partial t} = \alpha \left( \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} \right),
\end{equation}

akan menjadi

\begin{equation}\label{eqn:0284-2}
\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0,
\end{equation}

untuk keadaan tunak (steady state) dengan syarat batas pada Persamaan \eqref{eqn:0283-0}. Koefisien $\alpha$ dalam Persamaan \eqref{eqn:0284-1} adalah difusivitas termal yang tersusun atas konduktivitas termal $\kappa$, massa jenis $\rho$, dan kalor jenis $c$. Agar dapat menggunakan separasi variabel temperatur $T(x, y)$ diasumsikan dapat berbentuk

\begin{equation}\label{eqn:0284-3}
T(x, y) = X(x) Y(y).
\end{equation}

Substitusi Persamaan \eqref{eqn:0284-3} ke \eqref{eqn:0284-2} dan menyusun ulangnya akan dapat menghasilkan

\begin{equation}\label{eqn:0284-4}
-\frac1X \frac{d^2 X}{dx^2} = \frac1Y \frac{d^2 Y}{dy^2}.
\end{equation}

Salah satu cara termudah untuk mencari solusi dari Persamaan \eqref{eqn:0284-4}, dan masih memberikan hasil yang bermakna, adalah dengan

A | memisalkan ruas kiri $f(z)$ dan ruas kanan $g(z), dengan z = z(x, y)$.
B | memisalkan ruas kiri $f(x, y)$ dan ruas kanan $g(x, y)$.
C | memisalkan ruas kiri $f(x)$ dan ruas kanan $g(y)$.
D | memisalkan kedua ruas bernilai nol.
E | memisalkan kedua ruas bernilai konstanta yang sama, misalnya $\beta^2$.

{% comment %}
http://www.math.utah.edu/~gustafso/s2019/2270/projects-2019/submitted/kristenStewart/Determining%20Temperature%20Distribution%20of%20a%202D%20Heated%20Plate.pdf
{% endcomment %}