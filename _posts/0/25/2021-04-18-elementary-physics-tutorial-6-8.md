---
layout: soal
author: viridi
title: "0258"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "electromagnetic", "energy", "average power", "intensity", "magnetic field", "electric field", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-18 19:59:00 +07
permalink: /0258
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-18-elementary-physics-tutorial-6-8.md
ref: https://courses.lumenlearning.com/physics/chapter/24-4-energy-in-electromagnetic-waves/
---
Saat tiba pada sebuah antena TV berdiameter $D$ intensitas rata-rata suatu sinyal TV dalah $I_{\rm avg}$, di mana sinyal TV merupakan suatu gelombang elektromagnetik (EM). Dalam selang waktu $\Delta t$ dapat diperoleh total energi $U_{\rm total}$ yang diterima oleh antena dari sinyal tersebut. Pengamatan dilakukan untuk $\Delta t =  4 \ \rm jam$. Amplitudo medan listrik $E_0$ dan amplitudo medan magnetik $B_0$ dari gelombang EM tersebut, serta energi total yang diterima antena TV adalah

A | $\ \rm N/C$, $\ \rm T$, $\ \rm J$.
B | $\ \rm N/C$, $\ \rm T$, $\ \rm J$.
C | $\ \rm N/C$, $\ \rm T$, $\ \rm J$.
D | $\ \rm N/C$, $\ \rm T$, $\ \rm J$.
E | $\ \rm N/C$, $\ \rm T$, $\ \rm J$.


## &nbsp;
Daya rata-rata $P_{\rm avg}$ adalah energi $U$ per selang waktu $\Delta t$

\begin{equation}\label{eqn:257-0}
P_{\rm avg} = \frac{U}{\Delta t},
\end{equation}

dengan satuannya masing-masing adalah $\rm W$, $\rm J$, dan $\rm s$. Untuk medan elektromagnetik (EM), di mana laser termasuk di dalamnya, intensitas rata-ratanya diberikan oleh

\begin{equation}\label{eqn:257-1}
I_{\rm avg} = \frac{P_{\rm avg}}{A},
\end{equation}

dengan $A$ adalah luas area yang dilalui gelombang EM tersebut. Selain itu, terkait dengan amplitudo medan listrik $E_0$ dan amplitudo medan magnetiknya $B_0$, terdapat pula rumusan intensitas rata-rata dalam bentuk

\begin{equation}\label{eqn:0257-2}
I_{\rm avg} = \frac12 c \epsilon_0 E_0^2,
\end{equation}

\begin{equation}\label{eqn:0257-3}
I_{\rm avg} = \frac12 \frac{c}{\mu_0} B_0^2,
\end{equation}

atau 

\begin{equation}\label{eqn:0257-4}
I_{\rm avg} = \frac12 \frac{1}{\mu_0} B_0 E_0,
\end{equation}

dengan permitivitas vakum $\epsilon_0 = 8.8542 \times 10^{-12} \ \rm F/m$ dan permeabilitas vakume $\mu_0 = 1.2566 \times 10^{-6} \ \rm H/m$. Hubungan antara amplitudo dan besaran rms adalah melalui

\begin{equation}\label{eqn:0257-5}
E_{\rm rms} = \tfrac12\sqrt{2} E_0,
\end{equation}

misalnya untuk amplituoda medan listrik $E_0$, yang berlalu juga untuk amplitudo medan magnetik $B_0$. Dengan demikian

\begin{eqnarray}
\label{eqn:0257-6} U_{\rm laser} = P_{\rm avg} \Delta t, \newline
\label{eqn:0257-7} E_{\rm rms} = \tfrac12\sqrt{2} E_0 = \tfrac12\sqrt{2} \sqrt{\frac{2 I_{\rm avg}}{c \epsilon_0}} = \sqrt{\frac{P_{\rm avg}}{c \epsilon_0 A}} = \sqrt{\frac{P_{\rm avg}}{c \epsilon_0 \pi R^2}},
\end{eqnarray}

dengan luas penampang

\begin{equation}\label{eqn:0257-8}
A = \pi R^2.
\end{equation}

Kode Python berikut, Persamaan \eqref{eqn:0257-6} dan \eqref{eqn:0257-7} dapat digunakan untuk mendapatkan energi laser dan rms medan listriknya.

<iframe src="https://trinket.io/embed/python/7ea9458717" width="100%" height="260" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>