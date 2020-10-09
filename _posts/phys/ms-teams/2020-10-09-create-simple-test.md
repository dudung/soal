---
layout: post
author: viridi
title: create simple test using ms-teams
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["ms-teams"]
date: 2020-10-09 15:21:00 +07
permalink: /physics/ms-teams/create-simple-test
---
A step-by-step how to make a simple test for physics lecture using Microsoft Teams [[1](#ref1)] is discussed here.


## Microsoft Teams
Usually you will have access through your institution using the link <https://teams.microsoft.com/> and will be asked to sign in with your institutional account. It is also assumed that you have already a team for virtual room in creating a test. The team should be the type of Class.


## Creating an assigment of type Choice
1. In a team of type Class find the tab **Assignments** and click it.
2. Click **Create** button and choose **Quiz**.
3. By Assuming this is the first quis, choose **+ New Quiz**.
4. Click **Unnamed Quiz** and change it to a name you desired, e.g. "Kinematics 1-d".
5. Do **Enter a description** with some information, e.g. "Quiz about 1-d kinematics".
6. Click **+ Add new**.
7. There are types of Choice, Text, Rating, Date, Ranking, Likert, File upload, Net Promoter Score, and Section. Choose **Choice** this time.
8. Fill **Question** with your question, e.g. A particle is at position x1 at time t1 and at position x2 at time t2. A physical quantity obtained using (x2 - x1) / (t2 - t1) is
9. Fill **Option 1** with "acceleration".
10. Fill **Option 2** with "instantanenous velocity".
11. Click **+ Add option** and fill **Option 3** with "average velocity". Click **✓** on the right of the option to mark it as right answer.
12. Click **+ Add option** and fill **Option 4** with "average acceleration".
13. Set **Points**, e.g. 25.
14. Activate **Required** to assure that it must be answered.
15. You can use **Preview** on the tab to see how the question is displayed in different gadgets, e.g. **Computer** and **Mobile**.
16. Use the button **Back** on top of the preview to continue editing the question.
17. Continue to add more questions using **+ Add new**. See the next section for the other question beside the first one.

## Trial questions
Following trial questions are only for creating the quiz.
1. A particle is at position $x_1$ at time $t_1$ and at position $x_2$ at time $t_2$. A physical quantity obtained using $(x_2 - x_1) / (t_2 - t_1)$ is (a) acceleration, (b) instantanenous velocity, (c) average velocity, (d) average acceleration. Points: 25. Required: true. Answer: c.
2. At t = 0 s a partikel has velocity of 1 m/s and at t = 1 s it has velocity of 5 m/s. If it is an nonuniform motion, what is its acceleration? (a) 1 m/s^2, (b) 2 m/s^2, (c) 3 m/s^2, (d) 4 m/s^2. Points: 25. Required: true. Answer: d.


## References
1. <a name="ref1"></a>Wikipedia contributors, "Microsoft Teams", Wikipedia, The Free Encyclopedia, 9 Oct 2020, 03:46 UTC, <https://en.wikipedia.org/w/index.php?oldid=982604302> [20201009].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/ms-teams/2020-10-09-create-simple-test.md)



{% comment %}
A physical quantity, designates how fast and in what direction a point is moving, is velocity [[1](#ref1)].


## Notation
Velocity in vector form is presented using $\vec{v}$, sometimes is also $\vec{u}$. In general velocity

\begin{equation}
\label{eqn:velo-t}
\vec{v} = \vec{v}(t)
\end{equation}

is function of time $t$ and also its components

\begin{equation}
\label{eqn:velo-t-components}
\vec{v}(t) = v_x(t) \hat{i} + v_y(t) \hat{j} + v_z(t) \hat{k}.
\end{equation}

The functions $x(t)$, $y(t)$, and $z(t)$ can also be a constant value or simply zero.


## Relation to position
When we have position $\vec{r}$, velocity $\vec{v}$ can be obtained from it

\begin{equation}
\label{eqn:velo-from-r}
\vec{v} = \frac{d\vec{r}}{dt}
\end{equation}

using differential. Suppose we have

\begin{equation}
\label{eqn:velo-r-example-1}
\vec{r} = (t + 10) \hat{i} + (t^2 - 2t + 1) \hat{j} + 4 \hat{k},
\end{equation}

then the velocity is simply

\begin{equation}
\label{eqn:velo-v-example-1}
\vec{v} = \hat{i} + (2t - 2) \hat{j}
\end{equation}

using Eqn. \eqref{eqn:velo-from-r}.


## Relation to acceleration
If we have acceleration $\vec{a}$, velocity $\vec{v}$ can also be obtained from it

\begin{equation}
\label{eqn:velo-from-a}
\vec{v} = \int \vec{a} \ dt
\end{equation}

using integral. An initial condition in the form of $\vec{v}(t_0)$ is also required. Suppose we have

\begin{equation}
\label{eqn:velo-a-example-2}
\vec{a} = 3t^2 \ \hat{i} + (2t + 1) \hat{j} + \hat{k},
\end{equation}

and initial condition

\begin{equation}
\label{eqn:velo-a-example-2-ic}
\vec{v}(0) = \hat{i} + 2 \hat{j} + 3 \hat{k},
\end{equation}

where we choose that $t_0 = 0$. By introducing the lower and upper bounds to the integral in Eqn. \eqref{eqn:velo-from-a}, we can have

\begin{equation}
\label{eqn:velo-v-example-2}
\vec{v}(t) - \vec{v}(0) = \int_0^{t} \vec{a} \ dt.
\end{equation}

Substitution of Eqns. \eqref{eqn:velo-a-example-2} and \eqref{eqn:velo-a-example-2-ic} to Eqn. \eqref{eqn:velo-v-example-2} will produce

\begin{equation}
\label{eqn:velo-v-example-2-2}
\vec{v}(t) - \left( \hat{i} + 2 \hat{j} + 3 \hat{k} \right) = \int_0^{t} \left[ 3t^2 \ \hat{i} + (2t + 1) \hat{j} + \hat{k} \right] \ dt.
\end{equation}

Solution of Eqn. \eqref{eqn:velo-v-example-2-2} is

\begin{equation}
\label{eqn:velo-v-example-2-3}
\begin{array}{rl}
\vec{v}(t) & = & \left[ t^3 \ \hat{i} + (t^2 + t) \hat{j} + t \ \hat{k} \right]_{t = 0}^t +
\left( \hat{i} + 2 \hat{j} + 3 \hat{k} \right) \newline
& = & (t^3 + 1) \hat{i} + (t^2 + t + 2) \hat{j} + (t + 3) \hat{k}.
\end{array}
\end{equation}

You can put $t = 0$ into Eqn. \eqref{eqn:velo-v-example-2-3} to obtain Eqn. \eqref{eqn:velo-a-example-2-ic} and differentiate it to obtain Eqn. \eqref{eqn:velo-a-example-2}.


## Quantity with the same dimension
Velocity in Eqn. \eqref{eqn:velo-t} is known also as instantaneous velocity or velocity at specific time of the particle in a point along particle trajectory [[2](#ref2)]. This type of velocity is presented in a function of time $t$, that can be a continuous function or a discrete function such [step function velocity](step-function-velocity). Related to (instantaneous) velocity there are average velocity, speed, and [relative velocity](relative-velocity), which have the same dimension as velocity.


## Exercises
1. Find the velocity of a particle that has position of $\vec{r} = (t^4 - \cos 2t) \hat{i} + (1 - t^2) \hat{j} + 2 \hat{k}$. Remember hat $(d/dt)(\cos at) = - a\sin at$.
2. A particle has $a = (4t^3 - 2t) \ \rm m/s^2$. Find its velocity if $v(0) = 2 \ \rm m/s$.
3. Find velocity of a particle with acceleration $a = (-3t^2 + 5) \ \rm m/s^2$, where the initial velocity is $v(2) = 5 \ \rm m/s$.
4. A particle has a position of $\vec{r} = (2 \cos 0.25\pi t) \hat{i} + (2 \sin 0.25\pi t) \hat{j}$. Draw its position for $t = 0, 1, \dots, 7, 8$ and at each position draw its velocity vector. What form is the of particle trajectory?
5. A particle move with $x = 0.5 t^2$ and $a_y = 4$. If $v_{0y}(1) = 3$, find $\vec{v}$. 


## References
1. <a name="ref1"></a>The Editors of Encyclopaedia Britannica, Piyush Bhathya, Yamini Chauhan, William L. Hosch, Emily Rodriguez, "Vector", Encyclopædia Britannica, 14 Apr 2016, url <https://www.britannica.com/science/velocity> [20200929].
2. <a name="ref1"></a>José L. Fernández, "Instantaneous velocity", Fisicalab, url <https://www.fisicalab.com/en/section/instantaneous-velocity>
[20200929].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-09-05-velocity.md)

{% endcomment %}
