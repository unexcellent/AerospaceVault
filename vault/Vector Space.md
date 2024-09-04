#uni/courses/math1 

Consider a set $V$. Define a sum between two elements of $V$ satisfying the axioms. Define a multiplication of an element of $V$ by a scalar satisfying the axioms $(V, +, \cdot)$ is said to be a [[Vector|vector]] space.

# Example

$(\mathbb{R}^{3}, +, \cdot)$ is called the euclidian vector space of dimension $3$.

$(V, +, \cdot)$ is a vector space. 
Take $W \subset V$: Under which condition can we say that also $(W, +, \cdot)$ is a vector space.

# Euclidian Vector Space

A vector space $V$ endowed with a scalar product $<v, w>$ satisfying the [[Vector#Euclidian Scalar Product|axioms]] the n the vector space V is said to be an Euclidian vector space.

## Axioms

The properties of vector addition and scalar multiplication in $\mathbb{R}^{n}$ are given below. For all $v, w, z \in \mathbb{R}^{n}$ and $\alpha, \beta \in \mathbb{R}$ the following holds true:

1) $v + w = w + v$
2) $v + (w + z) = (v + w) + z$
3) $v + 0 = 0 + v$
4) $v + (-v) = (-v) + v = 0$
5) $1 \cdot v = v$
6) $\alpha (\beta v) = (\alpha \beta)v$
7) $\alpha (v + w) = \alpha v + \alpha w$
8) $(\alpha + \beta)v = \alpha v + \beta v$

# Sub-Vector Space Condition

$$
(\text{SVS}): \begin{cases}
1.\quad 0 \in W \\
2.\quad v, w \in W \Rightarrow v + w \in W \\
3.\quad v \in W, \alpha \in \mathbb{R} \Rightarrow \alpha v \in W
\end{cases}
$$

In other words: given $v, w \in W$ and $\alpha, \beta \in \mathbb{R}$

$(W, +, \cdot)$ is an SVS $\Leftrightarrow \alpha v + \beta w \in W$ is a linear combination of $v$ and $w$ with coefficient alpha and beta
$$
\alpha (\lambda_{1}u) + \beta (\lambda_{2}u) = (\alpha \lambda_{1} + \beta \lambda_{2}) u \in g
$$

# Orthogonality

A vector space $W$ with a set of vectors $\{w_{1}, w_{2}, \cdots, w_{m}\}, w_{j} \neq 0$ is called
- **orthogonal**, if $\langle w_{k}, w_{j} \rangle = 0, \quad \forall j \neq k$ (see [[Vector#Euclidian Scalar Product]]) i.e. all elements are orthogonal to each other
- **orthonormal**, if $\langle w_{k}, w_{j} \rangle = 0, \quad \forall j \neq k$ and $||w_{j||=1} \quad \forall j$ i.e. all elements are orthogonal to each other and their length is exactly one
- **orthonormal basis** if they are orthonormal and for a basis of $W$