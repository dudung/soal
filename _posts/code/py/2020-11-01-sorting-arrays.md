---
layout: post
author: viridi
title: sorting arrays
mathjax: false
ptext: false
x3dom: false
threejs: false
oo: false
category: python
date: 2020-11-01 12:55:00 +07
tags: ["topics"]
permalink: /code/py/sorting-arrays
---
In Python sorting arrays can be performed manually with iteration, e.g. using selection sort [[1](#ref1)], or simply with the sort() method provided by Python or even sorted() function, where the former changes the list directy and does not return any value, while the later does not change the list and return the sorted list [[2](#ref2)].

## Code
Three examples and their result are given as follow.

### Iteration
```python
# Create an array, sort, find its min, max, med (all manually)
x = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
print("init =", x)
N = len(x)
print("N =", N)
for i in range(0, N - 1):
	for j in range(i + 1, N):
		if x[i] > x[j]:
			x[i], x[j] = x[j], x[i]
print("sort =", x)
```

whose result is

```batch
init = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
N = 17
sort = [0, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9]
```

### sort() method
```python
# Create an array, sort using sort() method
y = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
print("init =", y)
y.sort()
print("sort =", y)
```

whose result is

```batch
init = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
sort = [0, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9]
```

### sorted() function
```python
# Create an array, sort using sorted() function
z = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
a = sorted(z)
print("init =", z)
print("sort =", a)
```

whose result is

```batch
init = [9, 1, 9, 2, 3, 3, 1, 5, 7, 9, 6, 5, 4, 4, 8, 6, 0]
sort = [0, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9]
```


## References
1. <a name="ref1"></a>Wikipedia contributors, "Selection sort", Wikipedia, The Free Encyclopedia, 20 Sep 2020, 03:48 UTC, <https://en.wikipedia.org/w/index.php?oldid=979325950> [20201101].
2. <a name="ref2"></a>-, "Python List sort()", Programiz, Parewa Labs, url <https://www.programiz.com/python-programming/methods/list/sort> [20201101].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/code/py/2020-11-01-sorting-arrays.md)
