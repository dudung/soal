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
date: 2021-04-24 18:29:00 +07
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
\Delta \phi_{61} = \Delta \phi_{60} - \Delta \phi_{10} = \frac{4\pi}{\lambda} n_2 L.
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
\frac12 \Delta \phi_{61} & = & (m + \frac12) \pi \newline
\displaystyle \tfrac12 \frac{4\pi}{\lambda} n_2 L & = & (m + \frac12) \pi \newline
2 L_m & = & (m + \frac12) \displaystyle \frac{\lambda}{n_2}.
\end{array}
\end{equation}

Tebal minimum tercapai saat $m = 0$ sehingga diperoleh

\begin{equation}\label{eqn:0303-7}
L_0 = \frac14 \frac{\lambda}{n_2} = \frac14 \lambda_2.
\end{equation}

Ketebalan lapisan tipis (film) sebenarnya adalah

\begin{equation}\label{eqn:0303-8}
t = L \cos \theta_2 = L \cos \sin^{-1} \left( \frac{n_1}{n_2} \sin \theta_1 \right).
\end{equation}

Bila digunakan asumsi bahwa $\theta \approx 0$ yang menggambarkan pengamatan hampir tegak lurus lapisan tipis, maka akan diperoleh tebal

\begin{equation}\label{eqn:0303-9}
t = (2m + \tfrac14) \frac{\lambda}{n_2}, \ \ \ \ m = 0, 1, 2, \dots,
\end{equation}

untuk interferensi minimum pada lapisan tipis.
Bila indeks bias kaca kamera adalah $1.55$ dan indeks bias lapisan tipis di atas kaca adalah $1.45$, agar pantulan cahaya monokromatik $580 \ \rm nm$ dari udara ke kaca kamera dapat dicegah, ketebalan minium yang bukan nol dapat dihitung menggunakan kode Python berikut dengan bantuan Persamaan \eqref{eqn:0302-9}.

<iframe src="https://trinket.io/embed/python/66e9a4e38c" width="100%" height="210" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

{% comment %}
Lapisan sabun dengan ketebalan berbeda di tempat berbeda memiliki indeks bias n yang tidak diketahui dan udara di kedua sisinya. Cahaya pantul terlihat beraneka warna. Satu area tampak kuning karena interferensi destruktif telah menghilangkan warna biru (vakum 469 nm) dari cahaya pantul, sedangkan area lain tampak ungu karena interferensi destruktif telah menghilangkan warna hijau (vakum 555 nm). Lapisan memiliki ketebalan minimun t (bukan nol) untuk terjadinya interferensi destruktif. Tentukan rasio t ungu /t kuning?
A soap film with different thicknesses at different places has an unknown refractive index n and air on both sides. In reflected light it looks multicolored. One region looks yellow because destructive interference has removed blue (vacuum 469 nm) from the reflected light, while another looks magenta because destructive interference has removed green (vacuum 555 nm). In these regions the film has the minimum nonzero thickness t required for the destructive interference to occur. Find the ratio t magenta/ t yellow?{% endcomment %}
