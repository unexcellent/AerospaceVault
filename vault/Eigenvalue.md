#uni/courses/math1 

During a [[Change of Basis|change of basis]] [[Linear Transformation|transformation]] represented by $A \in \mathbb{R}^{n \times n}$, there exists a set of vectors, that do not change direction, but are scaled by a set of eigenvalues $\lambda_{i} \in \mathbb{R}$.

# Multiplicity

In general it holds, that
$$
1 \le g(\lambda) \le a(\lambda) \le n
$$

## Algebraic Multiplicity

The algebraic multiplicity $a(\lambda_{i})$ of an eigenvalue $\lambda_{i}$ is the number of times it appears as a solution of the characteristic polynomial.

### Example
$$
P_{A}(\lambda) = \lambda^{2} - 6 \lambda + 6
$$
$$
\Rightarrow \lambda_{1} = 3 + \sqrt{3} \quad \lambda_{2} = 3 - \sqrt{3}
$$
In this case $a(\lambda_{1})= a(\lambda_{2})= 1$ since the eigenvalues are not repeated.

## Geometric Multiplicity

The geometric multiplicity of an eigenvalue is the dimension of the associated [[Eigenspace]]
$$
g(\lambda)=\dim (E_\lambda)
$$
