---
layout: post
author: viridi
title: function intro
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: python
date: 2021-01-10 21:23:00 +07
tags: ["function"]
permalink: /code/py/function-intro
---
Brief introduction to function in Python with an example is presented here.


## function
How a varying quantity depends on another quantity can be represented in a function [[1](#ref1)], e.g. $y$ depends on $x$

\begin{equation}
\label{fintro-function}
y = f(x)
\end{equation}

and it may also be said, in this case, that $x$ is independent variable, while $y$ is dependent variable [[2](#ref2)].


## code
In Python we can define a function [[3](#ref3)] as follow

```python
def function_name(argument):
	# Relate the argument (as input) with processed_value (as output)
	processed_value = argument
	return processed_value
```

which is only an illustration.


## example
..


## note
Function name should represent purpose of the function and argument(s) should be defined to give a clear description and usage of the function.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Function (mathematics)", Wikipedia, The Free Encyclopedia, 9 Jan 2021, 17:09 UTC, <https://en.wikipedia.org/w/index.php?oldid=999330249> [20210110].
2. <a name="ref2"></a>Wikipedia-Autoren, "Abhängige und unabhängige Variable", Wikipedia, Die freie Enzyklopädie, 1 Dez 2020, 17:28 UTC, <https://de.wikipedia.org/w/index.php?oldid=206134794> [20210110].
3. <a name="ref3"></a>-, "Python Functions", W3Schools, url <https://www.w3schools.com/python/python_functions.asp> [20210110].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/code/py/2021-01-10-function-intro.md)
