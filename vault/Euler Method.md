#uni/courses/math3 

Euler's method is the most basic [[Runge-Kutta Method]] used to approximate [[Initial Value Problem|initial value problems]].

Given an ODE $y' = f(t, y(t))$ and $y(t_{0}) = y_{0}$ the method uses a step size $h \in \mathbb{R}$ to approximate the function at different points with
$$
y_{n+1} = y_{n} + h \cdot y'(t_{n})
$$
and
$$
t_{n+1} = t_{n} + h
$$
The $y'$ can then be approximated using
$$
y'(t_{n}) = \frac{y(t_{n+1}) - y(t_{n})}{t_{n+1} - t_{n}}
$$

![[Pasted image 20250214143610.png|600]]

The smaller the step size $h$ is, the more accurate the method approximates the equation but the higher is the computational workload.
