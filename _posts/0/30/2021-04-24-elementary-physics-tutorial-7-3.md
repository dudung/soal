---
layout: soal
author: viridi
title: "0303"
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
date: 2021-04-26 17:49:00 +07
permalink: /0303
src: https://github.com/dudung/soal/commits/master/_posts/0/30/2021-04-24-elementary-physics-tutorial-7-3.md
ref: https://www.google.com
---
Terdapat lapisan tipis sabun berketebalan berbeda pada lokasi berbeda. Indeks bias lapisan tipis tersebut adalah $n$ dan nilainya tidak diketahui. Lapisan tipis tersebut diapit oleh udara di kedua sisinya. Cahaya polikromatik jatuh pada lapisan tipis sabun tersebut dan permukaan lapisan sabun teramati beraneka warna. Suatu daerah terlihat berwarna kuning karena terjadi interferensi destruktif untuk warna biru (dalam vakum $\lambda_{\rm blue} = 469 \ \rm nm$), sementara daerah lain terlihat berwarna ungu karena terjadi interferensi destruktif untuk warna hijau (dalam vakum $\lambda_{\rm green} = 555 \ \rm nm$). Lapisan tipis tersebut memiliki ketebalan minimum $t$ yang bukan nol agar dapat menghasilkan interferensi destruktif lapisan tipis. Rasio ketebalan daerah bewarna ungu $t_{\rm purple}$ terhadap ketebalan daerah berwarna kuning $t_{\rm yellow}$ adalah

A | $1.318$.
B | $1.813$.
C | $0.854$.
D | $0.845$.
E | $1.183$.


## &nbsp;
Lapisan tipis pada gelembung sabun merupakan suatu lapisan tipis dengan susunan bahan udara, cairan sabun, dan udara. Interferensi yang terjadi merupakan hasil superposisi dari berkas datang yang dipantulkan oleh berbagai lapisan dengan indeks bias berbeda. Untuk lapisan tipis (gelembung) sabun indeks bias $n_1 = n_3 = 1$ yang merupakan udara dan indeks bias $n_2$ yang merupakan gelembung sabun. Nilai $n_2 > 1$.

![]({{site.baseurl}}/assets/img/0/30/0302.png)

Saat berkas cahaya dipantulkan pada batas antar dua medium berbeda indeks bias atau menempuh jarak tertentu, terjadi perubahan fasa $\Delta \phi$. Untuk gambar di atas dapat dituliskan perubahan-perubahan fasa $\Delta \phi_{ji}$ yang terjadi antara berkas awal $i$ dan berkas akhir $f$

$i$ | $j$ | $\Delta \phi_{ji}$ | Catatan
:-: | :-: | :-: | :-:
0 | 1 | $\pi$ | $n_1 < n_2$
0 | 2 | 0 | -
2 | 3 | $k_2 L$ | $\displaystyle k_2 = \frac{2\pi}{\lambda} n_2$
3 | 4 | 0 | $n_2 > n_3 = n_1$
4 | 5 | $k_2 L$ | $\displaystyle k_2 = \frac{2\pi}{\lambda} n_2$
5 | 6 | 0 | -

Untuk interferensi lapisan tipis diperlukan informasi $\Delta \phi_{61}$. Untuk itu diperlukan

\begin{equation}\label{eqn:0303-0}
\Delta \phi_{10} = \pi
\end{equation}

dan

\begin{equation}\label{eqn:0303-1}
\begin{array}{rcl}
\Delta \phi_{60} & = & \Delta \phi_{65} + \Delta \phi_{54} + \Delta \phi_{43} + \Delta \phi_{32} + \Delta \phi_{20} \newline
& = & \displaystyle 0 + \frac{2\pi}{\lambda} n_2 L_2 + 0 + \frac{2\pi}{\lambda} n_2 L + 0 \newline
& = & \displaystyle \frac{4\pi}{\lambda} n_2 L,
\end{array}
\end{equation}

sehingga

\begin{equation}\label{eqn:0303-2}
\Delta \phi_{61} = \Delta \phi_{60} - \Delta \phi_{10} = \frac{4\pi}{\lambda} n_2 L - \pi.
\end{equation}

Kembali ke bentuk fungsi medan listrik untuk berkas $1$

\begin{equation}\label{eqn:0303-3}
E_1(x, t) = E_0 \sin \omega t
\end{equation}

dan berkas $6$

\begin{equation}\label{eqn:0303-4}
E_6(x, t) = E_0 \sin (\omega t + \Delta \phi_{61}),
\end{equation}

yang akan memberikan hasil superposisi

\begin{equation}\label{eqn:0303-5}
\begin{array}{rcl}
E(x, t) & = & E_1(x, t) + E_6(x, t) \newline
& = & E_0 \sin \omega t + E_0 \sin (\omega t + \Delta \phi_{61}) \newline
& = & 2E_0 \sin \frac12 (\omega t + \frac12 \Delta \phi_{61}) \cos \frac12 \Delta \phi_{61}.
\end{array}
\end{equation}

Persamaan \eqref{eqn:0303-5} akan selalu bernilai nol atau interferensi minimum bila

\begin{equation}\label{eqn:0303-6}
\begin{array}{rcl}
\frac12 \Delta \phi_{61} & = & (m' + \frac12) \pi \newline
\displaystyle \tfrac12 \left( \frac{4\pi}{\lambda} n_2 L - \pi \right) & = & (m' + \frac12) \pi \newline
\displaystyle \frac{2\pi}{\lambda} n_2 L - \tfrac12 \pi & = & m' \pi + \frac12 \pi \newline
\displaystyle \frac{2\pi}{\lambda} n_2 L & = & m' \pi + \pi \newline
2 L_m & = & (m' + 1) \displaystyle \frac{\lambda}{n_2}. \newline
2 L_m & = & m \displaystyle \frac{\lambda}{n_2}.
\end{array}
\end{equation}

Dengan demikian, tebal minimum yang tidak nola tercapai saat $m = 1$ sehingga diperoleh

\begin{equation}\label{eqn:0303-7}
L_1 = \frac12 \frac{\lambda}{n_2}.
\end{equation}

Ketebalan lapisan tipis (film) sebenarnya adalah

\begin{equation}\label{eqn:0303-8}
t = L \cos \theta_2 = L \cos \sin^{-1} \left( \frac{n_1}{n_2} \sin \theta_1 \right).
\end{equation}

Bila digunakan asumsi bahwa $\theta_1 \approx 0$ yang menggambarkan pengamatan hampir tegak lurus lapisan tipis, maka akan diperoleh tebal

\begin{equation}\label{eqn:0303-9}
t_m = \left( \frac{2m}{4} \right) \frac{\lambda}{n_2}, \ \ \ \ m = 0, 1, 2, \dots,
\end{equation}

untuk interferensi minimum pada lapisan tipis.

Cahaya polikromatik akan berwarna putih (W: white) di mana terdapat semua warna, sebagaimana disajikan dalam gambar berikut ini, dengan merah (R: red $\color{#f00}\blacksquare$), biru (B: blue $\color{#00f}\blacksquare$), hijau (G: green $\color{#0f0}\blacksquare$), kuning (Y: yellow $\color{#ff0}\blacksquare$), ungu (M: magenta, purple $\color{#f0f}\blacksquare$), sian (C: cyan $\color{#0ff}\blacksquare$).

![]({{site.baseurl}}/assets/img/0/30/0303.png)

Bila terdapat warna tertentu yang hilang karena interferensi destruktif yang tersisa adalah warna komplementernya untuk membentuk warna putih.

Cahaya asal | Interferensi desktruktif | Warna tersisa | Warna tampak
:-: | :-: | :-: | :-:
W $\color{#000}\square$ | R $\color{#f00}\blacksquare$ | B $\color{#00f}\blacksquare$ + G $\color{#0f0}\blacksquare$ | C $\color{#0ff}\blacksquare$
W $\color{#000}\square$ | G $\color{#0f0}\blacksquare$ | R $\color{#f00}\blacksquare$ + B $\color{#00f}\blacksquare$ | M $\color{#f0f}\blacksquare$
W $\color{#000}\square$ | B $\color{#00f}\blacksquare$ | R $\color{#f00}\blacksquare$ + G $\color{#0f0}\blacksquare$ | Y $\color{#ff0}\blacksquare$

Terdapat lapisan tipis sabun berketebalan berbeda pada lokasi berbeda. Indeks bias lapisan tipis tersebut adalah $n$ dan nilainya tidak diketahui. Lapisan tipis tersebut diapit oleh udara di kedua sisinya. Cahaya polikromatik jatuh pada lapisan tipis sabun tersebut dan permukaan lapisan sabun teramati beraneka warna. Suatu daerah terlihat berwarna kuning karena terjadi interferensi destruktif untuk warna biru (dalam vakum $\lambda_{\rm blue} = 480 \ \rm nm$), sementara daerah lain terlihat berwarna sian karena terjadi interferensi destruktif untuk warna merah (dalam vakum $\lambda_{\rm red} = 700 \ \rm nm$). Lapisan tipis tersebut memiliki ketebalan minimum $t$ yang bukan nol agar dapat menghasilkan interferensi destruktif lapisan tipis. Rasio ketebalan daerah bewarna kuning $t_{\rm yellow}$ terhadap ketebalan daerah berwarna sian $t_{\rm cyan}$ adalah

<iframe src="https://trinket.io/embed/python/c9d21be80c" width="100%" height="410" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

{% comment %}
tutorial problem-3
Lapisan sabun dengan ketebalan berbeda di tempat berbeda memiliki indeks bias n yang tidak diketahui dan udara di kedua sisinya. Cahaya pantul terlihat beraneka warna. Satu area tampak kuning karena interferensi destruktif telah menghilangkan warna biru (vakum 469 nm) dari cahaya pantul, sedangkan area lain tampak ungu karena interferensi destruktif telah menghilangkan warna hijau (vakum 555 nm). Lapisan memiliki ketebalan minimun t (bukan nol) untuk terjadinya interferensi destruktif. Tentukan rasio t ungu /t kuning?
A soap film with different thicknesses at different places has an unknown refractive index n and air on both sides. In reflected light it looks multicolored. One region looks yellow because destructive interference has removed blue (vacuum 469 nm) from the reflected light, while another looks magenta because destructive interference has removed green (vacuum 555 nm). In these regions the film has the minimum nonzero thickness t required for the destructive interference to occur. Find the ratio t magenta/ t yellow?

url https://scied.ucar.edu/image/wavelength-blue-and-red-light-image [20210426]
This diagram shows the relative wavelengths of blue light and red light waves. Blue light has shorter waves, with wavelengths between about 450 and 495 nanometers. Red light has longer waves, with wavelengths around 620 to 750 nm. Blue light has a higher frequency and carries more energy than red light. The wavelengths of light waves are very, very short, just a few 1/100,000ths of an inch.
blue: 450-495 nm
red: 620-750 nm

url https://www.britannica.com/science/color/The-visible-spectrum
yellow: 580 nm
green: 550 nm
cyan: 500 nm
*Typical values only.

url https://www.quora.com/What-colour-will-form-when-red-yellow-and-blue-are-mixed

{% endcomment %}
