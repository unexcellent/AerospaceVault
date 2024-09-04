#uni/courses/math1 

Cramer's rule is a formula for solving [[Linear Systems of Equations]].

Let $A = (a^{1}, \cdots, a^{n}) \in \mathbb{R}^{n \times n}$ be a [[Matrix#Regularity of a Matrix|regular matrix]], where $a^{i}$ are the columns of $A$. Then for a $b ∈ R^{n}$ the unique solution to the system $Ax = b$ is given by components $x = (x^1, \cdots , x^n)$:
$$
x_{k}= \frac{\det (a^{1}, \cdots, a^{k-1}, b, a^{k+1}, \cdots, a^{n})}{\det A}
$$
$\det (a^{1}, \cdots, a^{k-1}, b, a^{k+1}, \cdots, a^{n})$ refers to the $k$-th column of the matrix being replaced by $b$.