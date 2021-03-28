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
date: 2021-03-28 17:21:00 +07
permalink: /soal/0131
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/12/2021-03-28-line-integral-b-long-wire.md
ref: https://mathinsight.org/line_integral_vector_examples
---
Terdapat sebuah kawat lurus panjang yang mengalirkan arus $I$ keluar dari bidang gambar menuju pembaca. Suatu lintasan garis lurus dari $y = -b$ sampai $y = b$ terletak pada jarak $a$ dari kawat tersebut, sebagaimana diberikan dalam gambar di bawah ini.

![](../../../assets/img/soal/13/0131a.png)

Ingin dihitung $\int \vec{B} \cdot d\vec{l}$ menggunakan lintasan garis lurus tersebut. Untuk memudahkan digunakan sistem koordinat berikut di mana pusat koordinat berda pada tengah kawat (tidak digambarkan demikian agar terlihat lebih sederhana).

![](../../../assets/img/soal/13/0131b.png)

Beberapa hal yang akan digunakan adalah

<ol>
<li>Untuk kawat lurus panjang $\displaystyle \vec{B} = \frac{\mu_0 I}{2 \pi r} \hat{\theta}$.</li>
<li>Vektor satuan posisi angular $\hat{\theta} = -\sin\theta \ \hat{x} + \cos\theta \ \hat{y}$.</li>
<li>Elemen panjang lintasan $d\vec{l} = \hat{y} dy$.</li>
<li>Integral dilakukan mulai dari $y = -b$ sampai $y = b$.</li>
<li>Perlu menggunakan solusi bentuk integral $\displaystyle \int \frac{ady}{a^2 + y^2}$.</li>
</ol>

Dengan demikian hasil integral

\begin{equation}\nonumber
\int_{y = -b}^{y = b} \vec{B} \cdot d\vec{l}
\end{equation}

adalah

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
