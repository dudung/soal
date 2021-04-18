---
layout: soal
author: viridi
title: "0257"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "electromagnetic", "energy", "average power", "laser", "pulse", "magnetic field", "electric field", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-18 17:33:00 +07
permalink: /0257
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-18-elementary-physics-tutorial-6-7.md
ref: https://en.wikipedia.org/wiki/Laser#Examples_by_power
---
Selama selang waktu $\Delta t$ sebuah laser bernergi tinggi mengeluarkan pulsa dengan daya rata-rata $P_{\rm avg}$. Sinar yang keluar dapat dianggap berbentuk silinder dengan jari-jari $R$. Bila $\Delta t = 1 \ \rm ns$, $P_{\rm avg} = 1.5 \times 10^{11} \ \rm W$, dan $R = 2.2 \times 10^{-3} \ \rm m$ dapat dihitung energi tiap pulsa $U_{\rm laser}$ dan nilai rms medan listriknya $E_{\rm rms}$, yaitu

A | $150 \ \rm J$ dan $1.7219 \times 10^9 \ \rm N/C$.
B | $192 \ \rm J$ dan $1.2971 \times 10^9 \ \rm N/C$.
C | $150 \ \rm J$ dan $1.9271 \times 10^9 \ \rm N/C$.
D | $192 \ \rm J$ dan $1.9271 \times 10^9 \ \rm N/C$.
E | $150 \ \rm J$ dan $2.9171 \times 10^9 \ \rm N/C$.


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