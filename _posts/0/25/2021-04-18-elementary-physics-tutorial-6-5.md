---
layout: soal
author: viridi
title: "0255"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "sound intensity", "dB", "treshold of hearing", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-18 03:05:00 +07
permalink: /0255
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-18-elementary-physics-tutorial-6-5.md
ref: http://hyperphysics.phy-astr.gsu.edu/hbase/Sound/db.html
---
Seekor nyamuk pada jarak $5 \ \rm m$ menghasilkan suara dengan intensitas mendekati batas ambang pendengaran manusia ($0 \ \rm dB$). Tingkat intensitas (dalam $\rm dB$) dari $200$ nyamuk sejenis adalah

A | $\ \rm dB$.
B | $\ \rm dB$.
C | $\ \rm dB$.
D | $\ \rm dB$.
E | $\ \rm dB$.


## &nbsp;
Intensitas bunyi dapat dinyatakan dalam desibel ($\rm dB$) di atas standar ambang pendengaran $I_0$ dalam bentuk

\begin{equation}\label{eqn:0255-0}
{\rm TI} = I ({\rm dB}) = 10 \log_{10} \left( \frac{I}{I_0} \right),
\end{equation}

dengan intensitas bunyi $I$ dapat diperoleh dari

\begin{equation}\label{eqn:0255-1}
I = \frac{P}{A},
\end{equation}

di mana $P$ adalah daya sumber bunyi dan $A$ adalah luas permukaan pemancar bunyi, yang umumnya digunakan berbentuk permukaan bola

\begin{equation}\label{eqn:0255-2}
A = 4\pi r^2.
\end{equation}

Untuk intesitas ambang pendengaran $I_0$ akan terdapat $P_0$ dengan menggunakan Persamaan \eqref{eqn:0255-1}. Intensitas bunyi pada jarak $r_1$ dari suatu sumber bunyi adalah $I_1$

\begin{equation}\label{eqn:0255-3}
I_1 = \frac{P}{4\pi r_1^2},
\end{equation}

akan menjadi $I_2$ pada jarak $r_2$

\begin{equation}\label{eqn:0255-4}
I_2 = \frac{P}{4\pi r_2^2}.
\end{equation}

Dengan menggunakan Persamaan \eqref{eqn:0255-0} dan \eqref{eqn:0255-2} dapat dituliskan

\begin{eqnarray}
\nonumber {\rm TI}\_1 = 10 \log_{10} \left( \frac{I_1}{I_0} \right) = 10 \log_{10} \left( \frac{P}{4\pi I_0} \right) - 20 \log_{10} (r_1), \newline
\nonumber {\rm TI}\_2 = 10 \log_{10} \left( \frac{I_1}{I_0} \right) = 10 \log_{10} \left( \frac{P}{4\pi I_0} \right) - 20 \log_{10} (r_2), \newline
\nonumber {\rm TI}\_1 + 20 \log_{10} (r_1) = {\rm TI}\_2 + 20 \log_{10} (r_2), \newline
\label{eqn:0255-5} {\rm TI}\_2 = {\rm TI}\_1 + 20 \log_{10} \left( \frac{r_1}{r_2} \right).
\end{eqnarray}

Bila $P_1 = P$ dan $P_2 = NP$ sehingga $I_2 = N I_1$, sumber awal digandakan sebanyak $N$ buah, dapat pula diperoleh

\begin{eqnarray}
\nonumber {\rm TI}\_1 = 10 \log_{10} \left( \frac{I_1}{I_0} \right), \newline
\nonumber {\rm TI}\_2 = 10 \log_{10} \left( \frac{N I_1}{I_0} \right) = 10 \log_{10} \left( \frac{I_1}{I_0} \right) + 10 \log_{10} (N), \newline
\label{eqn:0255-6} {\rm TI}\_2 = {\rm TI}\_1 + 10 \log_{10} (N).
\end{eqnarray}

Kemungkinan lain adalah pengamat mengubah jaraknya dari $r_1$ menjadi $r_2$ dengan $r_2 > r_1$ dan jumlah sumber digandakan dari $N_1$ menjadi $N_2$ dengan $N_2 > N_1$ maka dapat diperoleh

\begin{equation}\label{eqn:0255-7}
{\rm TI}\_2 = {\rm TI}\_1 + 10 \log_{10} \frac{N_2}{N_1} + 20 \log_{10} \left( \frac{r_1}{r_2} \right).
\end{equation}

Dengan demikian bila jumlah $N > >$ maka $\rm TI > >$, akan tetapi bila jarak $r > >$ maka $\rm TI < <$.

Selanjutnya untuk seekor nyamuk $N_1 = 1$ dengan $r_1 = 5 \ \rm m$ dapat diperoleh

\begin{equation}\label{eqn:0255-8}
I_0 = I_1 = \frac{N_1 P_0}{4\pi r_1^2},
\end{equation}

sehingga untuk $N_2 = 200$ nyamuk akan menjadi

\begin{equation}\label{eqn:0255-9}
I_2 = \frac{N_2 P_0}{4\pi r_1^2} = \left( \frac{N_2}{N_1} \right) I_0,
\end{equation}

yang dengan Persamaan \eqref{eqn:0255-6} akan menjadi

{\rm TI}\_2 = {\rm TI}\_1 + 10 \log_{10} (N).


