#uni/courses/math0 

A polynomial is a formal expression of the form

$$
p(x) = \sum\limits_{i=0}^{n} a_{i} x^{i} = a_{n} x^{n} + \dots a_{i} x + a_{0}
$$

Here, $a_{0}, \dots, a_{n} \in \mathbb{R}, n \in \mathbb{N}_0$, are the so-called coefficients of $p$. We denote the set of all real polynomials by $R[x]$

-> By interpreting $x$ as a placeholder for an argument of a function, every $p \in \mathbb{R}[x]$ can be identified with a real-valued map $p: \mathbb{R} \rightarrow \mathbb{R}, x \mapsto p(x)$

# Degree

Let $p(x)$ be a polynomial:
- if $a_{n} \neq 0$, then $a_n$ is called the leading coefficient of $p$
- the degree os p is defined by
	- $\deg(p):= n$ if $a_{n}\neq 0$
	- $\deg(p):= - \infty$ if $p(x) = a_{0} = 0$

The polynomial $p=0$ is called the zero-polynomial.

Polynomials of degree one are called affine-linear.

# Zeros of Polynomials

A number $x_{0} \in \mathbb{R}$ is called a zero of a polynomial $p \in \mathbb{R}[x]$ if $p(x_{0}) = 0$ holds.

- If $\deg p = - \infty$, then every $x \in \mathbb{R}$ is a zero of $p$
- If $\deg p = 0$, then $p$ has no zeros
- If $\deg p = 1$, then $p(x) = a_{1} x + a_{0}$ has precisely one zero at $x_{0} = - \frac{a_{0}}{a_{1}}$
- If $\deg p = 2$, then $p(x)$ depends on the so-called discriminant $\Delta := a_{1}^{2} - 4 a_{2} a_{0}$ of $p$
	- If $\Delta = 0$, then $p$ has precisely one zero at $x = - \frac{a_{1}}{2a_{2}}$
	- If $\Delta < 0$, then $p$ has no Zeros
	- If $\Delta > 0$, then $p$ has precisely two zeros:
		- $x_{1} = \frac{-a_{1} + \sqrt{\Delta}}{2 a_{2}}$
		- $x_{2} = \frac{-a_{1} - \sqrt{\Delta}}{2 a_{2}}$
- If $\deg p \in \{3, 4\}$, then there still exist closed formulas for some zeros of $p$
- if $\deg p \ge 5$, then there exist no general formulae for the zeros of $p$

## Theorem of Vieta

If $p \in \mathbb{R}[x]$ has the form $p(x) = x^{2} + a_{1}x + a_0$ and there exist $x1, x2 \in \mathbb{R}$ with $a_{1} = -(x_{1} + x_{2})$, $a_{0} = x_{1} \cdot x_{2}$, then $x_{1}, x_{2}$ are the zeros of p.

# Polynomial Division
https://www.cuemath.com/algebra/dividing-polynomials/

# Factorization

Factorization wants to find the finest possible decomposition of a polynomial such that the parts can not be divided anymore.

## Example

$p(x) = x^{3}- 1 = (x-1)(x^{2}+x+1)$ <- can not be split into further factors, because $x^{2}+x+1$ can not be zero.

## Process

1. Identify a zero of the polynomial (by trial and error)
2. Do polynomial division on the original formula to identify the second factor
3. Check if the second factor has a zero, if yes, return to step one with the second factor

# Partial Fraction Decomposition

Finest decompositions can be used to rewrite rational functions (fractions of polynomials) as simply as possible to aid [[Integration|integration]]

## Process

https://www.purplemath.com/modules/partfrac.htm