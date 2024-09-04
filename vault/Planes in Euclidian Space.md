#uni/courses/math1 

# From 3 Points

$\Pi \subset \mathbb{R}^3$ is a plane if it is the set of those points $x \in \mathbb{R}^{3}$ such that
$$
x = a + \lambda (b-a) + \mu (c-a)
$$
with $\lambda, \mu \in \mathbb{R}$, $a, b, c \in \mathbb{R}^3$ being [[Vector]].

# From a Point and 2 Vectors

$\Pi \subset \mathbb{R}^3$ is a plane from the point $A \in \Pi$ and the vectors $u, v \in \mathbb{R}^3$ with u and v not being parallel
$$
x = a + \lambda u + \mu v
$$
with $\lambda, \mu \in \mathbb{R}$

# From the Normal Form

Give $n \in \mathbb{R}^3$ and consider all $x \in \mathbb{R}^3$ such that.
$$
\langle n, x \rangle = c = \text{constant}
$$
with $c \in \mathbb{R}$.

If $||n|| = 1$, then $\langle n, x \rangle = c$ is the Hesse normal form. In this case $c$ is the length of the projection of the vector $x$ in the direction $n$ which is the distance (if $c \ge 0$) of the plane $\Pi$ from $O$.

## Example

Find the intersection point between the lines
$$
g_{1}: x \in \mathbb{R}^{3}: x = a + \lambda u, \quad a, u \in \mathbb{R}^{3}, \lambda \in \mathbb{R}
$$
$$
g_{2}: y \in \mathbb{R}^{3}: y = b + \mu v, \quad b, v \in \mathbb{R}^{3}, \mu \in \mathbb{R}
$$

We look for $g_{1} \cap g_{2}$ and if $g_{1} \cap g_{2} = \emptyset$ we want to find the distance between $g_1$ and $g_2$

### Case 1: $g_{1} \cap g_{2} \ne \emptyset$ 

In this case $x = y$, $\exists \lambda, \mu: a + \lambda u = b + \mu v$
-> $b-a = \lambda u - \mu v$

### Case 2: $g_{1} \parallel g_{2}$

In this case $u \parallel v \Rightarrow u \times v = 0$
-> $y-x = b + \mu v - (a + \lambda u)$

The minimal distance between $g_1$ and $g_2$: $||y - x||$ when 
$$
y-x \perp u \Leftrightarrow \langle y-x, u \rangle = 0 = \langle b-a, u \rangle + \langle \mu v - \lambda u, u \rangle
$$
since we can consider $u = v$
$$
\mu - \lambda = \frac{\langle a-b, u \rangle}{||u||^2}
$$
$$
y-x = b-a + \frac{\langle a-b, u \rangle}{||u||^{2}} u
$$
distance $g_1$ from $g_2$ = $||y-x||$

### Case 3: Neither parallel nor intersecting

The direction of minimal distance is $\frac{u \times v}{||u \times v||} = n$ with $n \perp u$ and $n \perp v$.

We want $x \in g_{1}$ and $y \in g_{2}$ such that 
$$
||x-y||=d: x-y \perp v \wedge x-y \perp u
$$
$$
x-y = a-b + \lambda u - \mu v
$$


