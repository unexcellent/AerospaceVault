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

# For [[First Order Linear System of ODEs]]

For the classification of the critical points, the [[Eigenvalue|eigenvalues]] of the ODE system $\lambda_{1}, \lambda_{2}$ need to be determined.

## Types

### Improper Node

For $\lambda_{1} \neq \lambda_{2}$, $\lambda_{1} \cdot \lambda_{2} > 0$ and $\lambda_{1}, \lambda_{2} \in \mathbb{R}$
![[Pasted image 20250208170040.png|500]]

### Proper Node / Degenerate Node

For $\lambda_{1} = \lambda_{2}$ and $\lambda_{1}, \lambda_{2} \in \mathbb{R}$
![[Pasted image 20250208170244.png|500]]

### Saddle Point

For $\lambda_{1} < 0, \lambda_{2} > 0$ and $\lambda_{1}, \lambda_{2} \in \mathbb{R}$
![[Pasted image 20250208170434.png|500]]

### Center

For $Re(\lambda_{1}) = Re(\lambda_{2}) = 0$ and $\lambda_{1} = \overline{\lambda_{2}}$
![[Pasted image 20250208170806.png|500]]

### Spiral Point

For $Re(\lambda_{1}) = Re(\lambda_{2}) \neq 0$ and $\lambda_{1} = \overline{\lambda_{2}}$
![[Pasted image 20250208170950.png|500]]

## Stability

| Stability             | Condition                                                                           |
| --------------------- | ----------------------------------------------------------------------------------- |
| asymptotically stable | $\lambda_{1} + \lambda_{2} < 0 \quad \land \quad \lambda_{1} \cdot \lambda_{2} > 0$ |
| stable                | $\lambda_{1} + \lambda_{2} = 0 \quad \land \quad \lambda_{1} \cdot \lambda_{2} > 0$ |
| unstable              | $\lambda_{1} + \lambda_{2} > 0 \quad \vee \quad \lambda_{1} \cdot \lambda_{2} < 0$  |

# For Non-Linear Systems

Non-linear ODEs can be converted into a [[First Order Linear System of ODEs]] where the critical points can be classified like above.

1. Introduce two substitution functions $x_{1}=y$ and $x_{2} = y'$
2. Set up the system with those functions using $x'_{1}$ and $x'_{2}$
3. Find the points where $x'_{1} = x'_{2} = 0$
4. Calculate the [[Vector-Valued Function#Jacobian|Jacobian]]
5. For every critical point, follow the steps above with the matrix being the critical point inserted into the Jacobian