---
layout: post
author: viridi
title: quadratic formula
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "quadratic", "formula"]
date: 2021-01-23 05:02:00 +07
permalink: /fi3201/quadratic-formula
---
One way to get the solution of a quadratic equation is using the quadratic formula [[1](#ref1)]. Here how the formula can be written in some programming languages are shown.


## equation and solution
For an unknown $x$, a general quadratic equation can be written in form of

\begin{equation}
\label{eqn:qf-quadratic-equation}
ax^2 + bx + c = 0,
\end{equation}

where $a$, $b$, and $c$ represent constants. Solution of Eqn. \eqref{eqn:qf-quadratic-equation} can be obtained using the quadratic formula

\begin{equation}
\label{eqn:qf-quadratic-formula}
x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}

with $a \ne 0$. Note that a quadratic equation has two solutions, that is given by $x_1$ and $x_2$.


## algorithm
From Eqns. \eqref{eqn:qf-quadratic-equation} and \eqref{eqn:qf-quadratic-formula}, there are four input parameters $a$, $b$, $c$, and $x$, and there are two output values $x_1$ and $x_2$. We can make the following algorithm using previous information.

Algorithm <a name="alg:qf-quadratic-formula-algorithm">1</a> Quadratic formula. \
`I`: $a$, $b$, $c$, $x$ \
`O`: $x_1$, $x_2$
1. $D \leftarrow b^2 - 4ac$.
2. $\displaystyle x_1 \leftarrow \frac{-b + \sqrt{D}}{2a}$.
3. $\displaystyle x_2 \leftarrow \frac{-b - \sqrt{D}}{2a}$.

The $\leftarrow$ means that the variable on the left is substituted by the expression on the right, which is different when using $=$ which is for equating  [[2](#ref2)]. As an alternative to the previous algorithm, a flow chart for quadratic formula is shown in Fig. <a href="#fig:qf-quadratic-formula-flow-chart">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/quadratic-formula-flow-chart.png)
<br />
Figure <a name="fig:qf-quadratic-formula-flow-chart">1</a> A quadratic equation specified by constants $a$, $b$, $c$ and unknown $x$ have solutions of $x_1$ and $x_2$ through quadratic formula.
{: refdef}

Algorithm and flow chart have their own advantages and disadvantages [[3](#ref3)], and it also depends on the complexity of the problem you are trying to solve. It might be better if you try to exercise which one suits you and on what kind of problem.


## implementation
Flow chart in Fig. <a href="#fig:qf-quadratic-formula-flow-chart">1</a> and algorithm in Alg. <a href="#alg:qf-quadratic-formula-algorithm">1</a> will be implemented in, at least, one programming language. Since there is a lot of variation in writing program, following codes are not the only solution to the problem.

### output
Independent of the programming language
```batch
Equation: ax^2 + bx + c = 0
Constant: a = 1, b = -5, c = 4
Solution: x1 = 4, x2 = 1
```
should be output of the program.

### javascript
```javascript
var a = 1, b = -5, c = 4;
var D = b*b - 4*a*c;
var x1 = (-b + Math.sqrt(D))/(2*a);
var x2 = (-b - Math.sqrt(D))/(2*a);
console.log("Equation: ax^2 + bx + c = 0");
console.log("Constant: a = " + a + ", b = " + b + ", c = " + c);
console.log("Solution: x1 = " + x1 + ", x2 = " + x2);
```

### c++
```c++
#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char *argv[]) {
    double a = 1, b = -5, c = 4;
    double D = b*b - 4*a*c;
    double x1 = (-b + sqrt(D))/(2*a);
    double x2 = (-b - sqrt(D))/(2*a);
    cout << "Equation: ax^2 + bx + c = 0" << endl;
    cout << "Constant: a = " << a << ", b = " << b << ", c = " << c << endl;
    cout << "Solution: x1 = " << x1 << ", x2 = " << x2 << endl;
    return 0;
}
```

### python
```python
a = 1; b = -5; c = 4
D = b*b - 4*a*c
x1 = (-b + D**0.5)/(2*a)
x2 = (-b - D**0.5)/(2*a)
print("Equation: ax^2 + bx + c = 0")
print("Constant: a = ", a, ", b = ", b, ", c = ", c, sep="")
print("Solution: x1 = ", x1, ", x2 = ", x2, sep="")
```

To test the given codes you can use [online compilers](online-compiler).


## exercises
1. Discriminant $D$ in Alg. <a href="#alg:qf-quadratic-formula-algorithm">1</a>. seems not too essential, since it can be directly substitute to the formula for $x_1$ and $x_2$. Explain why it is defined as separate term $D$? Can you guess? The hint is number of solutions.
2. Modify the given JavaScript program for calculating solution of a quadratic equation $2x^2 - 5x + 2 = 0$.
3. Modify the given C++ program for calculating solution of a quadratic equation $4x^2 - 9$.
4. Modify the given Python program for calculating solution of a quadratic equation $5x^2 - 125x = 0$.
5. Make program in BASIC to calculate solution of a quadratic equation $x^2 - 10x + 9 = 0$.




## references
1. <a name="ref1"></a>Wikipedia contributors, "Vector (mathematics and physics)", Wikipedia, The Free Encyclopedia, 22 August 2020, 14:24 UTC, <https://en.wikipedia.org/w/index.php?oldid=974354203> [20210123].
2. <a name="ref2"></a>Henry Swanson, "Answer to 'reverse (left) arrow in an algorithm?'", Mathematics Stack Exchange, 9 Mar 2014, url <https://math.stackexchange.com/q/704942> [20210123].
3. <a name="ref3"></a>Sampurna Shrestha, "Advantages and disadvantages of algorithm and flowchart", Computer Science Mentor, 28 Feb 2017, url <https://computersciencementor.com/advantages-and-disadvantages-of-algorithm-and-flowchart/> [20210123].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-23-quadratic-formula.md)

