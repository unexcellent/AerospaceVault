#uni/courses/math2 

Given a [[Sequence of Numbers|numerical sequence]] $a_{k}$ and point of expansion $x_{0} \in \mathbb{R}$, the power series is defined as
$$
\sum^{\infty}_{k=0} a_{k} \cdot (x - x_{0})^{k}
$$
or if $x_{0}=0$
$$
\sum^{\infty}_{k=0} a_{k} \cdot y^{k}
$$
# Convergence

The power series always converges for $x = x_{0}$ / $y = 0$.

If it converges for an $x_{1} \in \mathbb{R}$, then it converges $\forall x : 0 \le |x| < |x_{1}|$.

## Radius of Convergence

The radius of converges $r$ describes the maximum number of $|x_{1}|$ where all $x$ smaller than $x_{1}$ converge.

From [[Root Test]], we can deduct that if $L := \displaystyle \lim_{k \to \infty} \sqrt[k]{|a_{k}|}$ exists, then
$$
r = \begin{cases}
\infty \quad \text{if } L = 0 \\
\frac{1}{L} \quad \text{if } 0 < L < \infty \\
0 \quad \text{if } L = \infty \\
\end{cases}
$$

From [[D'Alembert Criterion]], we can deduct, that if $L := \displaystyle \lim_{k \to \infty} \left| \frac{a_{k} + 1}{a_{k}} \right|$ exists, then
$$
r = \begin{cases}
\infty \quad \text{if } L = 0 \\
\frac{1}{L} \quad \text{if } 0 < L < \infty \\
0 \quad \text{if } L = \infty \\
\end{cases}
$$

# Real-Analytic Functions

The power series can also be used to define [[Series of Functions]]
$$
f(x) = \sum^{\infty}_{k=0} a_{k} \cdot x^{k}
$$
with
$$
f'(x) = \sum^{\infty}_{k=1} a_{k} \cdot k \cdot x^{k-1}
$$

A function $f: (-r, r) \to \mathbb{R}$ with radius of convergence $r > 0$ is called **real-analytic** on $(-r, r)$ if
- $f \in C^{\infty}(-r,r)$ and
- the power series$$
\sum^{\infty}_{k=0} \frac{f^{(k)}(x_{0})}{k!} (x-x_{0})^{k}$$ converges pointwise to $f \ \forall x \in (x_{0} - \delta, \ x + \delta), \ \delta > 0$ (see [[Taylor Series]])

## Remainder

A necessary and sufficient condition for a function $f$ to be real-analytic is that the remainder $R_{n}(x)$ approaches $0$.
$$
\lim_{n \to \infty} R_{n}(x) = \lim_{n \to \infty} \left( f(x) - \sum^{n}_{k=0} \frac{f^{(k)}(0)}{k!} x^{k} \right) = 0
$$

## List of Real-Analytic Functions

| Function             | [[Taylor Series]]                                                                 | Radius of convergence |
| -------------------- | --------------------------------------------------------------------------------- | --------------------- |
| $e^x$                | $\displaystyle \sum^{\infty}_{k=0} \dfrac{x^{k}}{k!}$                             | $r=\infty$            |
| $\sin x$             | $\displaystyle \sum^{\infty}_{k=0} (-1)^{k} \dfrac{x^{2k+1}}{(2k+1)!}$            | $r=\infty$            |
| $\cos x$             | $\displaystyle \sum^{\infty}_{k=0} (-1)^{k} \dfrac{x^{2k}}{(2k)!}$                | $r=\infty$            |
| $\dfrac{1}{1-x}$     | $\displaystyle \sum^{\infty}_{k=0} x^{k}$                                         | $r=1$                 |
| $\dfrac{1}{1+x^{2}}$ | $\displaystyle \sum^{\infty}_{k=0} (-1)^{k} \cdot x^{2k}$                         | $r=1$                 |
| $\arctan x$          | $\displaystyle \sum^{\infty}_{k=0} (-1)^{k} \dfrac{x^{2k+1}}{2k+1}$               | $r=1$                 |
| $(1 + x)^{\alpha}$   | $\displaystyle \sum^{\infty}_{k=0} \dfrac{\alpha!}{(\alpha - k)! \cdot k!} x^{k}$ | $r=1$                 |
