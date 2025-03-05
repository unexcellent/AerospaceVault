#uni/courses/math3 

A first order inhomogenous ODE is a [[Linear ODE|linear]] [[First Order ODE]] where the remainder $r(x) \not\equiv 0$.
$$
y' + p(x) \cdot y = r(x)
$$

# Examples

$$
y' - 14 \sin x \cdot y = \cos x
$$

# Solution Approach

The solution relies on the fact that
$$
y = y_{p} + y_{h}
$$
with $y_{h}$ being the solution to the [[First Order Homogeneous ODE]] and $y_{p}$ being called the particular solution.

$y_{p}$ can be determined using the variation of constants approach with
$$
y_{p}(x) = c(x) \cdot e^{-\int p(x) \ dx}
$$
using
$$
c'(x) = e^{\int p(x) \ dx} \cdot r(x).
$$

The general solution is therefore
$$
y = e^{-\int p(x) \ dx} \cdot \left( \int r(x) \cdot e^{\int p(x) \ dx} \ dx + C\right)
$$
