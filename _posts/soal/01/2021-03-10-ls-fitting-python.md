---
layout: soal
author: viridi
title: "0014"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fitting", "least squares", "regression coefficient", "correlation coefficient", "python"]
date: 2021-03-10 17:04:00 +07
permalink: /soal/0014
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/01/2021-03-10-list-square-fitting.md
ref: https://mathworld.wolfram.com/LeastSquaresFitting.html
---
Suatu program sederhana dalam bahasa pemrograman Python berikut

```python
def avg(lst):
	return sum(lst) / len(lst)

def SS(a, b):
	aavg = avg(a)
	bavg = avg(b)
	ss = 0;
	N = min(len(a), len(b))
	for i in range(0, N):
		ss += (a[i] - aavg) * (b[i] - bavg)
	return ss

x = [1, 2, 3, 4, 5]
y = [2, 5, 8, 11, 9]
print("Data")
print("x = ", x)
print("y = ", y)
print()

b = SS(x, y) / SS(x, x)
a = avg(y) - b * avg(x)
r2 = SS(x, y) * SS(y, x) / ( SS(x, x) * SS(y, y) )

print("Model")
print("y = a + bx")
print()

print("Least squares fitting")
print("a = ", a, sep="")
print("b = ", b, sep="")
print("r^2 = ", r2, sep="")
```

berfungsi untuk mencari koefisien regresi $b$, konstanta $a$, dan koefisien korelasi $r^2$ dari model

\begin{equation} \nonumber
f(x, a, b) = a + bx,
\end{equation}

untuk pasangan data $\\{(x_i, y_i) \ \| \ i = 1, 2, \dots, N \\}$.

<ol type="A">
<li>$\displaystyle \frac{ {\rm SS} _{xy} }{ {\rm SS} _{xx} }$ dan $\bar{y} - b \bar{x}$, serta $\displaystyle \frac{ {\rm SS} _{xy}^2}{ {\rm SS} _{xx} {\rm SS} _{yy} }$.
<li>$\displaystyle \frac{ {\rm SS} _{xy} }{ {\rm SS} _{xx} }$ dan $\bar{y} + b \bar{x}$, serta $\displaystyle \frac{ {\rm SS} _{xy}^2}{ {\rm SS} _{xx} {\rm SS} _{yy} }$.
<li>$\displaystyle \frac{ {\rm SS} _{xx} }{ {\rm SS} _{xy} }$ dan $\bar{y} - b \bar{x}$, serta $\displaystyle \frac{ {\rm SS} _{xy}^2}{ {\rm SS} _{xx} {\rm SS} _{yy} }$.
<li>$\displaystyle \frac{ {\rm SS} _{yy} }{ {\rm SS} _{xx} }$ dan $\bar{y} - b \bar{x}$, serta $\displaystyle \frac{ {\rm SS} _{xy}^2}{ {\rm SS} _{xx} {\rm SS} _{yy} }$.
<li>$\displaystyle \frac{ {\rm SS} _{yy} }{ {\rm SS} _{xy} }$ dan $\bar{y} + b \bar{x}$, serta $\displaystyle \frac{ {\rm SS} _{xy}^2}{ {\rm SS} _{xx} {\rm SS} _{yy} }$.
