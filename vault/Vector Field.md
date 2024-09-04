#uni/courses/math2 

Given a non-empty set $U \subset R^{n}$, a [[Function]] $v: U \to \mathbb{R}^{n}$ is called a vector field.
$$
v(x) = v(x_{1}, \dots, x_{n}) = \begin{pmatrix}
v_{1}(x_{1}, \dots, x_{n}) \\ 
\vdots \\ 
v_{n}(x_{1}, \dots, x_{n})
\end{pmatrix}
$$

![[Pasted image 20240617201929.png|400]]

$v$ is called a $C^{k}$-vector field if each component function $v_{i}$ is $k$-times continuously differentiable on $U$.
The real [[Vector Space]] of all $C^{k}$-vector fields over $U$ is denoted by $\Gamma^{(k)}(U)$.

# Curl

The curl operator only exists if $U \subseteq \mathbb{R}^{3}$ and is defined as
$$
\text{curl } v := \nabla \times v =  \begin{pmatrix}
\partial_{2} & v_{3} - \partial_{3} & v_{2} \\ 
\partial_{3} & v_{1} - \partial_{1} & v_{3} \\ 
\partial_{1} & v_{2} - \partial_{2} & v_{1} \\ 
\end{pmatrix}
$$
