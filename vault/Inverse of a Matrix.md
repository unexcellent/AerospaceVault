#uni/courses/math1 

A square [[Matrix|matrix]] $A \in \mathbb{R}^{n \times n}$ is called invertible, if there exists a matrix $A^{-1} \in \mathbb{R}^{n \times n}$, such that
$$
A \cdot A^{-1} = A^{-1} \cdot A = I_{n}
$$
with $I_{n}$ referring to the [[Matrix#Identity Matrix|identity matrix]]. 

The inverse matrix can be calculated by combining $A$ and $I_n$ into a single [[Linear Systems of Equations|system of equations]].
$$
(A|I_{n}) = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} & |  & 1 & 0 & \cdots & 0 \\ 
a_{21} & a_{22} & \cdots & a_{2n} & | &  0 & 1 & \cdots & 0 \\ 
\vdots & \vdots & \ddots & \vdots &  & \vdots & \vdots & \ddots & \vdots \\ 
a_{n1} & a_{n2} & \cdots & a_{nn} & | & 0 & 0 & \cdots & 1
\end{pmatrix}
$$
The left side of the equation should then first be converted into the upper-triangular form and then the identity matrix using the [[Gauss-Jordan-Algorithm]]. The matrix on the right side is then equal to $A^{-1}$.

# Properties

- If $A$ is invertible, then $A$ is [[Matrix#Regularity of a Matrix|regular]]
- $(A^{-1})^{-1} = A$
- $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$
- $(A^{T})^{-1} = (A^{-1})^{T}$ (see [[Transposition of a Matrix]])

