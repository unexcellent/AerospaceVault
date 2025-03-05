#uni/courses/math3 

The Runge-Kutta methods are a family of [[Numerical Method for ODEs|numerical ODE approximation methods]].

The general form is defined for $y' = f(t,y)$ as
$$
y_{n+1} = y_{n} + \Delta t \cdot \sum_{j=1}^{s} b_{j} \cdot k_{j}
$$
with
$$
k_{j} = f(t_{n} + c_{j} \cdot \Delta t,\ \ y_{n} + \Delta t \sum_{l=1}^{s} a_{jl} \cdot k_{l})
$$
-> $a_{jl}$,$b_{j}$,$c_{j}$: parameters
-> $s$: number of auxiliary steps

# Order of Convergence

The order of convergence of a Runge-Kutta method can be calculated using the [[Butcher Tableau]].

- the method has an order of $1$ if $\sum_{i=1}^{s} b_{i} = 1$
- the method has an order of $2$ if $\sum_{i=1}^{s} b_{i} \cdot c_{i} = \frac{1}{2}$
- the method has an order of $3$ if $\sum_{i=1}^{s} b_{i} \cdot c_{i}^{2} = \frac{1}{3}$ and $\sum_{i=1}^{s} b_{i} \cdot \left( \sum_{j=1}^{s} a_{ij} \cdot c_{j} \right) = \frac{1}{6}$