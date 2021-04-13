---
layout: soal
author: viridi
title: "0224"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["artificial neural network", "ann", "treshold logic unit", "fi3201", "2020-2"]
date: 2021-04-14 04:19:00 +07
permalink: /0224
src: https://github.com/dudung/soal/commits/master/_posts/0/22/2021-04-13-intro-to-ann-4.md
ref: https://developer.ibm.com/articles/l-neural/
---
Langkah pertama untuk memahami jaringan saraf adalah dengan membuat abstraksi dari neuron biologis dan berkonsentrasi pada karakternya sebagai suatu satuan logis ambang (SLA) atau treshold logic unit (TLU) sebagaimana diilustrasikan berikut ini.

![]({{site.baseurl}}/assets/img/0/22/0223.png)



Dengan $y_i = f(z_i)$, di mana $y_i$ adalah keluaran suatu SLA, formulasi umum untuk memperoleh $z_i$ adalah

<ol type="A">
<li>$\displaystyle \sum_i w_{ji} x_i$.
<li>$\displaystyle \prod_i w_{ji} x_i$.
<li>$\displaystyle \sum_i \frac{w_{ji}}{x_i}$.
<li>$\displaystyle \prod_i \frac{w_{ji}}{x_i}$.
<li>$\displaystyle \sum_i e^{w_{ji} x_i}$.
