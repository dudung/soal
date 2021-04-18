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
date: 2021-04-19 03:25:00 +07
permalink: /0259
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-18-elementary-physics-tutorial-6-9.md
ref: https://en.wikipedia.org/wiki/Polarizer#Malus's_law_and_other_properties
---
Terdapat tiga pasang susunan keping polarisator-analisator sebagai berikut ini.

ID | Konfigurasi 
TOP | ![]({{site.baseurl}}/assets/img/0/25/0259f.png)
MID | ![]({{site.baseurl}}/assets/img/0/25/0259d.png)
BOT | ![]({{site.baseurl}}/assets/img/0/25/0259e.png)

Sinar datang dengan intensitas $I_0$ tidak terpolarisasi dan berintensitas rata-rata $I_{\rm avg}$. Intensitas rata-rata $I_1$ dan $I_2$ adalah setelah lewat keping polarisator dan analisator, berturut-turut. Bila $I_0 = 48 \ \rm W/m^2$, nilai $I_2$ untuk masing-masing pasangan pada gambar sebelumnya (TOP: atas, MID: tengah, BOT: bawah) adalah

A | $0 \ \rm W/m^2$, $18 \ \rm W/m^2$, $24 \ \rm W/m^2$.
B | $18\ \rm W/m^2$, $0 \ \rm W/m^2$, $24 \ \rm W/m^2$.
C | $18 \ \rm W/m^2$, $24 \ \rm W/m^2$, $0 \ \rm W/m^2$.
D | $24\ \rm W/m^2$, $18 \ \rm W/m^2$, $0 \ \rm W/m^2$.
E | $24 \ \rm W/m^2$, $0 \ \rm W/m^2$, $18 \ \rm W/m^2$.


## &nbsp;
Terdapat pasangan susuna keping polarisator-analisator sebagai berikut ini.

![]({{site.baseurl}}/assets/img/0/25/0259.png)

Berkas tak terpolarisasi dengan intesitas rata-rata $I_0$ saat melewati keping polarisator akan memberikan

\begin{equation}\label{eqn:259-0}
I_1 = \tfrac12 I_0.
\end{equation}

Dan setelah lewat keping analisator akan diperoleh

\begin{equation}\label{eqn:259-1}
I_2 = I_1 \cos^2 (\theta_2 - \theta_1).
\end{equation}

menurut hukum Malus. Untuk ketiga kasus sebelumnya dapat diresumekan.

Kasus | $\theta_1$ | $\theta_2$
:-: | :-: | :-:
TOP | $30 \rm ^\circ$ | $30 \rm ^\circ$
MID | $-30 \rm ^\circ$ | $60 \rm ^\circ$
BOT | $-60 \rm ^\circ$ | $-30 \rm ^\circ$

Dengan Persamaan \eqref{eqn:259-0} dan \eqref{eqn:259-1}, informasi dari tabel, dan kode Python berikut, dapat diperoleh intesitas rata-rata setelah lewat keping analisator atau $I_2$.

<iframe src="https://trinket.io/embed/python/05f234cc7f" width="100%" height="280" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
