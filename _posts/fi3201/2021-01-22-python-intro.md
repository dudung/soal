---
layout: post
author: viridi
title: python intro
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "python", "intro"]
date: 2021-01-22 06:22:00 +07
permalink: /fi3201/python-intro
---
Some simple examples of python are presented here, including the hello world program [[1](#ref1)]. It is not a realy complete introduction to Python but only a first glance of taste in entering Computational Physics course in beginning of 2021.


## applications
You can use various types of plain text editors, e.g. Notepad++ [[2](#ref2)] to write a Python code. To execute the code we can install Cygwin, which is a large collection of GNU and Open Source tools which provide functionality similar to a Linux distribution on Windows [[3](#ref3)], use online compiler [[4](#ref4)], or install a Python 3 compiler [[5](#ref5)] on your local computer.


## hello world
Look at the following code
```python
# 
# hello.py
# Display 'Hello, world!' in Python 3.7
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3.7 hello.py
# 
# 20210122
# 0647 Create this example, test it, and it works.
# 

print("Hello, world!")
```

that can be executed as

```batch
$ python3.7 hello.py
Hello, world!
```

to produce desired result. In the previous example we can see that the actual line to produce the output is only

```python
print("Hello, world!")
```

where the other lines are comments that are suggested to put in a program to explain the program, e.g. purpose of the program, how to execute the program, what is output of the program, etc.


## for
Using `for` [[6](#ref6)] we will reduce our effort in doing a repetition work.

```python
# 
# for.py
# Use for to display lines of number in Python 3.7
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3.7 for.py
# 
# 20210122
# 0921 Create this example, test it, and it works.
# 

for i in range(1, 10):
	print(i)
```

will produce

```batch
$ python3.7 for.py
1
2
3
4
5
6
7
8
9
```

as executed. Previous result can also be obtained when we use following code

```
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
```

which still works but not so efficient compered to

```python
for i in range(1, 10):
	print(i)
```

Note that there is tabulator or tab charater in front of `print` statement. This tab charater or `\t` must be used in every sub-block in iteration `for` or condition `if`.

## nested for
From now on the comments will not be displayed when they are not so important, in order to focus on the essential lines only. Pay attention to the following code saved as `for-nested.py`

```python
for i in range(1, 5):
	for j in range(1, 4):
		print(i, j)
```

that produces

```python
$ python3.7 for-nested.py
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
4 1
4 2
4 3
```

and `for-nested-3.py`

```python
for i in range(1, 5):
	for j in range(1, 4):
		for k in range(0, 2):
			print(i, j, k)
```

that produces

```python
$ python3.7 for-nested-3.py
1 1 0
1 1 1
1 2 0
1 2 1
1 3 0
1 3 1
2 1 0
2 1 1
2 2 0
2 2 1
2 3 0
2 3 1
3 1 0
3 1 1
3 2 0
3 2 1
3 3 0
3 3 1
4 1 0
4 1 1
4 2 0
4 2 1
4 3 0
4 3 1
```

Can you deduce the funtion of `for` and `range` statements?


## list and for
Using list and `for` in Pyhton, we can have following example

```python
# Define a list
x = [1, 7, 8, 5, 4]

# Get length of the list
N = len(x)

for i in range(0, N, 1):
	print(x[i])
```

that produces

```python
$ python3.7 list-for.py
1
7
8
5
4
```

and

```python
for i in range(0, N):
	print(x[i])
```

that produces

```python
$ python3.7 list-for.py
1
7
8
5
4
```

and

```python
for i in range(N):
	print(x[i])
```

that produces

```python
$ python3.7 list-for.py
1
7
8
5
4
```

and

```python
for i in x:
	print(i)
```

that produces

```python
$ python3.7 list-for.py
1
7
8
5
4
```

In the last example `i` is actualy element of `x` and not only index of `x`. This is a difference that should be noted.


## Exercices
1. What is the ASCII character that we need to put in the beginning of a line to indicate that the line is a comment (not a Python statement)? What about a multi-line commment in Python? Is there any pair of `/*` and `*/`in Python as in C++ language?
2. Explain the use of `range` in a `for` loop. What are the parameters required? What is the minimum number of parameters? Read reference about it [[7](#ref7)], whenever necessary.


## for and if
In the next example we will show the use of `if` in a `for` loop.



## References
1. <a name="ref1"></a>Wikipedia contributors, "'Hello, World!' program", Wikipedia, The Free Encyclopedia, 20 Jan 2021, 01:21 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1001702830> [20210122].
2. <a name="ref2"></a>-, "Notepad++", Version 7.9.2, release Date 2021-01-01, url <https://notepad-plus-plus.org/downloads/> [20210122].
3. <a name="ref3"></a>-, "Cygwin", Version 3.1.6-1, url <https://www.cygwin.com/> [20210122].
4. <a name="ref4"></a>-, "Python Online Compiler", Programiz, url <https://www.programiz.com/python-programming/online-compiler/> [20210122].
5. <a name="ref5"></a>-, "Python Releases for Windows", Latest Python 3 Release - Python 3.9.1, url <https://www.python.org/downloads/windows/> [20210122].
6. <a name="ref6"></a>-, "Python For Loops", W3Schools, url <https://www.w3schools.com/python/python_for_loops.asp. [20210122].
7. <a name="ref7"></a>Vishal Hule, "Python range() function explained with examples", PYnative - Python Programming, 15 Dec 2020, url <https://pynative.com/python-range-function/> [20210122].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-22-python-intro.md)

{% comment %}
Fig. <a href="#fig:x">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/x.png)
<br />
Figure <a name="fig:x">1</a> ...
{: refdef}

1. <a name="ref1"></a> -, "Kinetic Theory of Gases", Glenn Research Center, National Aeronautics and Space Administration, url <https://www.grc.nasa.gov/www/k-12/airplane/kinth.html> [20201210].
2. <a name="ref2"></a>-, "6.1 Kinetic Theory of Gases", Introductory Chemistry, v. 1.0, url <https://saylordotorg.github.io/text_introductory-chemistry/s10-01-kinetic-theory-of-gases.html> [20201210].
3. <a name="ref3"></a>The Editors of Encyclopaedia Britannica, Kanchan Gupta, Thinley Kalsang Bhutia, Erik Gregersen, "Kinetic theory of gases", Encyclopædia Britannica, url <https://www.britannica.com/science/kinetic-theory-of-gases> [20201210].
4. <a name="ref4"></a>Jessie A. Key, David W. Ball, "Kinetic Molecular Theory of Gases", in Introductory Chemistry, 1st Canadian Edn., Chap. 6. Gases, url <https://opentextbc.ca/introductorychemistry/chapter/kinetic-molecular-theory-of-gases-2/> [20201210].
5. <a name="ref5"></a>Carl R. Nave, "Kinetic Theory", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/Kinetic/kinthe.html> [20201210].
6. <a name="ref6"></a>Wikipedia contributors, "Kinetic theory of gases", Wikipedia, The Free Encyclopedia, 2 Dec 2020, 21:15 UTC, url <https://en.wikipedia.org/w/index.php?oldid=991982665> [20201210].
7. <a name="ref7"></a>-, "Kinetic Theory of Gases", in Calculus-Based General Physics, 22, 1975, url <https://digitalcommons.unl.edu/calculusbasedphysics/22/> [20201210].
{% endcomment %}
