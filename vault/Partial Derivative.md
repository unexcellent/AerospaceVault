#uni/courses/math2 

A [[Function]] $f(x)$ with multiple inputs $x = (x_{1}, \dots, x_{n})$ can be [[Derivative|derived]] by a single parameter $x_{i}$ with $i \in \{ 1, \dots, n \}$ by
$$
\frac{\partial f}{\partial x_{i}}(x) := \lim_{h \to 0} \frac{f(x_{1}, \dots, x_{i} + h, \dots x_{n}) - f(x_{1}, \dots, x_{i}, \dots x_{n})}{h}
$$

$f$ is partially differentiable at $x$ if all partial derivatives $\frac{\partial f}{\partial x_{i}}(x)$ exist.

Note that the order of derivatives matters
$$
\frac{\partial^{2}f}{\partial x_{j} \ \partial x_{i}} \neq \frac{\partial^{2}f}{\partial x_{i} \ \partial x_{j}}
$$

# Directional Derivative

The derivative of $f$ can be calculated in any direction at point $x_{0} \in \mathbb{R}^{n}$ via the directional **unit** vector $v \in \mathbb{R}^{n}$ via
$$
\frac{\partial f}{\partial v} (x_{0}) = \sum^{n}_{i=1} \frac{\partial f}{\partial x_{i}} (x_{0}) \cdot v_{i}
$$

# Gradient

The gradient of $f$ is a [[Vector]], that points in the direction of greatest change of $f$ and is defined by:
$$
(\nabla f)(x_{0}) := \begin{pmatrix}
(\partial_{x_{1}}f)(x_{0})  \\ 
\vdots \\ 
(\partial_{x_{n}}f)(x_{0})
\end{pmatrix} \in \mathbb{R}^{n}
$$

# Hessian

The $n \times n$ [[Matrix]] consisting of all $n^{2}$ second partial derivatives $\partial_{x_{j}x_{i}}f$ for $i, j = 1, \dots, n$, is called the Hessian (matrix) of $f$ at $x$. We denote it as
$$
\text{Hess} (f)(x) := H_{f}(x) := \begin{pmatrix}
(\partial_{x_{1}x_{1}}f)(x) & \dots & (\partial_{x_{1}x_{n}}f)(x) \\ 
\vdots & \ddots & \vdots \\ 
(\partial_{x_{n}x_{1}}f)(x) & \dots & (\partial_{x_{n}x_{n}}f)(x)
\end{pmatrix}
$$

# Chain Rule

Let $g, h$ be functions of one real parameter $x$ with values in $\mathbb{R}^{n}$. Let $f$ be a function defined as $f(x) = g( \ h(x) \ )$. Then the derivative of $f$ is defined by
$$
f'(x) = \sum^{n}_{k=1} \frac{\partial g(\ h(x) \ )}{\partial h_{k}(x)} \cdot h_{k}'(x)
$$
