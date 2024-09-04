#uni/courses/math1 

The determinant is a powerful tool to study [[Linear Independence of Vectors|linear independence]] of systems of vectors ([[Matrix]]). The [[Gauss-Algorithm]] (without swapping lines) does not change the determinant of a matrix.

# Calculation
## For a $2\times 2$ Matrix

$$
A = \begin{pmatrix}
a_{11} & a_{12} \\ 
a_{21} & a_{22}
\end{pmatrix} \quad \Rightarrow \quad  
|A| = a_{11} \cdot a_{22} - a_{12} \cdot a_{21}
$$

## For a $3\times 3$ Matrix

$$
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\ 
a_{21} & a_{22} & a_{23} \\ 
a_{31} & a_{32} & a_{33} \\ 
\end{pmatrix} \quad \Rightarrow \quad 
\begin{align}
|A| = a_{11} \cdot a_{22} \cdot a_{33} + a_{12} \cdot a_{23} \cdot a_{31} \\ + a_{21} \cdot a_{32} \cdot a_{13} - a_{32} \cdot a_{23} \cdot a_{11} \\ - a_{21} \cdot a_{12} \cdot a_{33}
\end{align}
$$

![[Pasted image 20231025132511.png|500]]

## For larger Matrices

Use the [[Laplace Development]] Algorithm to reduce the dimensions.

# Properties

- $\det A = \det A^{T}$
- Swapping rows or columns of a matrix multiplies the determinant by $-1$
- $\det \begin{pmatrix} \vdots \\ \alpha \cdot a_{k}^{T} \\ \vdots \end{pmatrix} = \alpha \det \begin{pmatrix} \vdots \\ a_{k}^{T} \\ \vdots \end{pmatrix}$ (see [[Linear Independence of Vectors]])
- $\det \begin{pmatrix} \vdots \\ a_{k}^{T} + b_{k}^{T} \\ \vdots \end{pmatrix} = \det \begin{pmatrix} \vdots \\ a_{k}^{T} \\ \vdots \end{pmatrix} + \det \begin{pmatrix} \vdots \\ b_{k}^{T} \\ \vdots \end{pmatrix}$ 
- $\det(A \cdot B) = \det A \cdot \det B, \quad \forall A, B \in \mathbb{R}^{n \times n}$
- $\det A^{-1} = \frac{1}{\det A}$
- $\det (A+B) \neq \det A + \det B$
- $\det (\alpha A) = \alpha^{n} \det A$
