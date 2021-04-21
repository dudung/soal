---
layout: soal
author: viridi
title: "0281"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["heat conduction", "fourier's law", "fi3201", "2020-2"]
date: 2021-04-22 05:20:00 +07
permalink: /0281
src: https://github.com/dudung/soal/commits/master/_posts/0/28/2021-04-22-fourier-law-hc-fd-2d-0.md
ref: https://dx.doi.org/10.1615/AtoZ.c.conduction
---
Laju perubahan energi yang diperoleh (atau hilang) pada arah $x$ yang menembus suatu luasan $dA = dydz$ diberikan oleh

\begin{equation}\label{eqn:0281-1}
\frac{\Delta Q}{\Delta t} = (q_x - q_{x + dx}) (dy dz).
\end{equation}

Ekspansi deret Fourier memberikan

\begin{equation}\label{eqn:0281-2}
f(x + dx) \approx f(x) + \frac{\partial f}{\partial x} dx,
\end{equation}

yang dapat memberikan

\begin{equation}\label{eqn:0281-3}
f(x) - f(x + dx) \approx  - \frac{\partial f}{\partial x} dx,
\end{equation}

sehingga membuat Persamaan \eqref{eqn:0281-1} menjadi

\begin{equation}\label{eqn:0281-4}
\frac{\Delta Q}{\Delta t} = \left( - \frac{\partial q}{\partial x} dx \right) (dy dz) = - \frac{\partial q}{\partial x} dV,
\end{equation}

di mana $dV = dA dx = dx dy dz$.
