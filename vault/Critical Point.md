#uni/courses/math2 

A point $x_{0} \in \mathbb{R}^{n}$ at which a [[Function]] $f : \mathbb{R}^{n} \to \mathbb{R}$ has a [[Partial Derivative#Gradient|gradient]] of $0$.
$$
\nabla f (x_{0}) = 0
$$
If the critical point is a maximum or a minimum, it is also called a local extremum.

# Maximum

A local extremum is called a maximum if
$$
\frac{\partial^{2} f}{\partial^{2}x_{1}}(x) > 0 \quad \text{and} \quad \det H_{f}(x) > 0
$$
-> $\det$: [[Determinant of a Matrix]]
-> $H_{f}$: [[Partial Derivative#Hessian|Hessian]] of $f$

If $n = 1$, then $\det H_{f}(x) = f''(x)$.
![[Pasted image 20240611174211.png|300]]

# Minimum

A local extremum is called a minimum if
$$
\frac{\partial^{2} f}{\partial^{2}x_{1}}(x) < 0 \quad \text{and} \quad \det H_{f}(x) > 0
$$
-> $\det$: [[Determinant of a Matrix]]
-> $H_{f}$: [[Partial Derivative#Hessian|Hessian]] of $f$

If $n = 1$, then $\det H_{f}(x) = f''(x)$.
![[Pasted image 20240611174226.png|300]]

# Sattle Point


A local extremum is called a minimum if
$$
\det H_{f}(x) < 0
$$
-> $\det$: [[Determinant of a Matrix]]
-> $H_{f}$: [[Partial Derivative#Hessian|Hessian]] of $f$

If $n = 1$, then $\det H_{f}(x) = f''(x)$.
![[Pasted image 20240611174239.png|300]]