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
Saat tiba pada sebuah antena TV berdiameter $D$ intensitas rata-rata suatu sinyal TV dalah $I_{\rm avg}$, di mana sinyal TV merupakan suatu gelombang elektromagnetik (EM). Dalam selang waktu $\Delta t$ dapat diperoleh total energi $U_{\rm total}$ yang diterima oleh antena dari sinyal tersebut. Pengamatan dilakukan selama $\Delta t =  4 \ \rm jam$ untuk gelombang sinyal TV dengan intensitas rata-rata $I_{\rm avg} = 1.0 \times 10^{−13} \ \rm W/m^2$ dan diameter antena $D = 33 \ \rm cm$. Amplitudo medan listrik $E_0$ dan amplitudo medan magnetik $B_0$ dari gelombang EM tersebut, serta energi total yang diterima antena TV adalah

A | $2.8924 \times 10^{-6} \ \rm N/C$, $8.6772 \times 10^{-14} \ \rm T$, $1.2316 \times 10^{-10}\ \rm J$.
B | $8.6772 \times 10^{-6} \ \rm N/C$, $2.8924 \times 10^{-14} \ \rm T$, $1.2316 \times 10^{-10}\ \rm J$.
C | $8.6772 \times 10^{-6} \ \rm N/C$, $1.2316 \times 10^{-14} \ \rm T$, $2.8924 \times 10^{-10}\ \rm J$.
D | $1.2316 \times 10^{-6} \ \rm N/C$, $2.8924 \times 10^{-14} \ \rm T$, $8.6772 \times 10^{-10}\ \rm J$.
E | $1.2316 \times 10^{-6} \ \rm N/C$, $8.6772 \times 10^{-14} \ \rm T$, $2.8924 \times 10^{-10}\ \rm J$.


## &nbsp;
Luas suatu penampang lingkaran berdiameter $D$ adalah

\begin{equation}\label{eqn:258-0}
A = \tfrac14 \pi D^2.
\end{equation}

Hubungan antara energi total $U_{\rm total}$ dan daya rata-rata $P_{\rm avg}$ adalah

\begin{equation}\label{eqn:258-1}
U_{\rm total} = P_{\rm avg} \Delta t,
\end{equation}

dengan $\Delta t$ adalah durasi pengamatan. Untuk medan EM, di mana gelombang sinyal TV termasuk di dalamnya, intensitas rata-ratanya diberikan oleh

\begin{equation}\label{eqn:258-2}
I_{\rm avg} = \frac{P_{\rm avg}}{A},
\end{equation}

dengan $A$ adalah luas area yang dilalui gelombang EM tersebut atau dalam kasus ini adalah luas penampang antena penerima sinyal TV. Selain itu, terkait dengan amplitudo medan listrik $E_0$ dan amplitudo medan magnetiknya $B_0$, terdapat pula rumusan intensitas rata-rata dalam bentuk

\begin{equation}\label{eqn:0258-3}
I_{\rm avg} = \frac12 c \epsilon_0 E_0^2,
\end{equation}

\begin{equation}\label{eqn:0258-4}
I_{\rm avg} = \frac12 \frac{c}{\mu_0} B_0^2,
\end{equation}

atau 

\begin{equation}\label{eqn:0258-5}
I_{\rm avg} = \frac12 \frac{1}{\mu_0} B_0 E_0,
\end{equation}

dengan permitivitas vakum $\epsilon_0 = 8.8542 \times 10^{-12} \ \rm F/m$ dan permeabilitas vakum $\mu_0 = 1.2566 \times 10^{-6} \ \rm H/m$. Dengan demikian dapat diperoleh

\begin{eqnarray}
\label{eqn:0258-6} E_0 = \sqrt{\frac{2 I_{\rm avg}}{c \epsilon_0}}, \newline
\label{eqn:0258-7} B_0 = \frac{E_0}{c}, \newline
\label{eqn:0258-8} U_{\rm total} = P_{\rm avg} \Delta t = I_{\rm avg} A \Delta t.
\end{eqnarray}

Dengan Persamaan \eqref{eqn:0258-6}, \eqref{eqn:0258-7}, dan \eqref{eqn:0258-8} serta kode Python berikut, dapat diperoleh amplitudo medan listrik, amplitudo medan magnetik, dan energi total yang diterima antena.

<iframe src="https://trinket.io/embed/python/dbdb36ffc6" width="100%" height="280" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
