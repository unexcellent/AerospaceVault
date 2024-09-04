#uni/courses/math2 

A real or complex [[Vector Space]] $\mathcal{H}$ is called a Hilbert space $(\mathcal{H}, \langle \cdot, \cdot \rangle)$ if
- it has an [[Vector#Euclidian Scalar Product|inner product]] $\langle \cdot, \cdot \rangle$
- it is complete (i.e. every [[Sequence of Numbers#Cauchy Sequence|Cauchy sequence]] converges to an element of $\mathcal{H}$)

It is called a pre-Hilbert space if only the first condition is true.

# Properties

- every pre-Hilbert space is a normed space with norm $||v|| := \sqrt{\langle v, v \rangle}, \ \ v \in \mathcal{H}$
- every Hilbert space is a [[Banach Space]]
- two elements of a Hilbert space $x, y \in \mathcal{H}$ are said to be **orthogonal** if $\langle x, y \rangle = 0$
- the angle between two functions $f$ and $g$ can be calculated as $\cos \theta = \dfrac{\langle f, g \rangle}{\sqrt{\langle f, f \rangle} \cdot \sqrt{\langle g, g \rangle}}$

# [[Inequalities]]

## Bessel's Inequalilty

Let $\mathcal{H}$ be a Hilbert space and $(e_{j})_{j \in I}$ an orthonormal system, then
$$
\forall x \in \mathcal{H}: \quad ||x||^{2} \ge \sum_{j \in I} |\langle x, e_{j} \rangle|^{2}
$$

## Parseval's Identity

Let $\mathcal{H}$ be a Hilbert space and $(e_{j})_{j \in I}$ a complete orthonormal system, then
$$
\forall x \in \mathcal{H}: \quad ||x||^{2} = \sum_{j \in I} |\langle x, e_{j} \rangle|^{2}
$$