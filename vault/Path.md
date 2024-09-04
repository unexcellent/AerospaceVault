#uni/courses/math2 

Symbol: $\varphi$

A path is the parametrization of a [[Curve]] by [[Function]] that maps from a continuous [[Interval]] $I \subseteq \mathbb{R}$ to $\mathbb{R}^{n}$.
$$
\varphi(t) = \begin{pmatrix}
\varphi_{1}(t) \\ 
\vdots \\ 
\varphi_{n}(t)
\end{pmatrix}
$$
Different paths can result in the same curve.

# Length

The length of a curve resulting from a path can be calculated via
$$
L(\varphi) = \int_{I} || \varphi'(t) || \ dt
$$

# Tangent

The vector tangent to the path is defined as
$$
\hat{\tau}(t) = \frac{\varphi'(t)}{||\varphi'(t)||}
$$

# Classification

## Regular

A path is called regular if its [[Derivative]] is non-zero for the entire interval $I$
$$
\varphi'(t) \neq 0 \ \ \forall t \in I
$$

## Simple

A path is called simple if for any pair of points $t_{1}, t_{2} \in I$ $\varphi(t_{1}) \neq \varphi(t_{2})$.

## Closed

A path is called called closed it starts and ends at the same point. 
$$
I:= [a,b], \quad \varphi(a) = \varphi(b)
$$

## Rectifiable

A path is called rectifiable if it has a finite length. Any path, that is differentiable at least once is rectifiable.

## Equivalent

Two paths $\varphi : I \to \mathbb{R}^{n}$ and $\psi : I* \to \mathbb{R}^{n}$ are called equivalent if there exists a parameter transformation $g : I* \to I$ such that
$$
\psi = \varphi \circ g
$$