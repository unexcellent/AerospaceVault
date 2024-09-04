#uni/courses/math0 
#uni/courses/math1 

Consider an open interval $D \subset \mathbb{R}$ and a continuous [[Function|function]] $f: D \rightarrow \mathbb{R}$. Let $x_{0} \in D, h \in \mathbb{R}\backslash \{0\}$ be fixed such that $x_{0}+ h \in D$.
```functionplot
---
xLabel: x
yLabel: y
bounds: [-2, 2, -1.5, 1.5]
grid: true
---
f(x) = 0.5x^3 + x^2
g(x) = 11/8 * x - 3/8
```

Then the secant through the points $(x_{0}, f(x_{0})), (x_{0}+h, f(x_{0}+h))$ i.e. the affine-linear function whose graph passes through these points has the slope:
$$
\frac{f(x_{0}+ h) - f(x_{0})}{h}
$$

A function $f: D \rightarrow \mathbb{R}$ defined on an open interval $D \subset \mathbb{R}$ is called differentiable at $x_{0} \in D$ if the limit 
$$
\lim_{h \rightarrow 0} \frac{f(x_{0}+ h) - f(x_{0})}{h} = f'(x_{0}) = \frac{df}{dx}(x_{0})
$$
exists. In this case, $f'(x_{0})$ is called the derivative of $f$ at $x_0$. The function $f$ is differentiable on $D$ if $f$ is differentiable everywhere.

# Rules

Given $a,b \in \mathbb{R}$

| Function             | Derivative                                              |
| -------------------- | ------------------------------------------------------- |
| $x^{b}$              | $b \cdot x^{b-1}$                                       |
| $a \cdot f(x)$       | $a \cdot f'(x)$                                         |
| $f(x) + g(x)$        | $f'(x) + g'(x)$                                         |
| $f(x) \cdot g(x)$    | $f'(x) \cdot g(x) + f(x) \cdot g'(x)$                   |
| $\dfrac{f(x)}{g(x)}$ | $\dfrac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{g(x)^{2}}$ |
| $f(g(x))$            | $f'(g(x)) \cdot g'(x)$                                  |
| $\sin x$             | $\cos x$                                                |
| $\cos x$             | $- \sin x$                                              |
| $\tan x$             | $\sec^{2} x$                                            |
| $\arcsin x$          | $\dfrac{1}{\sqrt{1-x^{2}}}$                             |
| $\arccos x$          | $-\dfrac{1}{\sqrt{1-x^{2}}}$                            |
| $\arctan x$          | $\dfrac{1}{1+x^{2}}$                                    |
| $e^{x}$              | $e^{x}$                                                 |
| $\ln x$              | $\dfrac{1}{x}$                                          |
| $\log_{a}x$          | $\dfrac{1}{x \cdot \ln a}$                              |
| $a^{x}$              | $\ln(a) \cdot a^{x}$                                                      |

# Derivative of Inverse Function

Suppose that $D_{1}, D_{2} \subset \mathbb{R}$ are open intervals, that $f: D_{1} \rightarrow D_{2}$ is bijective and differentiable with a non-vanishing derivative and that $f^{-1}: D_{2} \to D_{1}$ is the inverse of f. Then
$$
(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))}
$$