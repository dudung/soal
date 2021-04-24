---
layout: soal
author: viridi
title: "0302"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["interference", "thin film", "tutorial-7", "fi1202", "2020-2"]
date: 2021-04-24 11:13:00 +07
permalink: /0302
src: https://github.com/dudung/soal/commits/master/_posts/0/30/2021-04-24-elementary-physics-tutorial-7-2.md
ref: https://www.google.com
---
Sebuah lensa kamera berindeks bias $n_{\rm cam} = 1.52$ dilapisi dengan lapisan tak-reflektif magnesium flourida berindeks biar $n_{\rm MgF} = 1.38$ untuk mencegah pantulan cahaya kuning-hijau dengan panjang gelombang dalam vakum $\lambda = 565 \ \rm nm$. Ketebalan minimum, yang bukan nol, lapisan tak-reflektif tersebut adalah

A | $99\ \rm nm$.
B | $100\ \rm nm$.
C | $101\ \rm nm$.
D | $102\ \rm nm$.
E | $103\ \rm nm$.


## &nbsp;
Untuk mengurangi efek pantulan pada lensa kamera dapat digunakan fenomena interferensi lapisan tipis. Interferensi yang terjadi merupakan hasil superposisi dari berkas datang yang dipantulkan oleh berbagai lapisan dengan indeks bias berbeda.

![]({{site.baseurl}}/assets/img/0/30/0302.png)

Saat berkas cahaya dipantulkan pada batas antar dua medium berbeda indeks bias atau menempuh jarak tertentu, terjadi perubahan fasa $\Delta \phi$. Untuk gambar di atas dapat dituliskan perubahan-perubahan fasa $\Delta \phi_{ji}$ yang terjadi antara berkas awal $i$ dan berkas akhir $f$

$i$ | $j$ | $\Delta \phi_{ji}$ | Catatan
:-: | :-: | :-: | :-:
0 | 1 | $\pi$ | $n_1 < n_2$
0 | 2 | 0 | -
2 | 3 | $k_2 L$ | $\displaystyle k_2 = \frac{2\pi}{\lambda} n_2$
3 | 4 | $\pi$ | $n_2 < n_3$
4 | 5 | $k_2 L$ | $\displaystyle k_2 = \frac{2\pi}{\lambda} n_2$
5 | 6 | 0 | -

Untuk interferensi lapisan tipis diperlukan informasi $\Delta \phi_{61}$. Untuk itu diperlukan

\begin{equation}\label{eqn:0302-0}
\Delta \phi_{10} = \pi
\end{equation}

dan

\begin{equation}\label{eqn:0302-1}
\begin{array}{rcl}
\Delta \phi_{60} & = & \Delta \phi_{65} + \Delta \phi_{54} + \Delta \phi_{43} + \Delta \phi_{32} + \Delta \phi_{20} \newline
& = & \displaystyle 0 + \frac{2\pi}{\lambda} n_2 L_2 + \pi + \frac{2\pi}{\lambda} n_2 L + 0 \newline
& = & \displaystyle \pi + \frac{4\pi}{\lambda} n_2 L,
\end{array}
\end{equation}

sehingga

\begin{equation}\label{eqn:0302-2}
\Delta \phi_{61} = \Delta \phi_{60} - \Delta \phi_{10} = \frac{4\pi}{\lambda} n_2 L.
\end{equation}

Kembali ke bentuk fungsi medan listrik untuk berkas $1$

\begin{equation}\label{eqn:0302-3}
E_1(x, t) = E_0 \sin \omega t
\end{equation}

dan berkas $6$

\begin{equation}\label{eqn:0302-4}
E_6(x, t) = E_0 \sin (\omega t + \Delta \phi_{61}),
\end{equation}

yang akan memberikan hasil superposisi

\begin{equation}\label{eqn:0302-5}
\begin{array}{rcl}
E(x, t) & = & E_1(x, t) + E_6(x, t) \newline
& = & E_0 \sin \omega t + E_0 \sin (\omega t + \Delta \phi_{61}) \newline
& = & 2E_0 \sin \frac12 (\omega t + \frac12 \Delta \phi_{61}) \cos \frac12 \Delta \phi_{61}.
\end{array}
\end{equation}

Persamaan \eqref{eqn:0302-5} akan selalu bernilai nol atau interferensi minimum bila

\begin{equation}\label{eqn:0302-6}
\begin{array}{rcl}
\frac12 \Delta \phi_{61} & = & (m + \frac12) \pi \newline
\displaystyle \tfrac12 \frac{4\pi}{\lambda} n_2 L & = & (m + \frac12) \pi \newline
2 L_m & = & (m + \frac12) \displaystyle \frac{\lambda}{n_2}.
\end{array}
\end{equation}

Tebal minimum tercapai saat $m = 0$ sehingga diperoleh

\begin{equation}\label{eqn:0302-7}
L_0 = \frac14 \frac{\lambda}{n_2} = \frac14 \lambda_2.
\end{equation}

Ketebalan lapisan tipis (film) sebenarnya adalah

\begin{equation}\label{eqn:0302-8}
t = L \cos \theta_2 = L \cos \sin^{-1} \left( \frac{n_1}{n_2} \sin \theta_1 \right).
\end{equation}

Bila digunakan asumsi bahwa $\theta \approx 0$ yang menggambarkan pengamatan hampir tegak lurus lapisan tipis, maka akan diperoleh tebal

\begin{equation}\label{eqn:0302-9}
t = (2m + \tfrac14) \frac{\lambda}{n_2}, \ \ \ \ m = 0, 1, 2, \dots,
\end{equation}

untuk interferensi minimum pada lapisan tipis.
Bila indeks bias kaca kamera adalah $1.55$ dan indeks bias lapisan tipis di atas kaca adalah $1.45$, agar pantulan cahaya monokromatik $580 \ \rm nm$ dari udara ke kaca kamera dapat dicegah, ketebalan minium yang bukan nol dapat dihitung menggunakan kode Python berikut dengan bantuan Persamaan \eqref{eqn:0302-9}.

<iframe src="https://trinket.io/embed/python/66e9a4e38c" width="100%" height="210" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

{% comment %}
Lapisan nonreflektif magnesium fluorida (n=1,38) menutupi kaca (n=1,52) lensa kamera. Dengan asumsi
bahwa lapisan mencegah pantulan cahaya kuning-hijau (panjang gelombang dalam vakum = 565 nm),
tentukan ketebalan minimum (bukan nol) pelapis yang dapat dimiliki.
A nonreflective coating of magnesium fluoride (n = 1.38) covers the glass (n = 1.52) of a camera lens.
Assuming that the coating prevents reflection of yellow-green light (wavelength in vacuum = 565 nm),
determine the minimum nonzero thickness that the coating can have.
{% endcomment %}
