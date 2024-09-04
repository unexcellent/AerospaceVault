#uni/courses/math1 

Given two different [[Basis of a Vector Space|vector space bases]] $V = \{v_{1}, v_{2}, \dots, v_{n}\}$, $W = \{w_{1}, w_{2}, \dots, w_{n}\}$, the change of basis describes the transformation of any [[Vector|vector]] into the other basis' coordinate system.
Any vector $x_{V} \in V$ can by [[Linear Transformation|transformed]] into an equivalent vector $x_{W} \in W$ via
$$
x_{W} = \begin{pmatrix}
| & | &  & | \\ 
v_{1} & v_{2} & \cdots & v_{n} \\ 
| & | &  & | \\ 
\end{pmatrix}^{-1} 
\cdot x_{V} \cdot 
\begin{pmatrix}
| & | &  & | \\ 
w_{1} & w_{2} & \cdots & w_{n} \\ 
| & | &  & | \\ 
\end{pmatrix}
$$