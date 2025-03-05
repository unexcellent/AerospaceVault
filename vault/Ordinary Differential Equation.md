#uni/courses/math2 #uni/courses/math3 

ODEs are [[Differential Equation|differential equations]] with only one unknown value.

# Classification

An ordinary differential equation $f$ is called

## Implicit

An ordinary differential equation $f$ is called **implicit** if $f \big( x, y(x), y'(x), \dots, y^{(n)}(x)\big) = 0$

## Explicit

An ordinary differential equation $f$ is called **explicit** if $f \big( x, y(x), y'(x), \dots, y^{(n-1)}(x)\big) = y^{(n)}$.

## Autonomous

An ordinary differential equation $f$ is called **autonomous** if it is [[Ordinary Differential Equation#Explicit|explicit]] and $f$ does not depend on $x$.


## Separable

An ordinary differential equation $f$ is called **separable** if
$$
y' = \frac{f(x)}{g(y)}
$$
In that case it can be simplified to
$$
\int g(y) \ dy = \int f(x) \ dx + C
$$

## Exact

An ordinary differential equation is called **exact** if it can be written as
$$
P(x,y) + Q(x,y) \cdot y' = 0 \quad \text{with } \partial_{y}P = \partial_{x}Q
$$

### Solution

Exact ordinary differential equations can be solved by defining a $u(x,y) \in \mathbb{R}$ such that
$$
\partial_{x}u = P \quad \text{and} \quad \partial_{y}u = Q
$$