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
date: 2021-03-28 17:51:00 +07
permalink: /0131
src: https://github.com/dudung/soal/commits/master/_posts/0/13/2021-03-28-line-integral-b-long-wire.md
ref: https://mathinsight.org/line_integral_vector_examples
---
Terdapat sebuah kawat lurus panjang yang mengalirkan arus $I$ keluar dari bidang gambar menuju pembaca. Suatu lintasan garis lurus dari $y = -b$ sampai $y = b$ terletak pada jarak $a$ dari kawat tersebut, sebagaimana diberikan dalam gambar di bawah ini.

![]({{site.baseurl}}/assets/img/0/13/0131a.png)

Ingin dihitung $\int \vec{B} \cdot d\vec{l}$ menggunakan lintasan garis lurus tersebut. Untuk memudahkan digunakan sistem koordinat berikut di mana pusat koordinat berda pada tengah kawat (tidak digambarkan demikian agar terlihat lebih sederhana).

![]({{site.baseurl}}/assets/img/0/13/0131b.png)

Beberapa hal yang akan digunakan adalah

<ol>
<li>Untuk kawat lurus panjang $\displaystyle \vec{B} = \frac{\mu_0 I}{2 \pi r} \hat{\theta}$.</li>
<li>Vektor satuan posisi angular $\hat{\theta} = -\sin\theta \ \hat{x} + \cos\theta \ \hat{y}$.</li>
<li>Elemen panjang lintasan $d\vec{l} = \hat{y} dy$.</li>
<li>Integral dilakukan mulai dari $y = -b$ sampai $y = b$.</li>
<li>Perlu menggunakan solusi bentuk integral $\displaystyle \int \frac{ady}{a^2 + y^2}$.</li>
<li>Terdapat hubungan $a = r \cos \theta$, $y = r \sin \theta$, dan $r^2 = a^2 + y^2$</li>
</ol>

Dengan demikian hasil integral

\begin{equation}\nonumber
\int_{y = -b}^{y = b} \vec{B} \cdot d\vec{l}
\end{equation}

adalah

<ol type="A">
<li>$\displaystyle \frac{\mu_0 I}{\pi} \tan^{-1} \left( \frac{b}{a} \right)$.
<li>$\displaystyle \frac{\mu_0 I}{\pi} \tan^{-1} \left( \frac{a}{b} \right)$.
<li>$\displaystyle \frac{\mu_0 I}{\pi}$.
<li>$\displaystyle \frac{\mu_0 I}{4\pi}$.
<li>$\displaystyle \frac{\mu_0 I}{4}$.

{% comment %}
\begin{eqnarray}
\int_{y = -b}^{y = b} \vec{B} \cdot d\vec{l} \newline
= \int_{y = -b}^{y = b} \left( \frac{\mu_0 I}{2 \pi r} \hat{\theta} \right) \cdot (\hat{y} dy) \newline
= \int_{y = -b}^{y = b} \left( \frac{\mu_0 I}{2 \pi r} \right) \hat{\theta} \cdot (\hat{y} dy) \newline
= \int_{y = -b}^{y = b} \left( \frac{\mu_0 I}{2 \pi r} \right) (-\sin\theta \ \hat{x} + \cos\theta \ \hat{y}) \cdot (\hat{y} dy) \newline
= \int_{y = -b}^{y = b} \left( \frac{\mu_0 I}{2 \pi r} \right) \cos\theta dy \newline
= \int_{y = -b}^{y = b} \frac{\mu_0 I}{2 \pi r} \cos\theta dy \newline
= \frac{\mu_0 I}{2 \pi} \int_{y = -b}^{y = b} \left( \frac{\cos\theta}{r} \right) dy \newline
= \frac{\mu_0 I}{2 \pi} \int_{y = -b}^{y = b} \left( \frac{a}{r^2} \right) dy \newline
= \frac{\mu_0 I}{2 \pi} \int_{y = -b}^{y = b} \frac{a dy}{a^2 + y^2} \newline
= \frac{\mu_0 I}{2 \pi} \left[ \tan^{-1} \left( \frac{y}{a} \right) \right]_{y = -b}^{y = b} \newline
= \frac{\mu_0 I}{2 \pi} \left[ \tan^{-1} \left( \frac{b}{a} \right) - \tan^{-1} \left( \frac{-b}{a} \right) \right] \newline
= \frac{\mu_0 I}{2 \pi} \left[ \tan^{-1} \left( \frac{b}{a} \right) + \tan^{-1} \left( \frac{b}{a} \right) \right] \newline
= \frac{\mu_0 I}{2 \pi} \left[ 2 \tan^{-1} \left( \frac{b}{a} \right) \right] \newline
= \frac{\mu_0 I}{\pi} \tan^{-1} \left( \frac{b}{a} \right).
\end{eqnarray}
{% endcomment %}
