---
layout: soal
author: viridi
title: "0281"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["heat conduction", "fourier's law", "steady state", "fi3201", "2020-2"]
date: 2021-04-22 06:57:00 +07
permalink: /0281
src: https://github.com/dudung/soal/commits/master/_posts/0/28/2021-04-22-fourier-law-hc-fd-2d-1.md
ref: https://dx.doi.org/10.1615/AtoZ.c.conduction
---
Laju perubahan energi yang diperoleh (atau hilang) pada arah $x$ yang menembus suatu luasan $dA = dydz$ diberikan oleh

\begin{equation}\label{eqn:0281-1}
\left( \frac{Q}{\Delta t} \right) \_x = (q_x - q_{x + dx}) (dy dz).
\end{equation}

Ekspansi deret Fourier memberikan

\begin{equation}\label{eqn:0281-2}
f(x + dx) \approx f(x) + \frac{\partial f}{\partial x} dx,
\end{equation}

yang dapat memberikan

\begin{equation}\label{eqn:0281-3}
f(x) - f(x + dx) \approx  - \frac{\partial f}{\partial x} dx,
\end{equation}

sehingga membuat Persamaan \eqref{eqn:0281-1} menjadi

\begin{equation}\label{eqn:0281-4}
\left( \frac{Q}{\Delta t} \right)_x = \left( - \frac{\partial q_x}{\partial x} dx \right) (dy dz) = - \frac{\partial q_x}{\partial x} dV,
\end{equation}

di mana $dV = dA dx = dx dy dz$. Dengan demikian untuk suatu volume kontrol $dV$ kontribusi dari ketiga arah $x$, $y$, dan $z$ akan menjadi

\begin{equation}\label{eqn:0281-5}
\frac{Q}{\Delta t} = - \left( \frac{\partial q_x}{\partial x} + \frac{\partial q_y}{\partial y} + \frac{\partial q_z}{\partial z} \right) dV.
\end{equation}

Hukum Fourier tentang konduksi panas memberikan

\begin{equation}\label{eqn:0281-6}
q_x = - \kappa \frac{\partial T}{\partial x}, \ \ \ \ q_y = - \kappa \frac{\partial T}{\partial y}, \ \ \ \ q_z = - \kappa \frac{\partial T}{\partial z},
\end{equation}

dengan $\kappa$ konduktivitas termal bahan ($\rm W \cdot m^{-1} \cdot K^{-1}$). Substitusi ketiga persamaan dalam Persamaan \eqref{eqn:0281-6} ke Persamaan \eqref{eqn:0281-5} akan memberikan

\begin{equation}\label{eqn:0281-7}
\begin{array}{rcl}
\displaystyle \frac{Q}{\Delta t} & = & \displaystyle - \left[ \frac{\partial}{\partial x} \left( -\kappa \frac{\partial T}{\partial x} \right) + \frac{\partial}{\partial y} \left( -\kappa \frac{\partial T}{\partial y} \right) + \frac{\partial}{\partial z} \left( -\kappa \frac{\partial T}{\partial z} \right) \right] dV \newline
& = & \displaystyle \kappa \left( \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} + \frac{\partial^2 T}{\partial z^2} \right) dV,
\end{array}
\end{equation}

dengan asumsi konduktivitas termal bahan $\kappa$ invarian terhadap arah atau isotropik. Selanjutnya, suatu bahan yang akan mendapatkan (atau melepas) energi panas bila temperaturnya berubah sebesar $\Delta T$, perubahan energi bahan adalah

\begin{equation}\label{eqn:0281-8}
Q = m c \Delta T \approx (\rho dV) c \Delta T,
\end{equation}

dengan $m$ massa ($\rm kg$), $c$ kalor jenis ($\rm J \cdot kg^{-1} \cdot K^{-1}$), $\rho$ rapat massa per satuan volume ($\rm kg \cdot m^{-3}$), dan $dV$ elemen volume kontrol ($\rm m^3$) yang bermassa $m$. Substitusi Persamaan \eqr{eqn:0281-8} ke \eqref{eqn:0281-7} akan memberikan

\begin{equation}\label{eqn:0281-9}
\begin{array}{rcl}
\displaystyle \frac{\Delta T}{\Delta t} \rho c \ dV & = & \displaystyle \kappa \left( \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} + \frac{\partial^2 T}{\partial z^2} \right) dV, \newline
\displaystyle \frac{\Delta T}{\Delta t} & = & \displaystyle \frac{\kappa}{\rho c} \left( \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} + \frac{\partial^2 T}{\partial z^2} \right), \newline
& = & \alpha \nabla^2 T,
\end{array}
\end{equation}

yang untuk pengamatan dalam setiap selang waktu $\Delta t $ kecil akan mejadi

\begin{equation}\label{eqn:0281-A}
\frac{\partial T}{\partial t} = \alpha \nabla^2 T, 
\end{equation}

dengan $\alpha$ termal difusivitas ($\rm m^2 \cdot s^{-1}$). Secara umum $T = T(x, y, z, t)$. Untuk keadaan tunak Persamaan \eqref{eqn:0281-A} akan menjadi

A | $\displaystyle \frac{\partial^2 T}{\partial x^2} = 0$.
B | $\displaystyle \frac{\partial^2 T}{\partial y^2} = 0$.
C | $\displaystyle \frac{\partial^2 T}{\partial z^2} = 0$.
D | $\displaystyle \frac{\partial^2 T}{\partial x^2} +  \frac{\partial^2 T}{\partial y^2} +  \frac{\partial^2 T}{\partial z^2} = 0$.
E | bukan salah satu dari persamaan di atas.

