---
layout: soal
author: viridi
title: "0130"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["ampere law", "mathematics", "integral", "atan result", "fi1202", "2020-1"]
date: 2021-03-28 05:22:00 +07
permalink: /soal/0130
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/13/2021-03-27-integral-datan.md
ref: http://www.math.com/tables/integrals/tableof.htm
---
Terdapat sebuah segitiga siku-siku yang memberikan hubungan antara alas $a$, tinggi $y$, sisi miring $r$, dan sudut $\theta$ seperti dalam gambar berikut ini.

![](/assets/img/soal/13/0130.png)

Dengan mengggunakan bantuan gambar sebelumnya dapat diperoleh solusi dari

\begin{equation}\nonumber
\int \frac{a dy}{a^2 + y^2},
\end{equation}

yaitu

<ol type="A">
<li>$\tan y + c$.
<li>$\tan^{-1} y + c$.
<li>$\tan (y/a) + c$.
<li>$\tan^{-1} (y/a) + c$.
<li>$\tan^{-1}(a/y) + c$.

{% comment %}
\begin{eqnarray}
y = a \tan \theta \newline
dy = a \sec^2 \theta \ d\theta \newline
a^2 + y^2 = a^2 \sec^2 \theta \newline
\displaystyle \int \frac{a dy}{a^2 + y^2} = \int \frac{a (a\sec^2 \theta \ d\theta)}{a^2 \sec^2 \theta} = \int d\theta = \theta = \tan^{-1} \left(\frac{y}{a}\right) + c
\end{eqnarray}
{% endcomment %}
