---
layout: soal
author: viridi
title: "0309"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["diffraction", "double-slit", "tutorial-7", "fi1202", "2020-2"]
date: 2021-04-27 07:43:00 +07
permalink: /0309
src: https://github.com/dudung/soal/commits/master/_posts/0/30/2021-04-27-elementary-physics-tutorial-7-9.md
ref: https://www.google.com
---
Cahaya monokromatik berpanjang gelombang $600 \ \rm nm$ jatuh tegak lurus pada dua celah sempit, tepat di tengah-tengahnya sehingga kedua celah dapat dianggap sebagai dua sumber yang koheren. Jarak antara celah adalah $6.0 \ \rm \mu m$ dan jarak layar dari celah adalah $2 \ \rm m$. Lebar celah adalah $1.5 \ \rm \mu m$. Pola interferensi-difraksi yang tepat adalah

A | ![]({{site.baseurl}}/assets/img/0/30/0309a.png).
B | ![]({{site.baseurl}}/assets/img/0/30/0309b.png).
C | ![]({{site.baseurl}}/assets/img/0/30/0309c.png).
D | ![]({{site.baseurl}}/assets/img/0/30/0309d.png).
C | ![]({{site.baseurl}}/assets/img/0/30/0309e.png).


## &nbsp;
Pada interferensi oleh dua celah (sempit) dengan jarak antar kedua celah adalah $d$, posisi angular garis terang diberikan oleh

\begin{equation}\label{eqn:0309-0}
d \sin \theta = m_{\rm int} \lambda, \ \ \ \ m_{\rm int} = 0, 1, 2, 3, \dots,
\end{equation}

yang menggambarkan interferensi konstruktif (interferensi maksimum) dan posisi angular garis gelap diberikan oleh

\begin{equation}\label{eqn:0309-1}
d \sin \theta = (m_{\rm int}  + \tfrac12) \lambda, \ \ \ \ m_{\rm int} = 0, 1, 2, 3, \dots,
\end{equation}

yang menggambarkan interferensi destruktif (interferensi minimum). Pada difraksi oleh celah tunggal dengan lebar celah $a$ posisi garis angular gelap diberikan oleh

\begin{equation}\label{eqn:0309-2}
a \sin \theta = m_{\rm dif} \lambda, \ \ \ \ m_{\rm dif} = 1, 2, 3, 4, \dots,
\end{equation}

di mana pada difraksi pada pusat terdapat terang (pusat) atau dapat dikatakan saat $m_{\rm dif} = 0$. Dari ketiga Persamaan \eqref{eqn:0309-0}, \eqref{eqn:0309-1}, dan  \eqref{eqn:0309-2} dapat terlihat bahwa selalu terdapat $\sin\theta$ yang tak bersatuan dan dapat digunakan sebagai sumbu mendatar untuk menggambarkan pola intensitas interferensi-difraksi.

$\sin\theta$ | $0$ | $\frac12 \lambda/d$ | $\lambda/d$ | $\frac32 \lambda/d$ | $2\lambda/d$ | $\frac52 \lambda/d$ | $3\lambda/d$ | $\frac72 \lambda/d$ | $4\lambda/d$ | $\frac92 \lambda/d$ | $5\lambda/d$ | $\frac{11}2 \lambda/d$ | $6\lambda/d$
$I_{\rm int}$ | max | min | max | min | max | min | max | min | max | min | max | min | max
$\sin\theta$ | $0$ | | | | | | $\lambda/a$ | | | | | | $\lambda/a$
$I_{\rm dif}$ | max | | | | | | min | | | | | | min
$I_{\rm int-dif}$ | max | min | max | min | max | min | $\bf\tt\color{#00f}{min}$ | min | max | min | max | min | $\bf\tt\color{#00f}{min}$

Tabel di atas adalah untuk $d/a = 3$ dan $\bf\tt\color{#00f}{min}$ menggambarkan terang interferensi yang hilang karena posisinya bertepatan dengan minimum difraksi.

{% comment %}
Cahaya koheren dengan panjang gelombang 500 nm jatuh tegak lurus pada dua celah sempit dengan jarak antar celah d = 6,0 μm. Sebuah layar diletakkan pada jarak L=2 m dari celah.
a. Gambarkan/sketsa pola intensitas interferensi sebagai fungsi sin θ (nyatakan dalam λ dan d untuk titik titik dimana terjadi interferensi minimum dan maksimum hingga orde kedua
b. Tentukan jarak dari titik pusat O ke posisi interferensi minimum orde ke-2 di layar.
c. Jika digunakan panjang gelombang 600 nm, dimanakah posisi minimum orde pertama di layar relatif terhadap terang pusat.
d. Jika lebar celah adalah 2,0 μm, gambarkan sketsa pola intensitas interferensi sebagai fungsi sin θ dengan memperhitungkan pengaruh difraksi.
Coherent light with a wavelength of 500 nm falls perpendicular to the two slits narrow with a gap between the gaps d = 6,0 μm. A screen is placed at a distance of L = 2 m from the gap.
a. Draw / sketch the pattern of interference intensity as a function of sin θ (express in λ and d for the points where the minimum and maximum interference occurs up to the order second
b. Determine the distance from the center point O to the 2nd order minimum interference position on the screen.
c. If a wavelength of 600 nm is used, where is the minimum order position first on the screen relative to the center light.
d. If the width of the slit is 2,0 μm, sketch the pattern of the intensity of the interference as a function of sin θ taking into account the effect of diffraction.{% endcomment %}
