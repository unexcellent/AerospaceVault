#uni/courses/math1 

During some [[Change of Basis|change of basis]] [[Linear Transformation|transformation]] with $A \in \mathbb{R}^{n \times n}$, there exist a set of [[Vector|vectors]] called eigenvectors, that do not change their direction, but are only scaled by an [[Eigenvalue]] $\lambda_{i} \in \mathbb{R}$. This can be represented like this:
$$
A \cdot v_{i} = \lambda_{i} \cdot I_{n} \cdot v_{i} \quad \Rightarrow \quad (A - \lambda_{i} \cdot I_{n}) \cdot v_{i} = 0
$$
-> [[Matrix#Identity Matrix]]

This can only be valid if $\det(A - \lambda I_{n}) = 0$. $\det(A - \lambda I_{n})$ represents a [[Polynomial and Rational Functions|polynomial]] $P_{A}(\lambda)$ of degree $n$ in $\lambda$, which is called the characteristic polynomial of $A$.
To determine the eigenvectors, this polynomial has to solved:
$$
P_{A}(\lambda) = 0 = \det(A - \lambda \cdot I_{n})
$$
-> [[Determinant of a Matrix]]

# Linear Independence

Let $v_{1}, v_{2}, \dots, v_{m}$ be eigenvectors associated to different eigenvalues $\lambda_{1}, \lambda_{2}, \dots, \lambda_{m}$. It holds, that if $\lambda_{i} \neq \lambda_{j}$ then $v_{i}$ and $v_{j}$ are [[Linear Independence of Vectors|linearly independent]].