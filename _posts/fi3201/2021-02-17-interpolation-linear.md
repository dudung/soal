---
layout: post
author: viridi
title: linear interpolation
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "linear", "interpolation"]
date: 2021-02-17 06:18:00 +07
permalink: /fi3201/linear-interpolation
---
If there is a discrete set of data points, to construct new data points within the range of the known data we can use a method of curve fitting using linear polynomials known as linear interpolation [[1](#ref1)]. Due its simplicity this method is still used in may areas nowadays [[2](#ref2)]. In binary diagram of mixture of two substances, where the horizontal axis represents concentration of one substance, it uses linear interpolation [[3](#ref3)]. You can use a spreadsheet, e.g. Microsoft Excel [[4](#ref4)], or an online calculator [[5](#ref5)] to perform an interpolation.


## in [0,1] range
In $y-x$ diagram, suppose that we have two points $(0, B)$ and $(1, A)$ and we want to get value of $y$ at certain value of $x \in [0, 1]$ as illustrated in Fig. <a href="#fig:li-linear-interpolation-0-1">1</a>

{:refdef: style="text-align: center;"}
![..](/assets/img/math/intrpl/linear-interpolation-0-1.png)
<br />
Figure <a name="fig:li-linear-interpolation-0-1">1</a> Linear interpolation to calculate fraction of mixture $x$ representing substance $A$.
{: refdef}

We can have that

\begin{equation}
\label{eqn:li-in-range-0-1}
y(x) = x A + (1-x) B,
\end{equation}

that produces $y(0) = B$ and $y(1) = A$ as desired with

\begin{equation}
\label{eqn:li-fraction-x}
x = \frac{\chi_A}{\chi_A + \chi_B},
\end{equation}

where $\chi$ can be mass, volume, or other properties of the substances, which gives that $x = 0$ is pure substance of $B$ and $x = 1$ is pure substance of $A$.


## in arbitrary range
Suppose we have two points $(x_1, y_1)$ and $(x_2, y_2)$ and want to have $y$ at certain value of $x \in [x_1, y1]$ as given in Fig. <a href="#fig:li-linear-interpolation-x1-x2">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/intrpl/linear-interpolation-x1-x2.png)
<br />
Figure <a name="fig:li-linear-interpolation-x1-x2">2</a> Linear interpolation to calculate $x \in[x_1, x_2]$.
{: refdef}

Gradient of line passing the two points $(x_1, y_1)$ and $(x_2, y_2)$ is

\begin{equation}
\label{eqn:li-gradient-x1-y1-x2-y2}
m = \frac{y_2 - y_1}{x_2 - x_1}
\end{equation}

and the equation of a line can be constructed using

\begin{equation}
\label{eqn:li-equation-of-a-line-x1-y1-x2-y2-construction}
y = m(x - x_1) + y_1 = m(x - x_2) + y_2,
\end{equation}

that gives

\begin{equation}
\label{eqn:li-equation-of-a-line-x1-y1-x2-y2}
y = \left( \frac{y_2 - y_1}{x_2 - x_1} \right) x + \left( \frac{y_1 x_2 - x_1 y_2}{x_2 - x_1} \right).
\end{equation}

Since we will deal with the linear interpolation using numerical approach, Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2-construction} is recommended to memorize since it is simpler than Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2}.


## data set
If there is data set consists of pairs of $(x_1, y_1)$, $(x_2, y_2)$, $\dots$, $(x_N, y_N)$, then we require to perform the linear interpolation in each range $x_{n} \le x \le x_{n+1}$, where there will be only $N-1$ ranges, that is assumed have equal interval for simplicity.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/intrpl/linear-interpolation-data-set.png)
<br />
Figure <a name="fig:li-linear-interpolation-data-set">3</a> Linear interpolation in each range with equal interval of a data set.
{: refdef}

Fig. <a href="#fig:li-linear-interpolation-data-set">3</a> shows linear interpolation for a data set. With equal interval we can obtain the range using

\begin{equation}
\label{eqn:li-range-determination}
n = 1 + \left\lfloor \frac{x - x_1}{\Delta x} \right\rfloor,
\end{equation}

where $\Delta x$ is the interval of each range. After get the value of $n$, we use

\begin{equation}
\label{eqn:li-linear-interpolation-data-set}
y = \left( \frac{y_{n+1} - y_n}{x_{n+1} - x_n} \right) x + \left( \frac{y_n x_{n+1} - x_n y_{n+1}}{x_{n+1} - x_n} \right),
\end{equation}

which is actually Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2} but for each range indicated with the index $n$.


## implementation
Using common programming language, e.g. C++, JavaScript, or Python you can implement Eqns. \eqref{eqn:li-range-determination} and \eqref{eqn:li-linear-interpolation-data-set} to do the interpolation. Array for the data set is required.


## exercises
1. If $x = 0.25$ find the fraction of $B$ and $A$ using Fig. <a href="#fig:li-linear-interpolation">1</a>.
2. Prove that center and right side of Eqn. {eqn:li-equation-of-a-line-x1-y1-x2-y2-construction} do produce the same results as in Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2}.
3. Test Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2} that it holds for the two points $(x1, y1)$ and $(x2, y2)$.
4. If we transform all $x$s to $x - x_1$ we can obtain Eqn. \eqref{eqn:li-in-range-0-1} from Eqn. \eqref{eqn:li-equation-of-a-line-x1-y1-x2-y2} with $y_1 = B$ and $y_2 = A$. Show how to do that in a shortes way you are able to.
5. Prove that Eqn. \eqref{eqn:li-linear-interpolation-data-set} holds in its range for lower and upper bounds, $(x_n, y_n)$ and $(x_{n+1}, y_{n+1})$, respectively.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Linear interpolation", Wikipedia, The Free Encyclopedia, 2 Feb 2021, 04:04 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1004343292> [20210122].
2. <a name="ref2"></a>-, "Linear Interpolation", ScienceDirect, url <https://www.sciencedirect.com/topics/engineering/linear-interpolation> [20210217].
3. <a name="ref3"></a>Glenda Smith, Denise Watts, "Binary phase diagrams", PetroWiki, Society of Petroleum Engineers (SPE), 
Richardson, Texas 75080, 2 Jun 2015 at 11:53, url <https://petrowiki.spe.org/Binary_phase_diagrams> [20210217].
4. <a name="ref4"></a>-, "Linear Interpolation with Excel", Dagra Graph Digitizer, url <https://www.datadigitization.com/dagra-in-action/linear-interpolation-with-excel/> [20210217].
5. <a name="ref5"></a>-, "Linear interpolation and extrapolation with calculator", x-engineer.org, Engineering Tutorials, url <https://x-engineer.org/undergraduate-engineering/advanced-mathematics/numerical-methods/linear-interpolation-and-extrapolation-with-calculator/> [20210217].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-02-17-interpolation-linear.md)

{% comment %}

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


## for and if
Following code

```python
for i in range(0, 10):
	if i > 5:
		print(i)
```

is supposed to produce number more than 5 and the resulta are

```
$ python3.7 for-if.py
6
7
8
9
```

as expected.


## nested for and if
In the next example we will show the use of `if` in a `for` loop.

```python
for i in range(4, 10):
	for j in range(4, 10):
		k = i * j
		if i == j:
			print(k, end=" ")
		else:
			print("00", end=" ")
	print()
```

which produces

```python
$ python3.7 for-if.py
16 00 00 00 00 00
00 25 00 00 00 00
00 00 36 00 00 00
00 00 00 49 00 00
00 00 00 00 64 00
00 00 00 00 00 81
```

where the rule is simply

\begin{equation}
\label{eqn:pyint-matrix-example}
m_{ij} = \left\\{
\begin{array}{cc}
(i + 3)(j + 3), & i = j, \newline
0, & i \ne j,
\end{array}
\right.
\end{equation}

for the matrix elemement with $i = 1, .., 6$ and $j = 1, .., 6$.


## Exercises
1. What is the ASCII character that we need to put in the beginning of a line to indicate that the line is a comment (not a Python statement)? What about a multi-line commment in Python? Is there any pair of `/*` and `*/`in Python as in C++ language?
2. Explain the use of `range` in a `for` loop. What are the parameters required? What is the minimum number of parameters? Read reference about it [[7](#ref7)], whenever necessary.
3. What is the output of following code?
```python
for i in range(2, 7):
	for j in range(1, i):
		print(j, end=" ")
	print()
```
You can use [[4](#ref4)] to do that.
4. Write a code to produce following output
```
12345
1234
123
12
1
```
and name it as `triangle-number-lines-down.py`.
5. Study following lines
```python
N = 5
for i in range(2, N + 2):
	for j in range(1, N + 2 - i):
		print(" ", end=" ")
	for j in range(1, i):
		print("0", end=" ")
	print()
```
and shown the output. Explain how it can produce such result.

## References
1. <a name="ref1"></a>Wikipedia contributors, "'Hello, World!' program", Wikipedia, The Free Encyclopedia, 20 Jan 2021, 01:21 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1001702830> [20210122].
2. <a name="ref2"></a>-, "Notepad++", Version 7.9.2, release Date 2021-01-01, url <https://notepad-plus-plus.org/downloads/> [20210122].
3. <a name="ref3"></a>-, "Cygwin", Version 3.1.6-1, url <https://www.cygwin.com/> [20210122].
4. <a name="ref4"></a>-, "Python Online Compiler", Programiz, url <https://www.programiz.com/python-programming/online-compiler/> [20210122].
5. <a name="ref5"></a>-, "Python Releases for Windows", Latest Python 3 Release - Python 3.9.1, url <https://www.python.org/downloads/windows/> [20210122].
6. <a name="ref6"></a>-, "Python For Loops", W3Schools, url <https://www.w3schools.com/python/python_for_loops.asp. [20210122].
7. <a name="ref7"></a>Vishal Hule, "Python range() function explained with examples", PYnative - Python Programming, 15 Dec 2020, url <https://pynative.com/python-range-function/> [20210122].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-22-python-intro.md)

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
