---
layout: soal
author: viridi
title: "0114"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["finite difference", "nth derivative", "central", "fi3201", "2020-1"]
date: 2021-03-25 17:51:00 +07
permalink: /soal/0114
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/11/2021-03-25-finite-difference-nth-derivative-c.md
ref: https://en.wikipedia.org/wiki/Finite_difference
---
Suatu fungsi $f(x)$, dengan menggunakan beda hingga tengah, dapat dicari pendekatan untuk turunan pertamanya

\begin{equation}\label{eqn:0114-1st-derivative-central}
f'(x) \approx \frac{\delta_h [f] (x)}{h} = \frac{f(x+\frac12h) - f(x-\frac12h)}{h}
\end{equation}

dan untuk turunan keduanya

\begin{equation}\label{eqn:0114-2nd-derivative-central}
f{\rm''}(x) \approx \frac{\delta_h^2 [f] (x)}{h} = \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}.
\end{equation}

Dengan menggunakan koefisien binomial

\begin{equation}\label{eqn:0114-binomial-coefficient}
\left(
\begin{array}{c}
n \newline
k
\end{array}
\right) = \frac{n!}{k!(n-k)!},
\end{equation}

dapat diperoleh rumusan untuk turunan ke-$n$ dari $f(x)$ dengan beda hingga tengah, yaitu

<ol type="A">
<li>
$\displaystyle \sum_{i=0}^n (-1)^{n-i} \left(
\begin{array}{c}n \newline k\end{array} \right) f(x + ih)
$.

