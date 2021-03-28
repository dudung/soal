---
layout: soal
author: viridi
title: "0132"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["ampere law", "mathematics", "integral", "magnetic field", "long wire", "line integral", "square loop", "fi1202", "2020-1"]
date: 2021-03-28 18:45:00 +07
permalink: /soal/0132
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/12/2021-03-28-ampere-law-long-wire-square-loop.md
ref: https://web.iit.edu/sites/web/files/departments/academic-affairs/academic-resource-center/pdfs/Amperes_law.pdf
---
Terdapat kawat lurus panjang yang mengalirkan arus $I$ keluar dari bidang gambar menuju pembaca. Sebuah lintasan tertutup Ampere $(+a, -a)$ -- $(+a, +a)$ -- $(-a, +a)$ -- $(-a, -a)$ -- $(+a, -a)$ melingkupi kawat berarus sebelumnya yang menembus lintasan berbentuk persegi tepat di tengah-tengahnya secara tegak lurus seperti dalam gambar berikut.

![](../../../assets/img/soal/13/0132.png)

Hasil dari
\begin{equation}\nonumber
\oint \vec{B} \cdot d\vec{l}
\end{equation}

pada gambar adalah

<ol type="A">
<li>$0$.
<li>$\frac14\mu_0 I$.
<li>$\mu_0 I$.
<li>$2\mu_0 I$.
<li>$4\mu_0 I$.

{% comment %}
\begin{eqnarray}
\oint \vec{B} \cdot d\vec{l} \newline
= \int_{(+a, -a)}^{(+a, +a)} \vec{B} \cdot d\vec{l} + \int_{(+a, +a)}^{(-a, +a)} \vec{B} \cdot d\vec{l} + \int_{(-a, +a)}^{(-a, -a)} \vec{B} \cdot d\vec{l} + \int_{(-a, -a)}^{(+a, -a)} \vec{B} \cdot d\vec{l} \newline
= 4 \int_{(+a, -a)}^{(+a, +a)} \vec{B} \cdot d\vec{l} \newline
= 4 \left( \frac{\mu_0 I}{4} \right) \newline
= \mu_0 I.
\end{eqnarray}
{% endcomment %}
