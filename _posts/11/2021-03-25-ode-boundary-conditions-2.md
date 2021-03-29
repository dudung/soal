---
layout: soal
author: viridi
title: "0117"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["ode", "boundary conditions", "fi3201", "2020-1"]
date: 2021-03-25 19:29:00 +07
permalink: /soal/0117
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/11/2021-03-25-ode-boundary-conditions-2.md
ref: http://www.multiphysics.us/BC.html
---
Syarat batas (SB), yang muncul dalam bentuk persamaan matematika, merupakan kumpulan tambahan syarat bagi permasalahan pada suatu batas yang spesifik. Konsep SB ini berlaku baik untuk persamaan diferensial biasa (PDB) maupun persamaan diferensial parsial (PDP). Terdapat lima jenis syarat batas, yaitu Dirichlet, Neumann, Robin, Mixed, dan Cauchy, dengan dua pertama merupakan SB yang predominan. Terdapat sebuah PDB

\begin{equation}\nonumber
\frac{du}{dx} + u = 0
\end{equation}

dalam domain $[a, b]$. Syarat batas berbentuk

\begin{equation}\nonumber
\chi_1 \cdot u(a) + \chi_2 \cdot \left. \frac{du}{dx} \right\| _{x = a} = A _\alpha, \ \ \ \
\chi_1 \cdot u(b) + \chi_2 \cdot \left. \frac{du}{dx} \right\| _{x = b} = B _\beta,
\end{equation}

dengan $\chi_1$ dan $\chi_2$ merupakan konstanta bobot, merupakan suatu SB dengan jenis

<ol type="A">
<li>Cauchy.
<li>Mixed.
<li>Robin.
<li>Neumann.
<li>Dirichlet.
