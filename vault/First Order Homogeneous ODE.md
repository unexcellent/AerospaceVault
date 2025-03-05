#uni/courses/math3 

A first order homogenous ODE is a [[Linear ODE|linear]] [[First Order ODE]] where the remainder $r(x) \equiv 0$.
$$
y' + p(x) \cdot y = 0
$$

# Examples

$$
y' - 14 \sin x \cdot y = 0
$$

# Solution Approach

The following general solution can be applied:
$$
y(x) = C \cdot e^{-\int p(x) \ dx}, \quad \text{with } C \in \mathbb{R}
$$