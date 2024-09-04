#uni/courses/math1 

# From two Points

Given two points $A$ and $B$ with the [[Vector|vectors]] from the origin $a$ and $b$ in $\mathbb{R}^3$, a line $g$ between them is defined by:
$$
\overrightarrow{OP} = x = a + \lambda (b-a), \quad \lambda \in \mathbb{R}
$$

with $P$ being a point on the line dependent on $\lambda$.

![[Three Dimensional Straight Lines 2023-10-27 13.46.35.excalidraw]]

# From one Point and one Direction

Given a point $A$ with the vector from the origin $a$ and a direction vector $u$, a line is defined by:

$$
\overrightarrow{OP} = x = a + \lambda \cdot u, \quad \lambda \in \mathbb{R}
$$

![[Three Dimensional Straight Lines 2023-10-27 13.49.55.excalidraw]]

# From the Normal Form

In $\mathbb{R}^2$ there is another form of defining a line by introducing the normal vector $n$, which is orthogonal to $u$:
$$
\frac{\langle x, n \rangle}{||n||} = \text{const.}
$$

![[Pasted image 20231029193846.png]]

The Hesse normal form is defined as:
$$
\langle x, n \rangle = c
$$

with
$$
d := \langle n, x_{0} \rangle - c = \begin{cases}
> 0\quad x_{0} \text{ and } 0 \text{ are on opposite sides with respect to } g \\
= 0 \quad x_{0} \in g \\
< 0 \quad x_{0} \text{ and } 0 \text{ are on the same side with respect to } g \\
\end{cases}
$$

given $x_{0} \in \mathbb{R}$.

# Distance between Two 3D Lines

Given two lines $x_{1} = p_{1} + \lambda v_{1}$ and $x_{2} = p_{2} + \lambda v_{2}$ the distance between them can be computed via:
$$
d = \left| \dfrac{\langle p_{1} \times p_{2}, v_{1} \times v_{2} \rangle}{||v_{1} \times v_{2}||} \right|
$$
-> $\times$: [[Cross-Product of Vectors]]
-> $\langle \cdots \rangle$: [[Vector#Euclidian Scalar Product]]
-> $||\cdots||$: [[Vector#Euclidian Length]]

If the lines are parallel, then $p_{1} \times p_{2}$ results in the zero vector, which breaks the equation.