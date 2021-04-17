---
layout: soal
author: viridi
title: "0254"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "doppler effect", "frequency", "constant velocity", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-17 21:55:00 +07
permalink: /0254
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-17-elementary-physics-tutorial-6-4.md
ref: https://en.wikipedia.org/wiki/Doppler_effect#General
---
Terdapat sebuah kereta uap berjalan dengan laju tetap $v$. Saat mendekati pengamat frekuensi peluit kereta uap terdengar sebagai $565 \ \rm Hz$ dan saat menjauhi pengamat terdengar sebagai $486 \ \rm Hz$. Laju kereta uap tersebut adalah

A | $25.7821\ \rm m/s$.
B | $27.5821\ \rm m/s$.
C | $28.7521\ \rm m/s$.
D | $21.7825\ \rm m/s$.
E | $22.7851\ \rm m/s$.


## &nbsp;
Suatu sumber $S$ memancarkan gelombang bunyi dengan frekuensi $f_S$, frekuensi yang didengar oleh seorang observer (pendengar) $O$ akan menjadi

\begin{equation}\label{eqn:0254-0}
f_O = \left( \frac{c \pm v_O}{c \mp v_S} \right) f_S 
\end{equation}

bila sumber, pendengar, atau sumber dan pendengar bergerak. Laju $v_S$ untuk sumber dan $v_O$ untuk observer. Laju rambat rambat bunyi dalam medium (udara) diberikan oleh $c$. Tanda $v_O$ dan $v_S$ disarikan dalam tabel berikut ini.

$v_S$ | $v_O$ | Keadaan | Konsekuensi
:-: | :-: | :--
$0$ | $0$ | Sumber $S$ dan observer $O$ diam | $f_O = f_S$
$-$ | $0$ | Sumber $S$ mendekati observer $O$ yang diam  | $f_O > f_S$
$0$ | $+$ | Sumber $S$ diam dan didekati oleh observer $O$ | $f_O > f_S$
$-$ | $+$ | Sumber $S$ dan observer $O$ saling mendekat | $f_O > f_S$
$+$ | $0$ | Sumber $S$ menjauhi observer $O$ yang diam  | $f_O < f_S$
$0$ | $-$ | Sumber $S$ diam dan dijauhi oleh observer $O$ | $f_O < f_S$
$+$ | $-$ | Sumber $S$ dan observer $O$ saling menjauh | $f_O < f_S$
$-$ | $-$ | Sumber $S$ mendekati observer $O$ yang menjauh | $f_O \gtrsim f_S$
$+$ | $+$ | Sumber $S$ menjauhi observer $O$ yang mendekat | $f_O \lesssim f_S$

Untuk kasus yang diberikan terdapat dua keadaan yang berbeda, yaitu saat kereta uap mendekati pengamat

\begin{equation}\label{eqn:0254-1}
f_1 = \left( \frac{c}{c - v_S} \right) f_S
\end{equation}

dan saat menjauhi pengamat

\begin{equation}\label{eqn:0254-2}
f_2 = \left( \frac{c}{c + v_S} \right) f_S,
\end{equation}

dengan pengamat selalu dalam keadaan diam. Menggunakan Persamaan \eqref{eqn:0254-1} dan \eqref{eqn:0254-2} dapat diperoleh

\begin{eqnarray}
\nonumber f_2 (c + v_S) = f_1 (c - v_S), \newline
\nonumber v_S (f_2 + f_1) = c (f_1 - f_2), \newline
\label{eqn:0254-3} v_S = \left( \frac{f_1 - f_2}{f_1 + f_2} \right) c.
\end{eqnarray}

Persamaan \eqref{eqn:0254-3} dan kode Python berikut akan memberikan nilai laju kereta. Digunakan laju rambat suara pada $20 \ \rm ^\circ C$, yaitu $343 \ \rm m/s$.

<iframe src="https://trinket.io/embed/python/0fbf3418ac" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
