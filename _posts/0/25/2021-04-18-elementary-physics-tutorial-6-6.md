---
layout: soal
author: viridi
title: "0256"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "electromagnetic", "energy", "average power", "average intensity", "amplitude", "magnetic field", "electric field", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-18 17:15:00 +07
permalink: /0256
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-18-elementary-physics-tutorial-6-6.md
ref: https://courses.lumenlearning.com/physics/chapter/24-4-energy-in-electromagnetic-waves/
---
Terdapat suatu gelombang elektromagnetik (EM) dengan amplitudo medan magnetik $B$ adalah $B_0 = 2.2 \times 10^{-7} \ \rm T$. Amplitudo medan listrik $E$ dan daya rata-rata $P_{\rm avg}$ pada suatu luas penampang akibat gelombang EM ini adalah

A | $66 \ \rm N/C$ dan $7.5853 \ \rm W$.
B | $60 \ \rm N/C$ dan $5.7853 \ \rm W$.
C | $66 \ \rm N/C$ dan $5.3857 \ \rm W$.
D | $60 \ \rm N/C$ dan $7.5853 \ \rm W$.
E | $66 \ \rm N/C$ dan $5.7853 \ \rm W$.


## &nbsp;
Untuk suatu gelombang elektro magnetik (EM) terdapat hubungan antara medan listrik $E$ medan magnetik $B$ dalam bentuk

\begin{equation}\label{eqn:0256-0}
E = c B
\end{equation}

yang berimplikasi juge hubungan antara amplitudo kedua medan tersebut

\begin{equation}\label{eqn:0256-1}
E_0 = c B_0.
\end{equation}

Intensitas rata-rata suatu gelombang EM dapat diperoleh melalui

\begin{equation}\label{eqn:0256-2}
I_{\rm avg} = \frac12 c \epsilon_0 E_0^2,
\end{equation}

\begin{equation}\label{eqn:0256-3}
I_{\rm avg} = \frac12 \frac{c}{\mu_0} B_0^2,
\end{equation}

atau 

\begin{equation}\label{eqn:0256-4}
I_{\rm avg} = \frac12 \frac{1}{\mu_0} B_0 E_0,
\end{equation}

yang merupakan daya rata-rata $P_{\rm avg}$ per satuan luas $A$

\begin{equation}\label{eqn:0256-5}
I_{\rm avg} = \frac{P_{\rm avg}}{A}.
\end{equation}

Antara permitivitas vakum $\epsilon_0 = 8.8542 \times 10^{-12} \ \rm F/m$ dan permeabilitas vakume $\mu_0 = 1.2566 \times 10^{-6} \ \rm H/m$ terdapat hubungan

\begin{equation}\label{eqn:0256-6}
\epsilon_0 \mu_0 = \frac{1}{c^2}, 
\end{equation}

dengan $c \approx 3 \times 10^8 \ \rm m/s$ adalah laju rambat cahaya dalam vakum. Dengan Persamaan \eqref{eqn:0256-1}, $A = 1 \ \rm m^2$ dan Persamaan \eqref{eqn:0256-5}, serta kode Python berikut, dapat dihitung $B_0$ dan $P_{\rm avg}$ pada suatu luas penampang.

<iframe src="https://trinket.io/embed/python/44ec36ab7b" width="100%" height="250" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>