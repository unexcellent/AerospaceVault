#uni/courses/math1 

Given the [[Vector|vectors]] $v_1, v_{2}, \dots, v_{m} \in V$ with $V$ being a [[Vector Space|vector space]]. We say that:
$$
x = \sum\limits_{j=1}^{m} \alpha_{j} v_{j} = \alpha_{1} v_{1} + \alpha_{2} v_{2} + \dots + \alpha_{m} v_{m}
$$
is a linear combination of $v_1, v_{2}, \dots, v_{m}$ with coefficients $\alpha_1, \alpha_{2}, \dots, \alpha_{m}$.
$$
\text{span}(v_1, v_{2}, \dots, v_{m}) := \{\sum\limits_{j=1}^{m} \alpha_{j} v_{j}: \alpha_{j} \in \mathbb{R}\}
$$
This is a sub vector space (SVS) of $V$.

# Zero Dimensional

Given $m=1, v_{1}=0$
$$
\text{span}(v_{1}) = \text{span}(0) = \{\alpha v_{1}: \alpha \in \mathbb{R}\} = \{0\}
$$

# One Dimensional

Given $m=1, v_{1} \neq 0$
$$
\text{span}(v_{1}) = \{\alpha v_{1}: \alpha \in \mathbb{R}\} \quad \Rightarrow \quad \alpha_{1} v_{1} = x \in \text{span}(v_{1})
$$

Then $\text{span}(v_{1})$ defines a [[Straight Lines in Euclidian Space|line]] through the origin in the direction of $v_{1}$.

# Two Dimensional

Given $m=2, \quad v_{1}, v_{2} \neq 0$
$$
\text{span}(v_{1}) = \{\alpha_{1} v_{1} + \alpha_{2} v_{2}: \alpha_{1}, \alpha_{2} \in \mathbb{R}\} 
$$
$$
\Rightarrow \alpha_{1} v_{1} + \alpha_{2} v_{2} = x \in \text{span}(v_{1}, v_{2})
$$
Then $\text{span}(v_{1}, v_{2})$ defines a [[Planes in Euclidian Space|plane]] through the origin in the direction of $v_{1}$ and $v_{2}$.

# Linear Independence

If the vector space in not [[Linear Independence of Vectors|linearly independent]] it can be reduced, until it is.