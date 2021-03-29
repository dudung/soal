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
date: 2021-03-10 17:16:00 +07
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

untuk pasangan data $\\{(x_i, y_i) \ \| \ i = 1, 2, \dots, N \\}$ dengan

```batch
Data
x =  [1, 2, 3, 4, 5]
y =  [2, 5, 8, 11, 9]

Model
y = a + bx

Least squares fitting
a = 1.0
b = 2.0
r^2 = 0.8
```

adalah keluaran dari program di atas. Bila data terakhir untuk $y$ diganti dari yang semula $9$ menjadi $14$ akan memberikan $a$, $b$, dan $r^2$

<ol type="A">
<li>$1.0$, $2.0$, $0.8$.
<li>$-1.0$, $3.0$, $1.0$.
<li>$1.5$, $2.5$, $0.84$.
<li>$1.0$, $2.0$, $0.9$.
<li>$-1.5$, $2.0$, $1.0$.
