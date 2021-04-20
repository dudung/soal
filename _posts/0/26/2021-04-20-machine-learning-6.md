---
layout: soal
author: viridi
title: "0266"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["machine learning", "regression", "numerical solution", "learning type", "learning model", "fi3201", "2020-2"]
date: 2021-04-20 21:29:00 +07
permalink: /0266
src: https://github.com/dudung/soal/commits/master/_posts/0/26/2021-04-20-machine-learning-6.md
ref: https://www.toptal.com/machine-learning/machine-learning-theory-an-introductory-primer
---
Regresi merupakan salah satu permasalahan dalam machine learning (ML) dengan cara belajar supervised learning. Untuk satu variabel bebas $x$ dan satu variabel terikat $y$ suatu prediktor dalam bentuk

\begin{equation}\label{eqn:0265-0}
y = a + bx,
\end{equation}

nilai $a$ dan $b$ dapat diperoleh menggunakan regresi linier. Bila terdapat pasangan data $\\{(x_i, y_i) \ \| \ i = 1, 2, .., N \\}$ nilai $a$ dan $b$ dapat diperoleh menggunakan least square yang menghasilkan

\begin{equation}\label{eqn:0265-1}
a = \frac{\sum_{i = 1}^N y_i \sum_{i = 1}^N x_i^2 - \sum_{i = 1}^N x_i \sum_{i = 1}^N x_i y_i}{N \sum_{i = 1}^N x_i^2 - \left( \sum_{i = 1}^N x_i \right)^2}
\end{equation}

dan

\begin{equation}\label{eqn:0265-2}
b = \frac{N \sum_{i = 1}^N {x_i y_i} - \sum_{i = 1}^N x_i \sum_{i = 1}^N y_i}{N \sum_{i = 1}^N x_i^2 - \left( \sum_{i = 1}^N x_i \right)^2}.
\end{equation}

Kesalahan antara data dan prediktor diberikan oleh

\begin{equation}\label{eqn:0265-3}
\varepsilon = \sum_{i = 1}^N (a + b x_i - y_i)^2.
\end{equation}

Persamaan \ref{eqn:0265-1} dan \ref{eqn:0265-2} diperoleh dengan menggunakan Persamaan \eqref{eqn:0265-3} melalui

\begin{equation}\label{eqn:0265-4}
\frac{\partial \varepsilon}{\partial a} = 0, \ \ \ \ \frac{\partial \varepsilon}{\partial b} = 0.
\end{equation}

Untuk ML nilai $a$ dan $b$ diubah dengan gradient descent melalui

\begin{equation}\label{eqn:0265-5}
a^+ = a - \eta \frac{\partial \varepsilon}{\partial a}
\end{equation}

dan

\begin{equation}\label{eqn:0265-6}
b^+ = b - \eta \frac{\partial \varepsilon}{\partial b}
\end{equation}

dengan $\eta$ adalah laju belajar. Indeks atas $+$ menunjukkan nilai baru dari kedua parameter, yang diubah agar kesalahan $\varepsilon$ berkurang. Idealnya akan tercapai nilai $a$ dan $b$ seperti pada Persamaan \eqref{eqn:0265-1} dan \eqref{eqn:0265-2}, yang tak lain adalah $a^+$ dan $b^+$ pada Persamaan \eqref{eqn:0265-5} dan \eqref{eqn:0265-6} saat Persamaan \eqref{eqn:0265-4} terpenuhi. Selanjutnya, Persamaan \eqref{eqn:0265-5} dan \eqref{eqn:0265-6} dapat dihitung menggunakan kode Python berikut.

<iframe src="https://trinket.io/embed/python/d25081cc80" width="100%" height="390" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

x | 0 | 1 | 2 | 3 | 4 | 5
y | 0.5 | 2.5 | 4.5 | 6.5 | 8.5 | 10.5

Nilai $\varepsilon$, $b$, dan $a$ untuk data di atas adalah

A | $0.5$, $2$, $3.79\times 10^{-16}$.
B | $3.79\times 10^{-16}$, $2$, $0.5$.
C | $2$, $3.79\times 10^{-16}$, $0.5$.
D | $2$, $0.5$, $3.79\times 10^{-16}$.
E | $0.5$, $3.79\times 10^{-16}$, $2$.
