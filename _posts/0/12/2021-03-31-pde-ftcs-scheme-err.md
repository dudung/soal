---
layout: soal
author: viridi
title: "0129"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["pde", "ftcs", "forward time centered space", "heat equation", "error propagation", "fi3201", "2020-1"]
date: 2021-03-31 09:08:00 +07
permalink: /0129
src: https://github.com/dudung/soal/commits/master/_posts/0/12/2021-03-31-pde-ftcs-scheme-err.md
ref: https://en.wikipedia.org/wiki/Von_Neumann_stability_analysis
---
FTCS (forward time centered space) merupakan metode beda hingga untuk menyelesaikan persamaan diferensial dengan menggunakan beda hingga maju untuk waktu (forward in time) dan beda hingga tengah untuk ruang (centered in space). Persamaan perambatan panas dala satu-dimensi

\begin{equation}\nonumber
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
\end{equation}

merupakan contoh yang sering digunakan untuk ilustrasi penerapan FTCS, yang akan memberikan solusi iteratif

\begin{equation}\nonumber
u_i^{j+1} = \beta u_{i-1}^j + (1 - 2\beta) u_i^j + \beta u_{i+1}^j
\end{equation}

dengan

\begin{equation}\nonumber
\beta = \frac{\Delta t}{(\Delta x)^2}.
\end{equation}

Agar tercapai stabilitas maka perlu terpenuhi kondisi

<ol type="A">
<li>$\alpha \beta < \frac12$.
<li>$\alpha < \frac12$.
<li>$\beta < \frac12$.
<li>$(\alpha/\beta) < \frac12$.
<li>$(\beta/\alpha) < \frac12$.
