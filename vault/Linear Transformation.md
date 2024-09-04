#uni/courses/math1 

Linear transformations represent a mapping between two [[Vector Space]] that preserves the operations of [[Vector#Vector Addition|vector addition]] and [[Vector#Multiplication with a Scalar|scalar multiplication]].

Let $V, W \subset \mathbb{R}$ and $T: V \rightarrow W$ be a map between them. $T$ is a linear transformation if $\forall \alpha, \beta \in \mathbb{R}$ and $\forall u, v \in V$:
$$
T(\alpha u + \beta v) = \alpha T(v) + \beta T (u)
$$

# Matrix Representation

Given $V \subset \mathbb{R}^{n}, W \subset \mathbb{R}^{m}$, all [[Matrix|matrices]] $A \in \mathbb{R}^{m \times n}$ satisfy the properties of linear transformation and it holds that:
$$
T(x) = Ax
$$
If $V$ and $W$ are finite dimensional we can always find a matrix representation of any linear transformation $T$. We first find the [[Basis of a Vector Space|bases]] of $V$ and $W$:
$$
B_{V}= \{v_{1}, \cdots, v_{n}\}
$$
$$
B_{W}= \{w_{1}, \cdots, w_{m}\}
$$
Then for each base vector $v_j ∈ B_V$ we write $T(v_j) ∈ W$ as a coordinate representation w.r.t. the base $B_{W}$:
$$
T (v_{j}) = \sum\limits_{i=1}^{m} a_{ij} \cdot w_{i} \quad \forall j \in \{1, 2, \cdots, n\}
$$
The matrix $A = (a_{ij})$ represents $T$ w.r.t. the bases $B_V$ and $B_W$.

# Isometric Transformations

A transformation is called isometric if
$||Ax|| = ||x|| \quad \forall x \in \mathbb{R}^{n}$

# Equivalent Statements

1. $T$ is isometric
2. $T$ leaves the scalar product invariant: $\langle Ax, Ay \rangle = \langle x, y \rangle \quad \forall x, y \in \mathbb{R}^{n}$
3. $A$ is an orthogonal matrix: $A \cdot A^{T} = A^{T} \cdot A = I_{n}$
4. The rows/columns of $A$ are an [[Vector Space#Orthogonality|orthonormal basis]] in $\mathbb{R}^{n}$

# Injectivity

A linear transformation $A \in \mathbb{R}^{m \times n}$ is injective if
$$
\dim (\ker (A)) = 0
$$
-> [[Kernel of a Matrix]]

# Surjectivity

A linear transformation $A \in \mathbb{R}^{m \times n}$ is surjective if
$$
\rank A = m
$$
-> [[Rank of a Matrix]]

or in other words
$$
\dim (\range (A)) = \R{m}
$$
-> [[Range of a Matrix]]