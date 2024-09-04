#uni/courses/math0 #uni/courses/math2 

# Fundamental Theorem of Calculus

A differentiable [[Function|function]] $F: [a, b] \to \mathbb{R}$ called an anti-[[Derivative|derivative]] is a continuous function $f: [a, b] \to \mathbb{R}$ if $F'=f$
-> Antiderivatives are unique except for a constant $c \in \mathbb{R}$ $F = G + c$
$$
\int\limits^{b}_{a} f(x)dx = F(b) - F(a)
$$

# Indefinite Integral

If $F: [a, b] \to \mathbb{R}$ is an antiderivative of $f: [a, b] \to \mathbb{R}$ then the set of all antiderivatives of f is called the indefinite integral of f and denoted by
$$
\int f(x)dx := \{F+c | c \in \mathbb{R}\} = F + c
$$

# Examples

Given $a,b,C \in \mathbb{R}$

| Function       | Integral                                          |
| -------------- | ------------------------------------------------- |
| $x^{b}$        | $\dfrac{x^{b+1}}{b+1} + C$                        |
| $a \cdot f(x)$ | $a \cdot \int f(x)$                               |
| $f(x) + g(x)$  | $\int f(x) + \int g(x)$                           |
| $\sin x$       | $-\cos x + C$                                     |
| $\cos x$       | $\sin x + C$                                      |
| $\sin^{2} x$   | $\frac{x-\sin(x) \cdot \cos(x)}{2}$               |
| $\cos^{2} x$   | $\frac{x-\sin(x) \cdot \cos(x)}{2}$               |
| $\tan^{2} x$   | $\tan(x) - x$                                     |
| $\sin^{3} x$   | $\frac{1}{12} \cdot (\cos(3x) - 9 \cdot \cos(x))$ |
| $\cos^{3} x$   | $\frac{1}{12} \cdot (\sin(3x) + 9 \cdot \sin(x))$ |
| $e^{x}$        | $e^{x} + C$                                       |
| $\frac{1}{x}$  | $\ln{x} + C$                                      |
| $\log_{a}x$    | $\dfrac{1}{x \cdot \ln a} + C$                    |
| $\sqrt{x}$     | $\frac{2}{3} \cdot \sqrt{x^3}$                    |

## Integration by Parts

$$
\int^{b}_{a} u(x) \cdot v'(x) \ dx
$$
$$
= u(b) \cdot v(b) - u(a) \cdot v(a) - \int_{a}^{b} u'(x) \cdot v(x) \ dx
$$

# In Multiple Dimensions

![[Pasted image 20240618144541.png]]

## Rectangular Region

Given a rectangular base $R = [a,b] \times [c,d]$ with $a,b,c,d \in \mathbb{R}$, the theorem of Fubini states, that
$$
\iint_{R} f(x,y) \ dA(x,y) = \int^{d}_{c} \left( \int_{a}^{b} f(x,y) \ dx \right) dy = \int^{b}_{a} \left( \int_{c}^{d} f(x,y) \ dy \right) dx
$$

The double integral is linear:
- $\iint_{R} \big( f(x,y) \pm g(x,y) \big) \ dA = \iint_{R} f(x,y) \ dA \pm \iint_{R} g(x,y) \ dA$ 
- $\iint_{R} \lambda f(x,y) \ dA = \lambda \cdot \iint_{R} f(x,y) \ dA$

and if $f(x,y) \equiv h(x) \cdot k(y)$, then
$$
\iint_{R} f(x,y) \ dA = \left( \int_{a}^{b} h(x) \ dx \right) \cdot \left( \int_{c}^{d} k(y) \ dy \right)
$$

## In $\mathbb{R}^{2}$

### $x$-Axis Normal Region

A **normal region** in $\mathbb{R}^{2}$ w.r.t. the $x$-axis is given by
$$
D = \left\{ (x,y) \in \mathbb{R}^{2} \quad | \quad a \le x \le b, \quad \alpha(x) \le y \le \beta(x) \right\}
$$
![[Pasted image 20240618150237.png]]
In that case
$$
\iint_{D} f(x,y) \ dA = \int_{a}^{b} \left( \int_{\alpha(x)}^{\beta(x)} f(x,y) \ dx \right) dy
$$

### $y$-Axis Normal Region

A **normal region** in $\mathbb{R}^{2}$ w.r.t. the $y$-axis is given by
$$
E = \left\{ (x,y) \in \mathbb{R}^{2} \quad | \quad c \le y \le d, \quad \gamma(y) \le x \le \delta(y) \right\}
$$
![[Pasted image 20240618150327.png]]

in which case we call it a normal region w.r.t. the $y$-axis.

In that case
$$
\iint_{E} f(x,y) \ dA = \int_{c}^{d} \left( \int_{\gamma(y)}^{\delta(y)} f(x,y) \ dy \right) dx
$$

### General Regions in $\mathbb{R}^{2}$

Non-normal regions can be integrated by cutting the region into normal regions $G = G_{1} \cup G_{2} \cup G_{3}$![[Pasted image 20240620100426.png]]

## In $\mathbb{R}^{n}$

### $n$-Dimensional Box

A $n$-dimensional box can be viewed as a higher-dimensional rectangle with
$$
B_{n} := [a_{1}, b_{1}] \times [a_{2}, b_{2}] \times \cdots \times [a_{n}, b_{n}]
$$
A function $f$ can then be integrated over $B_{n}$ via
$$
\int \cdots \int_{B_{n}} f(x) \ dV_{n} = \int^{b_{1}}_{a_{1}} \cdots \int^{b_{n}}_{a_{n}} f(x_{1}, \dots x_{n}) \ dx_{n} \dots dx_{2} \ dx_{1}
$$

# Integration by Substitution

A useful technique for simplifying integration is changing the variables.

Let $U, V \subseteq \mathbb{R}^{n}$ and $f : U \to V$, $g : U \to g(u)$ 
![[Pasted image 20240624145934.png]]
Then
$$
\int \cdots \int_{V} f(x) \ dV_{n}(x) = \int \cdots \int_{U} f( \ g(u) \ ) \cdot |\det J_{g}(u)| \ dV_{n}(u)
$$
-> $\det$: [[Determinant of a Matrix]]
-> $J_{g}$: [[Vector-Valued Function#Jacobian|Jacobian]] of $g$

