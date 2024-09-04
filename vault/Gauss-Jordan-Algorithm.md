#uni/courses/math1 

The Gauss-Jordan-Algorithm is an extension of the [[Gauss-Algorithm]], which converts a square [[Matrix|matrix]] in the upper-triangular form into the [[Matrix#Identity Matrix|identity matrix]].

Given $A \in \mathbb{R}^{n \times n}$ in the upper triangular form:
$$
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1n} \\ 
0 & a_{22} & a_{23} & \cdots & a_{2n} \\ 
0 & 0 & a_{33} & \cdots & a_{3n} \\ 
\vdots & \vdots & \vdots & \ddots & \vdots \\ 
0 & 0 & 0 & \cdots & a_{nn}
\end{pmatrix}
$$
The Gauss-Algorithm is applied in reverse, until the identity matrix is reached.