#uni/courses/math3 

Multiple [[Linear ODE|linear ODEs]] of [[First Order ODE|first order]] can be dependent on each other in a [[Linear Systems of Equations]] like
$$
\begin{cases}
y'_{1} = 4y_{2} \\
y'_{2} = 4y_{1} + e^t 
\end{cases}
$$

# Solution Approach

As with [[First Order Inhomogenous ODE]]'s, the solution consists of there sum of homogeneous solution and particular solution
$$
y = y_{h} + y_{p}
$$

## Homogeneous Solution

First, the equation system should be expressed in [[Matrix]] form
$$
y_{h}' = A \cdot y_{h} = \begin{pmatrix}
0 & 4 \\ 
4 & 0
\end{pmatrix} \cdot \begin{pmatrix}
y_{h1} \\ 
y_{h2}
\end{pmatrix}
$$
Then, the [[Eigenvalue|eigenvalues]] of $A$ need to be determined and the corresponding [[Eigenvector|eigenvectors]]. For the eigenvalues $\lambda_{1/2} = \alpha \pm \beta i$ and eigenvectors $v_{1/2}$ the solution can be written as
$$
y_{h} = c_{1} \cdot e^{\alpha_{1} x} \cdot v_{1} + c_{2} \cdot e^{\alpha_{2} x} \cdot v_{2} \quad \text{with } c_{1}, c_{2} \in \mathbb{R}
$$
for this example
$$
y_{h} = c_{1} \cdot e^{4t} \cdot \begin{pmatrix}
1 \\
1
\end{pmatrix}
+ c_{2} \cdot e^{-4t} \cdot \begin{pmatrix}
1 \\
-1
\end{pmatrix}
$$

## Particular Solution

The particular solution is based on
$$
y_{p} = Y \cdot u \quad \text{and} \quad Y \cdot u' = r
$$
with $Y$ being the [[Fundamental System]] of $y$ and $r$ being the remainder.
The general solution is then
$$
y_{p} = Y \cdot \int Y^{-1} \cdot r \ dt
$$