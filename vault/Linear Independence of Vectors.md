#uni/courses/math1 

A set $B:= \{v_{1}, v_{2}, \cdots, v_{m}\}$ is made of linearly independent [[Vector|vectors]] if "no one of them can be written as a linear combination of all the others".
$$
\alpha_{1} v_{1} + \alpha_{2} v_{2} + \cdots + \alpha_{m} v_{m} = 0, \quad \alpha_{1}, \alpha_{2}, \cdots, \alpha_{m} \in \mathbb{R}
$$
only if $a_{1} = a_{2} = \cdots = a_{m} = 0$.

Two vectors are linearly independent, if they do not lie on the same line.
Three vectors are linearly independent, if they do not lie on the same plane.

# Examples

## Linearly Dependent Set of Vectors

Given the vectors $v_{1} = \begin{pmatrix}1  \\ 2\end{pmatrix}, v_{2} = \begin{pmatrix}2  \\ 4\end{pmatrix}$
$$
\alpha_{1} v_{1} + \alpha_{2} v_{2} = 0 \Rightarrow v_{1} = - \frac{\alpha_{2}}{\alpha_{1}} v_{2} \Rightarrow \frac{\alpha_{2}}{\alpha_{1}} = -\frac{1}{2}
$$
Since there is a combination of the coefficients other than $0$, they are not linearly independent.
