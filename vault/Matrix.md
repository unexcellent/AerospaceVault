#uni/courses/math0 
#uni/courses/math1 

Given $m, n \in \mathbb{N}$, an $m \times n$-matrix is an array of real numbers $a_{ij} \in \mathbb{R}, \quad i=1, \dots, m, \quad j=1, \dots, n$ of the form:

$$
A = \begin{pmatrix}
a_{11} & a_{12} & \dots  & a_{1n} \\ 
a_{21} & a_{22} & \dots  & a_{2n} \\
\vdots & \vdots & \ddots  & \vdots \\
a_{m1} & a_{m2} & \dots  & a_{mn} \\
\end{pmatrix}
$$

Given $A \in \mathbb{R}^{n \times n}$ the following [[Mathematical Statements|statements]] are equivalent
- $\det A \neq 0$ (see [[Determinant of a Matrix]])
- the row/column [[Vector]] of $A$ are [[Linear Independence of Vectors|linearly independent]]
- $A$ is [[Matrix#Regularity of a Matrix|regular]]
- $A$ is [[Inverse of a Matrix|invertible]]

# Matrix Calculus

## Addition with a Scalar

Given $A = (a_{ij}) \in \mathbb{R}^{m \times n}$, $\alpha \in \mathbb{R}$
$$
A + \alpha = (a_{ij} + \alpha) \in \mathbb{R}^{m \times n}
$$ 

## Multiplication with a Scalar

Given $A = (a_{ij}) \in \mathbb{R}^{m \times n}$, $\alpha \in \mathbb{R}$
$$
A \cdot \alpha = (a_{ij} \cdot \alpha) \in \mathbb{R}^{m \times n}
$$

## Sum of Two Matrices

Given $A = (a_{ij}) \in \mathbb{R}^{m \times n}$, $B = (b_{ij}) \in \mathbb{R}^{m\times n}$
$$
A + B = (a_{ij} + b_{ij})
$$

## Multiplication by a Vector

Given $A \in \mathbb{R}^{m \times n}$ and $x \in \mathbb{R}^{n}$ (the dimensions must match)
$$
\begin{align}
    A \cdot x &= \begin{pmatrix}
           a_{11} & a_{12} & \cdots & a_{1n} \\
           a_{21} & a_{22} & \cdots & a_{2n} \\
           \vdots & \vdots & \ddots & \vdots \\
           a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
\end{align} \cdot

         \begin{pmatrix}
	   x_1 \\ x_2 \\ \vdots \\  x_{n}
         \end{pmatrix}
= \begin{pmatrix}
    \sum\limits_{j=1}^{n} a_{1j} \cdot x_{j} \\
    \sum\limits_{j=1}^{n} a_{2j} \cdot x_{j} \\ 
    \vdots \\ 
    \sum\limits_{j=1}^{n} a_{mj} \cdot x_{j}
\end{pmatrix}
$$
with $A \cdot x  \in \mathbb{R}^m$.

### Properties

Given $A, B \in \mathbb{R}^{m \times n}$, $x, y \in \mathbb{R}^{n}$ and $\lambda \in \mathbb{R}$
- $A \cdot (x + y) = A \cdot x + A \cdot y$
- $A \cdot (\lambda \cdot x) = \lambda \cdot A \cdot x$
- $(A + B) \cdot x = A \cdot x + B \cdot x$

## Multiplication of 2 Matrices

Given $A \in \mathbb{R}^{l \times m}$, $B \in \mathbb{R}^{m \times n}$ (the dimensions must match).
$$
A \cdot B \in \mathbb{R}^{l \times n}
$$
$$
A = \begin{pmatrix}
   a_{11} & a_{12} & \cdots & a_{1n} \\
   a_{21} & a_{22} & \cdots & a_{2n} \\
   \vdots & \vdots & \ddots & \vdots \\
   a_{l1} & a_{l2} & \cdots & a_{ln}
\end{pmatrix},
B = \begin{pmatrix}
   b_{11} & b_{12} & \cdots & b_{1n} \\
   b_{21} & b_{22} & \cdots & b_{2n} \\
   \vdots & \vdots & \ddots & \vdots \\
   b_{m1} & b_{m2} & \cdots & b_{mn}
\end{pmatrix}
$$
$$
C := A \cdot B \Rightarrow C = (c_{ij})
$$
$$
c_{ij} = \langle \text{row } i \text{ of } A, \text{column } j \text{ of } B \rangle
$$

### Properties

- $A \cdot B \neq B \cdot A$ 
- If $A \in \mathbb{R}^{k \times m}$ and $B,C \in \mathbb{R}^{m \times n}$ then:
	- $A \cdot (B + C) = AB + AC$
- If $A \in \mathbb{R}^{k\times m}$, $B \in \mathbb{R}^{m\times n}$ and $C \in \mathbb{R}^{n\times r}$, then:
	- $ABC = (AB)C = A(BC)$
- If $A \in \mathbb{R}^{k\times m}$ and $B \in \mathbb{R}^{m\times n}$, then:
	- $(AB)^T = B^T A^T$ (see [[Transposition of a Matrix]])

# Symmetric Matrices

A square matrix is called symmetric, if $A^{T} = A \Rightarrow a_{ij} = a_{ji}$.

# Orthogonal Matrices

A square matrix $A \in \mathbb{R}^{n \times n}$ is called orthogonal, if $A \cdot A^{T} = A^{T} \cdot A = I_{n}$ with $I_{n}$ being the Identity Matrix.

## Example

$$
A = \begin{pmatrix}
\cos \alpha & \sin \alpha \\ 
-\sin \alpha & \cos \alpha
\end{pmatrix} 
\quad \Rightarrow \quad
A^{T} = \begin{pmatrix}
\cos \alpha & -\sin \alpha \\ 
\sin \alpha & \cos \alpha
\end{pmatrix} 
$$
with $\cos^{2} \alpha + \sin^{2} \alpha = 1$
$$
A \cdot A^{T} = \begin{pmatrix}
\cos^{2} \alpha + \sin^{2} \alpha & - \cos \alpha \cdot \sin \alpha + \sin \alpha \cdot \cos \alpha \\ 
- \cos \alpha \cdot \sin \alpha + \sin \alpha \cdot \cos \alpha & \sin^{2} \alpha + \cos^{2} \alpha
\end{pmatrix} 
$$
$$
\Rightarrow A \cdot A^{T} = \begin{pmatrix}
1 & 0 \\ 
0 & 1
\end{pmatrix}
$$

# Positive Definite Matrices

A square matrix $A \in \mathbb{R}^{n \times n}$ is positive definite if
- $A$ is symmetric AND
- $\forall x \in \mathbb{R}^{n}: x^{T} \cdot A \cdot x > 0$

# Regularity of a Matrix

A square matrix $A \in \mathbb{R}^{n \times n}$ is called regular (or non-singular), if $\text{rank}(A)=n$ (see [[Rank of a Matrix]]). If not, it is called singular.

# Diagonalizable Matrices

A matrix $A \in \mathbb{R}^{n \times n}$ is called diagonalizable, if there exists an [[Inverse of a Matrix|invertible]] matrix $P \in \mathbb{R}^{n \times n}$ and a diagonal matrix $D \in \mathbb{R}^{n \times n}$ such that:
$$
P^{-1} \cdot A \cdot P = D
$$
$A \in \mathbb{R}^{n \times n}$ is diagonalizable if for every [[Eigenvalue]] $\lambda$ it holds that the [[Eigenvalue#Algebraic Multiplicity|algebraic multiplicity]] is equal to the [[Eigenvalue#Geometric Multiplicity|geometric multiplicity]] $a(\lambda) = g(\lambda)$.

# Special Matrices

## Zero-Matrix

The zero-matrix is a matrix $\sigma \in \mathbb{R}^{m \times n}$ with all elements equal to $0$
-> $\forall A  \in \mathbb{R}^{m \times n}: A + \sigma = A$

## Identity Matrix

The identity matrix is defined as:

$$
I_{n} := \begin{pmatrix}
1 & 0 & 0 & \dots & 0 \\ 
0 & 1 & 0 & \dots & 0 \\ 
0 & 0 & 1 & \dots & 0 \\ 
\vdots & \vdots & \vdots & \ddots & \vdots \\ 
0 & 0 & 0 & \dots & 1
\end{pmatrix}
$$

It acts as the neutral element of matrix multiplication:

$$
\forall A \in \mathbb{R}^{m \times n}: I_{m} \cdot A = A \cdot I_{n} = A
$$
