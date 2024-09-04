#uni/courses/math2 

A [[Sequence of Numbers|sequence]] where every element is a [[Function]] $f_{n}(x)$.

```functionplot
---
xLabel: x
yLabel: y
bounds: [-2, 2, 0, 5]
grid: true
---
f_0(x) = 1 * x^2
f_1(x) = 2 * x^2
f_2(x) = 3 * x^2
f_3(x) = 4 * x^2
f_4(x) = 5 * x^2
```

# Convergence

Sequences of Functions can [[Series Convergence|converge]] to a function $f_{\infty}(x) = f(x)$
$$
\lim_{n \to \infty} f_{n}(x) = f(x)
$$
-> https://www.youtube.com/watch?v=GsORKmBCLuI

## Pointwise Convergence

A sequence of functions $f_{n}(x)$ is said to be pointwise convergent to a function $f(x)$ if
$$
\forall x: \lim_{n \to \infty} f_{n}(x) = f(x)
$$

Formally:
$$
\forall \varepsilon > 0 \quad 
\forall x \quad 
\exists N = N(\varepsilon, x) \in \mathbb{N} \quad
\forall n \ge N: \quad 
|f(x) - f_{n}(x)| < \varepsilon
$$

## Uniform Convergence

A sequence of functions $f_{n}(x)$ is said to be uniform convergent to a function $f(x)$ if it is pointwise continuous and $f(x)$ is continuous.

Formally:
$$
\forall \varepsilon > 0 \quad 
\exists N = N(\varepsilon) \in \mathbb{N} \quad
\forall x \quad 
\forall n \ge N: \quad 
|f(x) - f_{n}(x)| < \varepsilon
$$

# Limit Operations

Aside from the operation detailed in [[Limit of a Sequence]] and [[Limit of a Function]], there exist special limit rules for sequences of functions
- $\displaystyle \lim_{n \to \infty} \int^{b}_{a} f_{n}(x) = \int^{b}_{a} \lim_{n \to \infty} f_{n}(x)$ if $f_{n}(x)$ converges uniformly
- $\displaystyle \lim_{n \to \infty} f'_{n}(x) =  \left(\lim_{n \to \infty} f_{n}(x)\right)'$ if $f_{n}(x)$ converges uniformly