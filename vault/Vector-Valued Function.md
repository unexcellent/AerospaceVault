#uni/courses/math2 

A vector valued function $f : \mathbb{R}^{n} \to \mathbb{R}^{m}$ is a [[Function]], that takes multiple parameters as an input and outputs a [[Vector]]. $f$ can be written in the form
$$
f(x_{1}, \dots, x_{n}) = \begin{pmatrix}
f_{1}(x_{1}, \dots, x_{n}) \\ 
\vdots \\ 
f_{m}(x_{1}, \dots, x_{n})
\end{pmatrix}
$$

# Partial Derivative

$f$ can be [[Partial Derivative|derived]] via
$$
\frac{\partial f}{\partial x_{i}} (x_{0}) = \begin{pmatrix}
\dfrac{\partial f_{1}(x_{0})}{\partial x_{i}} \\ 
\vdots \\ 
\dfrac{\partial f_{m}(x_{0})}{\partial x_{i}}
\end{pmatrix}
$$

# Jacobian

The jacobian or derivative [[Matrix]] $df(x_{0}) \in \mathbb{R}^{m \times n}$ contains all derivatives of $f$ and is defined as
$$
df(x_{0}) = \begin{pmatrix}
\dfrac{\partial f_{1}(x_{0})}{\partial x_{i}} & \cdots & \dfrac{\partial f_{1}(x_{0})}{\partial x_{n}} \\ 
\vdots & \ddots & \vdots \\ 
\dfrac{\partial f_{m}(x_{0})}{\partial x_{i}} & \cdots & \dfrac{\partial f_{m}(x_{0})}{\partial x_{n}}
\end{pmatrix}
$$
