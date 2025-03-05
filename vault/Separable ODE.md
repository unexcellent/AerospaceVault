#uni/courses/math3 

A separable ODE is an [[Ordinary Differential Equation]] which can be expressed by
$$
y' = f(x) \cdot g(y)
$$

# Examples

$$
y' = 4x \cdot y^{2}, \quad y'' = y \cdot \sin 2x
$$

# Solution Approach

Take the ODE 
$$y' = 4y^{2}$$
It can also be written as
$$
\frac{dy}{dx} = 4y^{2}
$$
Switching the $dx$ and $y^{2}$ gives
$$
\frac{dy}{y^{2}} = 4 \ dx
$$
Applying an integral gives the solution as
$$
\int \frac{dy}{y^{2}} = \int 4 \ dx 
\quad \Rightarrow \quad 
-\frac{1}{y} = 4x + C
\quad \Rightarrow \quad 
y = \frac{1}{-4x - C}
$$