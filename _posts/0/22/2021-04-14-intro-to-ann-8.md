---
layout: soal
author: viridi
title: "0228"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["artificial neural network", "ann", "feed forward", "three layers", "error", "fi3201", "2020-2"]
date: 2021-04-14 11:38:00 +07
permalink: /0228
src: https://github.com/dudung/soal/commits/master/_posts/0/22/2021-04-13-intro-to-ann-8.md
ref: https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
---
Untuk melatih suatu jaringan sarat tiruan (JST) atau artificial neural network (ANN) dapat memanfaatkan metode yang umum digunakan, seperti backpropagation. Suatu arsitektur JST berjenis feed forward terdiri dari dua neuron masukan ($\LARGE \color{#ffcc00} \bullet$), dua neuron tersembunyi ($\LARGE \color{#66cc00} \bullet$), dan satu neuron keluaran ($\LARGE \color{#ff6600} \bullet$).

![]({{site.baseurl}}/assets/img/0/22/0228.png)

Dengan $f(x)$ adalah suatu fungsi aktivasi dapat dituliskan hubungan-hubungan berikut kecuali

<ol type="A">
<li>$y_1 = f(w_{11} x_1 + w_{12} x_2)$.
<li>$y_2 = f(w_{21} x_1 + w_{22} x_2)$.
<li>$z_1 = f(u_{11} y_1 + u_{12} y_2)$.
<li>$z_1 = f[u_{11} f(w_{11} x_1 + w_{12} x_2) + u_{12} f(w_{21} x_1 + w_{22} x_2)]$.
<li>$z_1 = f(w_{11} y_1 + w_{12} y_2)$.
