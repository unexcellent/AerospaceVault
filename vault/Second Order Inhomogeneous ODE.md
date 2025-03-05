#uni/courses/math3 

A second order inhomogenous ODE is a [[Linear ODE|linear]] [[Second Order ODE]] where the remainder $r(x) \not\equiv 0$.
$$
y'' + p(x) \cdot y' + q(x) \cdot y = r(x)
$$

# Solution Approach

The solution relies on the fact that
$$
y = y_{p} + y_{h}
$$
with $y_{h}$ being the solution to the [[Second Order Homogeneous ODE]] and $y_{p}$ being called the particular solution.

Multiple methods exist for determining $y_{p}$.

## Variation of Constants

First take the two summands of $y_{h}$ as $y_{h1}$ and $y_{h2}$ and create the [[Wronski Determinant]].
$$
W = y_{h1} \cdot y'_{2} - y_{h2} \cdot y'_{h1}
$$
Then calculate the two functions $u'_{1}$ and $u'_{2}$ as
$$
u'_{1} = - \frac{y_{2} \cdot r(x)}{W}, \quad u'_{2} = \frac{y_{1} \cdot r(x)}{W}
$$
$u_{1}$ and $u_{2}$ can be determined via integration.
The particular solution is then
$$
y_{p} = u_{1} \cdot y_{1} + u_{2} \cdot y_{2}
$$

## Method of Undetermined Coefficients

The method of undetermined coefficients can be straight forward, but is not applicable in every case. That depends on the remainder function $r(x)$

| remainder                                                                             | the guess                                                        |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| $a \cdot e^{\beta x}$                                                                 | $a \cdot e^{\beta x}$                                            |
| $a \cdot \sin (\beta x) + b \cdot \cos (\beta x)$                                     | $A \cdot \cos (\beta x) + B \cdot \sin (\beta x)$                |
| $a \cdot \sinh (\beta x) + b \cdot \cosh (\beta x)$                                   | $A \cdot \cosh (\beta x) + B \cdot \sinh (\beta x)$              |
| [[Polynomial and Rational Functions\|polynomial]] of degree $n$                       | $A_{n} x^{n} + A_{n-1} x^{n-1} + \dots + A_{1}x + A_{0}$         |
| $a \cdot e^{\alpha x} \cdot \sin(\beta x) + b \cdot e^{\alpha x} \cdot \cos(\beta x)$ | $e^{\alpha x} (A \cdot \cos (\beta x) + B \cdot \sin (\beta x))$ |

$y_{p}$ is then set equal to the guess and then inserted into the equation (with multiple derivatives). The coefficients are then calculated with the remainder.
