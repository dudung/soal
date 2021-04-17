---
layout: soal
author: viridi
title: "0253"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "sound", "arrival time", "path difference", "distance travelled" "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-17 21:48:00 +07
permalink: /0253
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-17-elementary-physics-tutorial-6-3.md
ref: http://hyperphysics.phy-astr.gsu.edu/hbase/Sound/souspe.html#c1
---
Terdapat dua buah mikrofon $M_1$ dan $M_2$ yang diletakkan pada jarak $L_1$ dan $L_2$ dari suatu sumber bunyi $S$ berupa speaker sebagaimana diilustrasikan dalam gambar berikut ini.

![]({{site.baseurl}}/assets/img/0/25/0253.png)

Jarak pisah kedua mikrofon adalah $1.5 \ \rm m$. Cepat rambat bunyi di udara pada suatu keadaaan adalah $343 \ \rm m/s$. Mikrofon $M_2$ menangkap terlebih dahulu bunyi yang berasal sumber bunyi $S$ dan baru $1.46 \ \rm ms$ kemudian bunyi yang sama mencapai mikrofon $M_1$. Besarnya $L_2$ dan $L_1$ adalah

A | $4.297\ \rm m$ dan $9.196\ \rm m$.
B | $2.497\ \rm m$ dan $1.996\ \rm m$.
C | $1.996\ \rm m$ dan $2.497\ \rm m$.
D | $2.497\ \rm m$ dan $4.297\ \rm m$.
E | $1.996\ \rm m$ dan $4.297\ \rm m$.


## &nbsp;
Gelombang bunyi dengan laju $v$ akan menempuh jarak

\begin{equation}\label{eqn:0253-0}
s = v t
\end{equation}

dalam waktu $t$. Bila terdapat dua pendengar (pengamat, mikrofon) yang terletak pada jarak $s_1$ dan $s_2 > s_1$ maka pada masing-masing pendengar gelombang bunyi akan sampai pada waktu

\begin{equation}\label{eqn:0253-1}
t_1 = \frac{s_1}{v}
\end{equation}

dan

\begin{equation}\label{eqn:0253-2}
t_2 = \frac{s_2}{v},
\end{equation}

selisih waktu terdengarnya gelombang tersebut pada kedua pendengar adalah

\begin{equation}\label{eqn:0253-3}
\Delta t = t_2 - t_1 = \frac{s_2}{v} - \frac{s_1}{v} = \frac{s_2 - s_1}{v}.
\end{equation}

Untuk kasus pada gambar di atas $L_1 > L_2$ sehingga $t_1 > t_2$ yang akan memberikan

\begin{equation}\label{eqn:0253-4}
\Delta t = t_1 - t_2 = \frac{L_1 - L_2}{v}
\end{equation}

dan dari posisi $M_1$, $M_2$, dan $S$ dapat diperoleh

\begin{equation}\label{eqn:0253-5}
L_1^2 = L_2^2 + H^2.
\end{equation}

Dari Persamaan \eqref{eqn:0253-4} dan \eqref{eqn:0253-5} dapat diperoleh

\begin{eqnarray}
\nonumber L_1^2 = \left( L_1 - v\Delta t  \right)^2 + H^2, \newline
\nonumber 2L_1v\Delta t = v^2(\Delta t)^2 + H^2, \newline
\label{eqn:0253-6} L_1 = \frac{v^2(\Delta t)^2 + H^2}{2v\Delta t}.
\end{eqnarray}

Dengan menggunakan gambar yang telah diberikan sebelumnya dan Persamaan \eqref{eqn:0253-6} serta \eqref{eqn:0253-4} atau \eqref{eqn:0253-5} dapat dihitung $L1$ dan $L_2$ menggunakan kode Python berikut.

<iframe src="https://trinket.io/embed/python/773e9ef63b" width="100%" height="230" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
