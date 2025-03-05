#uni/courses/math3 

An [[Ordinary Differential Equation]] is called a **Bernoulli differential equation** if it is of the form
$$
y' + p(x) \cdot y = r(x) \cdot y^{n}, \quad n \in \mathbb{R}
$$

# Solution

First, the equation is divided by $y^{n}$
$$
y^{-n} \cdot y' + p(x) \cdot y^{1-n} = r(x)
$$
Now we define $v = y^{1-n}$ with the derivative
$$
v' = (1-n)\cdot y^{-n} \cdot y'
$$
When we plug this into the equation above we get
$$
\frac{1}{1-n} v' + p(x) \cdot v = r(x)
$$
or differently
$$
v' + (1-n) \cdot p(x) \cdot v = (1-n) \cdot r(x)
$$
which can then be solved as a [[First Order Inhomogenous ODE]].

