---
layout: soal
author: viridi
title: "0259"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "electromagnetic", "light", "polarizer", "intensity", "malus law", "analyzer", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-18 21:33:00 +07
permalink: /0259
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-18-elementary-physics-tutorial-6-9.md
ref: https://en.wikipedia.org/wiki/Polarizer#Malus's_law_and_other_properties
---
Terdapat tiga pasang susunan keping polarisator-analisator sebagai berikut ini.

![]({{site.baseurl}}/assets/img/0/25/0259f.png)
![]({{site.baseurl}}/assets/img/0/25/0259d.png)
![]({{site.baseurl}}/assets/img/0/25/0259e.png)

Sinar datang dengan intensitas $I_0$ tidak terpolarisasi dan berintensitas rata-rata $I_{\rm avg}$. Intensitas rata-rata $I_1$ dan $I_2$ adalah setelah lewat keping polarisator dan analisator, berturut-turut. Bila $I_0 = 48 \ \rm W/m^2$, nilai $I_2$ untuk masing-masing pasangan di atas adalah

A | $\ \rm W/m^2$, $\ \rm W/m^2$, $\ \rm W/m^2$.
B | $\ \rm W/m^2$, $\ \rm W/m^2$, $\ \rm W/m^2$.
C | $\ \rm W/m^2$, $\ \rm W/m^2$, $\ \rm W/m^2$.
D | $\ \rm W/m^2$, $\ \rm W/m^2$, $\ \rm W/m^2$.
E | $\ \rm W/m^2$, $\ \rm W/m^2$, $\ \rm W/m^2$.


## &nbsp;

![]({{site.baseurl}}/assets/img/0/25/0259.png)

Berkas tak terpolarisasi dengan intesitas rata-rata $I_0$

\begin{equation}\label{eqn:259-0}
I_1 = \tfrac12 I_0.
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
