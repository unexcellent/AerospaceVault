#uni/courses/math1 

The kernel of a [[Matrix|matrix]] $A$ is a [[Vector Space|sub vector space]] resulting from the solution of the [[Linear Systems of Equations|linear system of equations]] $Ax = 0$
-> $\ker A = \{\forall x \in \mathbb{R}^{n}: Ax=0 \}$

# Example

$$
A = \begin{pmatrix}
1 & 2 & -1 \\
2 & -1 & 3 \\ 
-2 & 6 & -8
\end{pmatrix}, \quad
\widetilde{A} = \begin{pmatrix}
1 & 2 & -1 \\ 
0 & -5 & 5 \\ 
0 & 0 & 0 \\ 
\end{pmatrix} \quad \widetilde{A}x = 0
$$
$$
\begin{align}
x_{1} + 2x_{2} - x_{3} = 0 \\
-5x_{2} + 5x_{3} = 0
\end{align}
$$
$$
\Rightarrow \quad x_{2}= x_{3}, \quad x_{1} = -x_{3}
$$

$\ker A = \{ x = \begin{pmatrix} -\alpha \\ \alpha \\ \alpha \end{pmatrix}, \forall \alpha \in \mathbb{R} \} = \{ x = \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}, \forall \alpha \in \mathbb{R} \}$
$$
\Rightarrow \text{span} \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix} \quad \Rightarrow \quad \ker A \neq \{0\} \quad \Rightarrow \quad \dim \ker A = 1
$$
$x_{h}: Ax_{h} = 0$ this is the same as saying that $x_{h} \in \ker A = \text{span} \begin{pmatrix} -1 \\1\\ 1\end{pmatrix}$. 
