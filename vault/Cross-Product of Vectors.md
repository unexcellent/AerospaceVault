#uni/courses/math0 
#uni/courses/math1 

Given two [[Vector|vectors]] $a, b \in \mathbb{R}^3$, we define:

$$
\begin{align}
    a \times b &= \begin{pmatrix}
           a_{2} \cdot b_{3} - a_3 \cdot b_2 \\
           a_{3} \cdot b_{1} - a_1 \cdot b_3 \\
           a_{1} \cdot b_{2} - a_2 \cdot b_1 \\
         \end{pmatrix}
\end{align}
$$
$$
||a \times b||= ||a||\cdot ||b|| \cdot \sin \angle (a, b)
$$
The length of the vector product is equal to the area of a parallelogram spanned by $a$ and $b$ and is orthogonal to $a$ and $b$.

![[Pasted image 20231028211608.png|400]]

# Using the Kronecker Delta

The cross product can be calculated using the [[Determinant of a Matrix|determinant of a matrix]] and the [[Kronecker Delta]] as follows:
Given $v, w \in \mathbb{R}^{3}$
$$
\begin{gather}
v \times w = \det\begin{bmatrix}
v_{1} & w_{1} & e_{1} \\ 
v_{2} & w_{2} & e_{2} \\ 
v_{3} & w_{3} & e_{3} \\ 
\end{bmatrix}
\\\\ 
= v_{2} w_{3} e_{1} + v_{3} w_{1} e_{2} + v_{1} w_{1} e_{3} - v_{3} w_{2} e_{1} - v_{1} w_{3} e_{2} - v_{2} w_{1} e_{3} 
\\\\
= e_{1} (v_{2} w_{3} - v_{3} w_{2}) + e_{2} (v_{3} w_{1} - v_{1} w_{3}) + e_{3} (v_{1} w_{2} - v_{2} w_{1})
\end{gather}
$$

# Axioms

$\forall a, b, c \in \mathbb{R}^3$:
- $a \times b = -b \times a$
- $(a \times b) \perp a \wedge (a \times b) \perp b$
- $a, b, a \times b$ obey the right-hand-rule
- Jacobi-Identity: $a \times (b \times x) + b \times (c \times a)+ c \times (a \times b) = 0$
- Graßmann-Identity: $(a \times b) \times c = <a,b> \times b - <b,c> \times a$