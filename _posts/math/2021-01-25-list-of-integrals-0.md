---
layout: post
author: viridi
title: list of integrals 0
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: math
tags: ["integral", "0"]
date: 2021-01-25 16:40:00 +07
permalink: /math/list-of-integrals-0
---
Some integrals required in butiran are presented here.


## in front of line of charge
In [electric field in front of line of charge](/electrostatics/electric-field-line-charge-front) following form

\begin{equation}
\label{eqn:loi0-in-front-of-line-of-charge-1}
\int \frac{dx}{(b+l-x)^2}
\end{equation}

is required to solve. Using $u = (b + l - x)$ we can have that $du = d(b + l - x) = -dx$, which makes Eqn. \eqref{eqn:loi0-in-front-of-line-of-charge-1} into

\begin{equation}
\label{eqn:loi0-in-front-of-line-of-charge-2}
-\int \frac{du}{u^2} = \frac{1}{u} + c.
\end{equation}

Substitute $u$ back to Eqn. \eqref{eqn:loi0-in-front-of-line-of-charge-2} will produce

\begin{equation}
\label{eqn:loi0-in-front-of-line-of-charge-3}
\int \frac{dx}{(b+l-x)^2} = \frac{1}{b + l - x} + c,
\end{equation}

where $c$ is an arbitrary constant. If we put lower bound $x = a$ and upper bound $x = b$ we will have

\begin{equation}
\label{eqn:loi0-in-front-of-line-of-charge-4}
\begin{array}{rcl}
\displaystyle \int_a^b \frac{dx}{(b+l-x)^2} & = & \displaystyle \left[ \frac{1}{b + l - x} \right]_{x = a}^b \newline 
& = & \displaystyle \left( \frac{1}{b + l - b} \right) - \left( \frac{1}{b + l - a} \right) \newline
& = & \displaystyle \frac{1}{l} - \frac{1}{b-a + l} \newline
& = & \displaystyle \frac{1}{l} - \frac{1}{L + l} \newline
& = & \displaystyle \frac{(L + l) - l}{l (l + L)} \newline
& = & \displaystyle \frac{L}{l (l + L)},
\end{array}
\end{equation}

since it is known that $L = b - a$.


## at back of line of charge
In [at back of the other end of the line](/electrostatics/electric-field-line-charge-front) following form

\begin{equation}
\label{eqn:loi0-at-back-of-line-of-charge-1}
\int \frac{dx}{(a-l-x)^2},
\end{equation}

that the solution, straight forwards using previous way, is

\begin{equation}
\label{eqn:loi0-at-back-of-line-of-charge-2}
\int \frac{dx}{(a-l-x)^2} = \frac{1}{a-l-x} + c.
\end{equation}

By putting lower bound $x = a$ and upper bound $x = b$ we will have

\begin{equation}
\label{eqn:loi0-at-back-of-line-of-charge-3}
\begin{array}{rcl}
\displaystyle \int_a^b \frac{dx}{(a-l-x)^2} & = & \displaystyle \left[ \frac{1}{a - l - x} \right]_{x = a}^b \newline 
& = & \displaystyle \left( \frac{1}{a - l - b} \right) - \left( \frac{1}{a - l - a} \right) \newline
& = & \displaystyle \frac{1}{a - b - l} - \frac{1}{- l} \newline
& = & \displaystyle \frac{1}{-L - l} + \frac{1}{l} \newline
& = & \displaystyle -\frac{1}{L + l} + \frac{1}{l} \newline
& = & \displaystyle \frac{1}{l} - \frac{1}{L + l} \newline
& = & \displaystyle \frac{(L + l) - l}{l(L+l)} \newline
& = & \displaystyle \frac{L}{l(L+l)},
\end{array}
\end{equation}

again with $a - b = -L$.

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/math/2021-01-25-list-of-integrals-0.md)
