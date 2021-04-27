---
layout: soal
author: viridi
title: "0308"
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
date: 2021-04-27 06:16:00 +07
permalink: /0308
src: https://github.com/dudung/soal/commits/master/_posts/0/30/2021-04-27-elementary-physics-tutorial-7-8.md
ref: https://www.google.com
---
Dalam suatu percobaan difraksi celah ganda (lebar celah $a$ dan jarak antar celah $d$) diamati hilangnya garis terang ketiga yang sebelumnya muncul pada interferensi dua celah sempit (jarak antar celah $d$). Perbandingn $d$ terhadap $a$ dan orde garis-garis terang interferensi $m$ yang hilang adalah

A | $\frac13$ dan $1, 2, 3, \dots$.
B | $\frac13$ dan $3, 6, 9, \dots$.
C | $3$ dan $3, 6, 9, \dots$.
D | $3$ dan $1, 2, 3, \dots$.
C | Tidak dapat ditentunakan dari informasi yang diberikan.


## &nbsp;
Pada interferensi oleh dua celah (sempit) dengan jarak antar kedua celah adalah $d$, posisi angular garis terang diberikan oleh

\begin{equation}\label{eqn:0308-0}
d \sin \theta = m_{\rm int} \lambda, \ \ \ \ m_{\rm int} = 0, 1, 2, 3, \dots,
\end{equation}

yang menggambarkan interferensi konstruktif (interferensi maksimum). Pada difraksi oleh celah tunggal dengan lebar celah $a$ posisi garis angular gelap diberikan oleh

\begin{equation}\label{eqn:0308-1}
a \sin \theta = m_{\rm dif} \lambda, \ \ \ \ m_{\rm dif} = 1, 2, 3, 4, \dots,
\end{equation}

di mana pada difraksi pada pusat terdapat terang (pusat). Difraki oleh dua celah (jarak antar tengah kedua celah $d$ dan lebar masing-masing celah $a$) kedua Persamaan \eqref{eqn:0308-0} dan \eqref{eqn:0308-1} berlaku. Hal yang menarik dan umumnya disinggung adalah saat garis terang interferensi bertepatan dengan garis gelap difraksi (keduanya pada $\theta$ yang sama) sehingga membuat hilangnya beberapa garis terang yang seharusnya ada.

Bila terang interferensi ke-lima hilang, maka $m_{\rm int} = 5$ akan bertepatan dengan $m_{\rm dif} = 1$ dan dengan keduanya memiliki posisi angular ($\sin \theta$) yang sama, akan diperoleh

\begin{equation}\label{eqn:0308-2}
\begin{array}{rcl}
\sin \theta & = & \sin \theta \newline
\displaystyle \frac{m_{\rm dif} \lambda}{a} & = & \displaystyle \frac{m_{\rm int} \lambda}{d} \newline
\displaystyle \frac{d}{a} & = & \displaystyle \frac{m_{\rm int}}{m_{\rm dif}} \newline,
\end{array}
\end{equation}

di mana $\lambda$ pada kedua ruas juga sama karena digunakan sumber cahaya yang sama. Perhatikan bahwa $d/a$ akan berlaku pula untuk nilai-nilai $m_{\rm int}$ dan $m_{\rm dif}$ yang lain selama memenuhi Persamaan \eqref{eqn:0308-2}.

$m_{\rm dif}$ | 0 | | | | | 1 | | | | | 2
$I_{\rm dif}$ | max| | | | | min | | | | | min
$m_{\rm int}$ | 0 | 1 | 2  | 3 | 4 | 5 | 6 |7 | 8 | 9 | 10
$I_{\rm int}$ | max | max | max | max | max | max | max | max | max | max | max
$I_{\rm int-dif}$ | max | max | max | max | max | $\bf\tt\color{#00f}{min}$  | max | max | max | max | $\bf\tt\color{#00f}{min}$

Untuk kasus di atas $\bf\tt\color{#00f}{min}$ menggambarkan terang interferensi yang hilang karena posisinya bertepatan dengan minimum difraksi.

Dalam suatu percobaan difraksi celah ganda (lebar celah $a$ dan jarak antar celah $d$) diamati hilangnya garis terang keempat yang sebelumnya muncul pada interferensi dua celah sempit (jarak antar celah $d$). Perbandingn $d$ terhadap $a$ dan orde garis-garis terang interferensi $m$ yang hilang telah dapat ditentukan.


{% comment %}
Dalam sebuah percobaan celah ganda (a) berapakah perbandingan d yang menyebabkan difraksi menghilangkan garis terang ke-tiga? (b) Apakah garis-garis terang lainnya juga hilang?
In a multiple bug experiment, (a) what ratio d causes diffraction to remove the third bright line?, (b) Are other bright streaks also missing?
{% endcomment %}
