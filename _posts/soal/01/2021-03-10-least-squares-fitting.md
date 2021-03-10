---
layout: soal
author: viridi
title: "0013"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fitting", "least squares", "python"]
date: 2021-03-10 16:27:00 +07
permalink: /soal/0013
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/01/2021-03-10-list-square-fitting.md
ref: https://mathworld.wolfram.com/LeastSquaresFitting.html
---
Terdapat pasangan data $\\{(x_i, y_i) \ \| \ i = 1, 2, \dots, N \\}$ yang dapat dimodelkan dengan persamaan

\begin{equation} \nonumber
f(x, a, b) = a + bx,
\end{equation}

dengan $a$ dan $b$ adalah koefisien yang akan ditentukan menggunakan deviasi vertikal untuk seluruh titik data

\begin{equation} \nonumber
R^2 = \sum_{i = 1}^N [y_i - f(x_i, a, b)]^2
\end{equation}

yang diminimumkan melalui

\begin{equation} \nonumber
\frac{\partial}{\partial a}(R^2) = 0
\end{equation}

dan

\begin{equation} \nonumber
\frac{\partial}{\partial b}(R^2) = 0.
\end{equation}

Dengan $\bar{x}$ dan $\bar{y}$, yang merupakan rata-rata nilai $x$ dan $y$, dapat dihitung jumlah kuadrat (sum of squares, SS)

\begin{equation} \nonumber
\begin{array}{c}
{\rm SS} _{xx} = \sum _{i = 1}^N (x_i - \bar{x})^2, \newline
{\rm SS} _{yy} = \sum _{i = 1}^N (y_i - \bar{y})^2, \newline
{\rm SS} _{xy} = \sum _{i = 1}^N (x_i - \bar{x})(y_i - \bar{y}).
\end{array}
\end{equation}

Koefisien regresi $b$ dan konstanta $a$, serta koefisien korelasi $r^2$ dapat diperoleh melalui

<ol type="A">
<li>$\displaystyle \frac{ {\rm SS} _{xy} }{ {\rm SS} _{xx} }$ dan $\bar{y} - b \bar{x}$, serta $\displaystyle \frac{ {\rm SS} _{xy}^2}{ {\rm SS} _{xx} {\rm SS} _{yy} }$.
<li>$\displaystyle \frac{ {\rm SS} _{xy} }{ {\rm SS} _{xx} }$ dan $\bar{y} + b \bar{x}$, serta $\displaystyle \frac{ {\rm SS} _{xy}^2}{ {\rm SS} _{xx} {\rm SS} _{yy} }$.
<li>$\displaystyle \frac{ {\rm SS} _{xx} }{ {\rm SS} _{xy} }$ dan $\bar{y} - b \bar{x}$, serta $\displaystyle \frac{ {\rm SS} _{xy}^2}{ {\rm SS} _{xx} {\rm SS} _{yy} }$.
<li>$\displaystyle \frac{ {\rm SS} _{yy} }{ {\rm SS} _{xx} }$ dan $\bar{y} - b \bar{x}$, serta $\displaystyle \frac{ {\rm SS} _{xy}^2}{ {\rm SS} _{xx} {\rm SS} _{yy} }$.
<li>$\displaystyle \frac{ {\rm SS} _{yy} }{ {\rm SS} _{xy} }$ dan $\bar{y} + b \bar{x}$, serta $\displaystyle \frac{ {\rm SS} _{xy}^2}{ {\rm SS} _{xx} {\rm SS} _{yy} }$.
