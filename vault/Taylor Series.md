#uni/courses/math1 #uni/courses/math2 

A Taylor [[Series of Numbers|series]] is an approximation of a [[Function]] $f(x)$ around at a certain point $p$, which results in a [[Polynomial and Rational Functions|polynomial]].
$$
T(x) = f(p) + f'(p) \cdot (x-p) + \dfrac{f''(p)}{2!} \cdot (x - p)^{2} + \dfrac{f'''(p)}{3!} \cdot (x - p)^{3} + \dots
$$

The more terms are added to the series, the more accurately $f(x)$ is approximated.

In general, the polynomial is capped to a certain order.

The general term is:
$$
T(x) = \sum_{k=0}^{n} \dfrac{f^{(k)}(p)}{k!} (x - p)^{k} + e^{(n)}_{p}(x)
$$
with the error term $e$ describing the difference between the approximation and the actual function.

The following sections work with the example function $f(x) = e^{x}$ at the point $p=1$

# 0th-Order

The 0th-order Taylor polynomial only defines the value at the point $p$.
$$
T(x) = f(p) \cdot x^{0} = e
$$
```functionplot
---
xLabel: x
yLabel: y
bounds: [-1, 3, -0.5, 7.5]
grid: true
---
f(x) = exp(x)
T(x) = exp(1)
```

# 1st-Order

The 1th-order Taylor polynomial only defines the value at the point $p$ and the slope at that $p$.
$$
T(x) = f(p) \cdot x^{0} + f'(p) \cdot (x-p)
$$
$$
= e \cdot x
$$
```functionplot
---
xLabel: x
yLabel: y
bounds: [-1, 3, -0.5, 7.5]
grid: true
---
f(x) = exp(x)
T(x) = exp(1) * x
```

# 2nd-Order

$$
T(x) = f(p) \cdot x^{0} + f'(p) \cdot (x-p) + \dfrac{f''(p)}{2!} \cdot (x - p)^{2}
$$
$$
= \frac{e}{2} (x^{2} + 1)
$$
```functionplot
---
xLabel: x
yLabel: y
bounds: [-1, 3, -0.5, 7.5]
grid: true
---
f(x) = exp(x)
T(x) = exp(1)/2 * (x^2 + 1)
```

# 3rd-Order

$$
T(x) = f(p) + f'(p) \cdot (x-p) + \dfrac{f''(p)}{2!} \cdot (x - p)^{2} + \dfrac{f'''(p)}{3!} \cdot (x - p)^{3}
$$
$$
= \frac{e}{2} \cdot (x^{2} + 1) + \frac{e}{3}\cdot(x-1)^{3}
$$
```functionplot
---
xLabel: x
yLabel: y
bounds: [-1, 3, -0.5, 7.5]
grid: true
---
f(x) = exp(x)
T(x) = exp(1)/2 * (x^2 + 1) + exp(1)/3 *(x-1)^3
```

# Lagrange Error

$$
e_{p}^{(n)}(x) = \dfrac{f^{(n+1)}(\xi_{x})}{(n+1)!}
$$
with $\xi_{x} \in (x, p)$. 

# Multi Dimensional

If $f$ takes multiple input arguments $x \in \mathbb{R}^{n}$, then the second order Taylor polynomial can be calculated by
$$
T(x) = f(p) + \left\langle \ \nabla f(p), \ x-p \ \right\rangle + \frac{1}{2} \langle \ x-p, \ H_{f}(p) \cdot (x-p) \rangle
$$
-> $\nabla f$: [[Partial Derivative#Gradient|gradient]] of $f$
-> $H_{f}$: [[Partial Derivative#Hessian|hessian]] of $f$