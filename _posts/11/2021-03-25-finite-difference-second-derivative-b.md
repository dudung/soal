---
layout: soal
author: viridi
title: "0113"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["finite difference", "second derivative", "backward", "fi3201", "2020-1"]
date: 2021-03-25 17:46:00 +07
permalink: /soal/0113
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/11/2021-03-25-finite-difference-second-derivative-b.md
ref: https://en.wikipedia.org/wiki/Finite_difference
---
Turunan orde pertama dari suatu fungsi $f(x)$ dapat diperoleh pendekatannya menggunakan beda hingga maju

\begin{equation}\label{eqn:0111-1st-derivative-forward-fd}
f'(x) \approx \frac{\Delta_h [f] (x)}{h}
\end{equation}

dan mundur

\begin{equation}\label{eqn:0111-1st-derivative-backward-fd}
f'(x) \approx \frac{\nabla_h [f] (x)}{h}.
\end{equation}

Dengan beda hingga mundur untuk turunan kedua $f(x)$ dapat diperoleh

\begin{equation}\label{eqn:0111-2nd-derivative-central-fd}
f{\rm''}(x) \approx \frac{\nabla_h^2 [f] (x)}{h^2} = \frac{1}{h} \left\\{ \frac{\nabla_h [f] (x)}{h} - \frac{\nabla_h [f] (x-h)}{h} \right\\}
\end{equation}

yang akan memberikan $h^2 f{\rm''}(x)$ berbentuk

<ol type="A">
<li>$f(x+2h) - 2f(x+h) + f(x)$.
<li>$f(x) - 2f(x-h) + f(x-2h)$.
<li>$f(x+h) + 2f(x) - f(x-h)$.
<li>$f(x+h) - 2f(x) + f(x-h)$.
<li>$f(x+h) + 2f(x) + f(x-h)$.
