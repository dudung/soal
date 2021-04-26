---
layout: soal
author: viridi
title: "0307"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["diffraction", "gratings", "tutorial-7", "fi1202", "2020-2"]
date: 2021-04-27 04:36:00 +07
permalink: /0307
src: https://github.com/dudung/soal/commits/master/_posts/0/30/2021-04-27-elementary-physics-tutorial-7-7.md
ref: https://www.google.com
---
Salah satu pemanfaatan mikroskop adalah untuk memeriksa sel darah. Asumsikan bahwa diameter lensa obyektif sama dengan jarak fokusnya. Jarak terdekat antara dua sel yang dapat dipisahkan (resolved) dan panjang gelombang yang digunakan untuk dapat melihat dua sel yang darah yang bedekatan (apakah lebih panjang / pendek dari atau sama dengan jarak antar dua sel) adalah

A | $1.22 \lambda$ dan lebih pendek.
B | $1.22 \lambda$ dan sama dengan.
C | $1.22 \lambda$ dan lebih panjang.
D | $2.44 \lambda$ dan lebih panjang.
C | $2.44 \lambda$ dan lebih pendek.


## &nbsp;
Jarak pisah angular $\theta_{\rm min}$ dari dua obyek yang teramati oleh lensa obyektif dengan diameter $D$ saat menggunakan cahaya berpanjang gelombang $\lambda$ adalah

\begin{equation}\label{eqn:0307-0}
\theta_{\rm min} = 1.22 \frac{\lambda}{D},
\end{equation}

yang dikenal sebagai kriteria Rayleigh. Terdapat dua sel darah merah (RBC: red blood cell) yang terpisahkan dengan ajarak $y$ dan terletak pada jarak $f$ (fokus) dari sebuah lensa obyektif berdiameter $D$ sebagai mana diilustrasikan berikut ini.

![]({{site.baseurl}}/assets/img/0/30/0307.png)

Untuk sudut kecil dapat didekati dengan

\begin{equation}\label{eqn:0307-1}
\tan \theta_{\rm min} \approx \sin \theta_{\rm min} \approx \theta_{\rm min},
\end{equation}

sehingga dapat diperoleh

\begin{equation}\label{eqn:0307-2}
\theta_{\rm min} \approx \frac{y}{f}.
\end{equation}

Dengan demikian jarak terdekat $y$ dapat diperoleh dengan melakukan menyamakan Persamaan \eqref{eqn:0307-0} dengan Persamaan \eqref{eqn:0307-2} yang akan memberikan

\begin{equation}\label{eqn:0307-3}
y = 1.22 \frac{f \lambda}{D}.
\end{equation}

Dalam beberapa kasus sering (atau dapat) diasumsikan bahwa $f = D$. Selanjutnya dapat segera terlihat dengan menggunakan asumsi tesebut bahwa $\lambda < y$.

{% comment %}
Anda menggunakan mikroskop untuk memeriksa sel darah. (a) tentukan jarak terdekat antara dua sel darah yang dapat dipisahkan, (b) Apakah anda menggunakan cahaya dengan panjang gelombang yang lebih panjang atau lebih pendek untuk bisa melihat dua sel darah yang lebih berdekatan?
You are using a microscope to examine a blood sample. (a) Determine the closest distance between two blood cells that can just be resolved, (b) should you use light with a longer wavelength or a shorter wavelength if you wish to resolve two blood cells that are even closer together?
{% endcomment %}
