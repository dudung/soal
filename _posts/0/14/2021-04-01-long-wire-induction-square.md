---
layout: soal
author: viridi
title: "0146"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["long wire", "induction", "square wire", "fi1202", "2020-1"]
date: 2021-04-02 05:00:00 +07
permalink: /0146
src: https://github.com/dudung/soal/commits/master/_posts/0/14/2021-04-01-motional-emf.md
ref: https://doubtnut.com/question-answer-physics/a-long-straight-wire-carrying-current-i-and-a-square-conducting-wire-loop-of-side-l-at-a-distance-a--31091082
---
Terdapat kawat lurus panjang yang berarah vertikal dan mengalirkan arus $I$ dari bawah ke atas seperti dalam gambar di bawah. Di sebelah kanan kawat medan magnetik $B$ berarah masuk ke bidang gambar ($\times$) dan di sebelah kiri kawat medan magnetik $B$ berarah keluar dari bidang gambar ($\cdot$).

![]({{site.baseurl}}/assets/img/0/14/0146.png)

Pada suatu titik berjarak $p$ dari kawat berarus, medan magnetik yang disebabkan arus $I$ adalah

\begin{equation}\nonumber
B = \frac{\mu I}{2\pi p},
\end{equation}

dengan arahnya sesuai dengan penjelasan sebelumnya. Terdapat suatu simpul kawat berbentuk persegipanjang dengan lebar $(b-a)$ dan panjang $h$ yang terletak di sisi kanan kawat. Fluks magnetik yang melewati simpul persegi tersebut adalah

\begin{equation}\nonumber
\Phi_B = \int \vec{B} \cdot d\vec{A},
\end{equation}

dengan $dA = h dx$, di mana integrasi dilakukan dari $x = a$ sampai $x = b$. Variabel $x$ perlu digunakan dalam rumusan medan magnetik $B$ oleh kawat lurus panjang. Dengan demikian, dapat diperoleh fluks magnetik $\Phi_B$ pada loop kawat berbentuk persegi panjang $(b-a) \times h$, yaitu

<ol type="A">
<li>$\displaystyle \frac{\mu_0 I h}{2\pi} \ln \left( \frac{b}{a} \right)$.
<li>$\displaystyle \frac{\mu_0 I h}{2\pi} \ln \left( \frac{a}{b} \right)$.
<li>$\displaystyle \frac{\mu_0 I h}{2\pi} \ln (b - a)$.
<li>$\displaystyle \frac{\mu_0 I h}{2\pi} \ln (a - b)$.
<li>$\displaystyle \frac{\mu_0 I h}{2\pi} \ln ab$.

{% comment %}
\begin{eqnarray}
\Phi_B = \int \left(\frac{\mu_0 I}{2\pi x}\right) (h dx) \newline
= \left(\frac{\mu_0 I h}{2\pi}\right) \int \frac{dx}{x} \newline
= \left(\frac{\mu_0 I h}{2\pi}\right) \left[ \ln x \right]_{x = a}^b \newline
= \left(\frac{\mu_0 I h}{2\pi}\right) (\ln b - \ln a) \newline
= \frac{\mu_0 I h}{2\pi} \ln \left( \frac{b}{a} \right)
\end{eqnarray}
{% endcomment %}
