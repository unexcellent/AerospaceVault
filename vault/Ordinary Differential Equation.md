#uni/courses/math2 

Ordinary differential equations are a type of equation, that contain one or more unknown [[Function|function]] and its [[Derivative|derivatives]].

$F \big( x, y(x), y'(x), \dots, y^{(n)}(x)\big)$ is a differential equation of order $n$.

# Classification

An ordinary differential equation $f$ is called

## Implicit

An ordinary differential equation $f$ is called **implicit** if $f \big( x, y(x), y'(x), \dots, y^{(n)}(x)\big) = 0$

## Explicit

An ordinary differential equation $f$ is called **explicit** if $f \big( x, y(x), y'(x), \dots, y^{(n-1)}(x)\big) = y^{(n)}$.

## Autonomous

An ordinary differential equation $f$ is called **autonomous** if it is [[Ordinary Differential Equation#Explicit|explicit]] and $f$ does not depend on $x$.

## Linear

An ordinary differential equation $f$ is called **linear** if it is [[Ordinary Differential Equation#Explicit|explicit]] and 
$$
y^{(n)} = \sum^{n-1}_{j=0} a_{j}(x) \cdot y^{(j)} + b(x)
$$
They can be solved by first only considering the homogeneous part as
$$
y_{\text{hom}}' + g(x) \cdot y_{\text{hom}} = 0
$$
with the solution
$$
y_{\text{hom}}(x) = C_{1} \cdot e^{- \int g(x) \ dx} \quad \text{with } C_{1} \in \mathbb{R}
$$
And then considering the inhomogeneous part
$$
Ly = h(x)
$$
where the function then computes to
$$
y_{p} = e^{- \int g(x) \ dx} \cdot \int h(x) \cdot e^{- \int g(x) \ dx} \ dx
$$
The solution is then
$$
y(x) = y_{p}(x) + y_\text{hom}(x)
$$

## Homogeneous

An ordinary differential equation $f$ is called **homogeneous** if it is [[Ordinary Differential Equation#Linear|linear]] and $b(x) = 0$.

They are of the form
$$
Q(x,y) \cdot y' = P(x,y)
$$
then
$$
\int \frac{Q(1,v)}{P(1,v) - v \cdot Q(1,v)} dv = \ln|x| + C
$$
with
$$
v = \frac{y}{x}
$$

## Inhomogeneous

An ordinary differential equation $f$ is called **inhomogeneous** if it is [[Ordinary Differential Equation#Linear|linear]] and $b(x) \neq 0$.

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