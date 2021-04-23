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
date: 2021-04-23 09:48:00 +07
permalink: /0285
src: https://github.com/dudung/soal/commits/master/_posts/0/28/2021-04-23-fourier-law-hc-fd-2d-5.md
ref: https://www.eng.auburn.edu/~dmckwski/mech7210/condbook.pdf#page=94
---
Terdapat segiempat yang memiiki distribusi temperatur $T(x, y)$ yang bersyarat batasnya adalah

\begin{equation}\label{eqn:0285-0}
T(0, y) = T(x, 0) = T(L, y) = T_1, \ \ \ \ T(x, H) = T_2,
\end{equation}

dengan $0 \le x \le L$ dan $0 \le y \le H$, sebagaimana diilustrasikan dalam gambar berikut.

![]({{site.baseurl}}/assets/img/0/28/0282.png)

Persamaan (perambatan) panas atau heat equation dalam 2-d yang semula

\begin{equation}\label{eqn:0285-1}
\frac{\partial T}{\partial t} = \alpha \left( \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} \right),
\end{equation}

akan menjadi

\begin{equation}\label{eqn:0285-2}
\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0,
\end{equation}

untuk keadaan tunak (steady state) dengan syarat batas pada Persamaan \eqref{eqn:0285-0}. Koefisien $\alpha$ dalam Persamaan \eqref{eqn:0285-1} adalah difusivitas termal yang tersusun atas konduktivitas termal $\kappa$, massa jenis $\rho$, dan kalor jenis $c$. Agar dapat menggunakan separasi variabel temperatur $T(x, y)$ diasumsikan dapat berbentuk

\begin{equation}\label{eqn:0285-3}
T(x, y) = X(x) Y(y).
\end{equation}

Substitusi Persamaan \eqref{eqn:0285-3} ke \eqref{eqn:0285-2} dan menyusun ulangnya akan dapat menghasilkan

\begin{equation}\label{eqn:0285-4}
\frac1X \frac{d^2 X}{dx^2} = -\frac1Y \frac{d^2 Y}{dy^2}.
\end{equation}

Salah satu cara untuk mencari solusi dari Persamaan \eqref{eqn:0285-4} adalah dengan memisalkan kedua ruas sebagai suatu konstanta, sebut saja $\beta^2$ atau $-\beta^2$. Dengan melihat syarat batas yang diberikan dan bahwa $T_2 \ne T_1$ maka agar pada arah $x$ merupakan fungsi periodik dan pada arah $y$ merupakan fungsi yang meluruh, sebaiknya konstantanya adalah

A | $\beta^2$ ataupun $-\beta^2$
B | $\beta^2$
C | $-\beta^2$
D | bukan $-\beta^2$ ataupun $\beta^2$.
E | nol.

{% comment %}
http://www.math.utah.edu/~gustafso/s2019/2270/projects-2019/submitted/kristenStewart/Determining%20Temperature%20Distribution%20of%20a%202D%20Heated%20Plate.pdf
{% endcomment %}