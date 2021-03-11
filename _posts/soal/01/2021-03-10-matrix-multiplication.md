---
layout: soal
author: viridi
title: "0019"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["matrix", "multiplication"]
date: 2021-03-10 19:34:00 +07
permalink: /soal/0019
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/01/2021-03-10-matrix-multiplication.md
ref: https://en.wikipedia.org/w/index.php?oldid=1009455485
---
Terdapat dua matriks berdimensi $M \times P$

\begin{equation} \nonumber
\mathbf{A} = \left[
\begin{array}{cccc}
a_{11} & a_{12} & \dots & a_{1P} \newline
a_{21} & a_{22} & \dots & a_{2P} \newline
\vdots & \vdots & \ddots & \vdots \newline
a_{M1} & a_{M2} & \dots & a_{MP} \newline
\end{array}
\right]
\end{equation}

dan berdimensi $P \times N$

\begin{equation} \nonumber
\mathbf{B} = \left[
\begin{array}{cccc}
b_{11} & b_{12} & \dots & b_{1N} \newline
b_{21} & b_{22} & \dots & b_{2N} \newline
\vdots & \vdots & \ddots & \vdots \newline
b_{P1} & b_{P2} & \dots & b_{PN} \newline
\end{array}.
\right]
\end{equation}

Bila keduanya dikalikan sehingga menghasilkan

\begin{equation} \nonumber
\mathbf{C} = \mathbf{A} \mathbf{B},
\end{equation}

maka untuk setiap elemennya pada matriks $\mathbf{C}$ berlaku bahwa

<ol type="A">
<li>$\displaystyle c_{ij} = \sum_{k = 1}^P a_{ik} \ b_{kj}$.
<li>$\displaystyle c_{ij} = \sum_{k = 1}^P a_{ki} \ b_{jk}$.
<li>$\displaystyle c_{ij} = \sum_{k = 1}^P a_{ik} \ b_{jk}$.
<li>$\displaystyle c_{ij} = \sum_{k = 1}^P a_{ij} \ b_{jk}$.
<li>$\displaystyle c_{ij} = \sum_{k = 1}^P a_{jk} \ b_{ki}$.
