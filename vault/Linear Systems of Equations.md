#uni/courses/math0 
#uni/courses/math1 

One of the main applications of [[Matrix]] is the analysis of systems of linear equations (SLEs). An SLE with $m \in \mathbb{N}$ equations and $n \in \mathbb{N}$ unknowns $x_1, \dots, x_n$ has the form
$$
\begin{align}
a_{11}x_1 + a_{12}x_2 + \dots +  + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots +  + a_{2n}x_n = b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots +  + a_{mn}x_n = b_m \\
\end{align}
$$

with $a_{i,j} \in \mathbb{R}$, $b_{i} \in \mathbb{R}$, $1 \le i \le m$, $1 \le j \le n$, we can define $Ax = b$.

Given $A \in \mathbb{R}^{m \times n}$, $b \in \mathbb{R}^n$ with $m,n \in \mathbb{N}$, a [[Vector|vector]] $x \in \mathbb{R}^n$ satisfying $Ax = b$ is called a solution of the SLE.
We define: $\mathbb{L}:= \{x \in \mathbb{R}^n | Ax = b\}$

Given an SLE $Ax=b$, there are precisely three possible cases:

1. $|\mathbb{L}| = 0$ -> there are not solutions
2. $|\mathbb{L}| = 1$ -> there is a unique solution
3. $|\mathbb{L}| = \infty$ -> there are infinitely-many solution

# Homogenous Systems

Given a linear system of equations defined by $A \cdot x = b$, it is called **homogeneous** if $b = 0$ and **inhomogeneous** if $b \neq 0$.
Homogeneous systems always have the solution $x = 0$, but there are also other solutions.
