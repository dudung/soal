---
layout: soal
author: viridi
title: "0131"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["ampere law", "mathematics", "integral", "magnetic field", "long wire", "line integral", "fi1202", "2020-1"]
date: 2021-03-28 05:39:00 +07
permalink: /soal/0131
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/12/2021-03-28-line-integral-b-long-wire.md
ref: https://mathinsight.org/line_integral_vector_examples
---
Terdapat sebuah kawat lurus panjang yang mengalirkan arus $I$ keluar dari bidang gambar menuju pembaca. Suatu lintasan garis lurus dari $y = -a$ sampai $y = a$ terletak pada jarak $a$ dari kawat tersebut, sebagaimana diberikan dalam gambar di bawah ini.

{% if page.devlocal %}
![](/assets/img/soal/13/0131a.png)
{% else %}
![](../../../assets/img/soal/13/0131a.png)
{% endif %}

Ingin dihitung $\int \vec{B} \cdot d\vec{l}$ menggunakan lintasan garis lurus tersebut.


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
