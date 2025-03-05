#uni/courses/math3 

A second order homogenous ODE is a [[Linear ODE|linear]] [[Second Order ODE]] where the remainder $r(x) \equiv 0$.
$$
y'' + p(x) \cdot y' + q(x) \cdot y = 0
$$

# Solution Approach

The ODE can be solved with the characteristic equation
$$
\lambda^{2} + p \cdot \lambda + q = 0
$$
This can then be solved using the $pq$-method
$$
\lambda_{1 / 2} = - \frac{p}{2} \pm \sqrt{\left( \dfrac{p}{2} \right)^{2} - q} = \alpha \pm \sqrt{\Delta}
$$

If $\Delta \ge 0$
$$
y = C_{1} \cdot e^{\lambda_{1}} + C_{2} \cdot x \cdot e^{\lambda_{2}}, \quad \text{with } C_{1}, C_{2} \in \mathbb{R}
$$
if $\Delta < 0$ ($\lambda_{1 / 2} = \alpha \pm \beta i$)
$$
y = e^{\alpha x}(C_{1} \cos \beta x + C_{2} \sin \beta x)
$$