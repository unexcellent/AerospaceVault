#uni/courses/math0 
#uni/courses/math1 

For more complicated applications (e.g. calculation of forces), we require more adequate description of the structure and the elements of the Euclidian space $\mathbb{R}^n, n \in \mathbb{N}$. This leads to the concept of vectors and vector-spaces.

# Informal Definition

Vectors in Euclidian space are objects with prescribed length and direction. An $n$-dimensional vector is typically given in the form of an $n$-tuple.
$$
\begin{align}
    a &= \begin{pmatrix}
           a_{1} \\
           a_{2} \\
           \vdots \\
           a_{n}
         \end{pmatrix}
    , a_i \in \mathbb{R}, i=1, \dots, n
\end{align}
$$
They could also be expressed as 1-dimensional [[Matrix]].

# Vector between Points

Suppose that $A$, $B$ are elements of $\mathbb{R}^n$. Then the vector $\overrightarrow{AB}$ describes how to move from $A$ to $B$:

$$
\begin{align}
    \overrightarrow{AB} &= \begin{pmatrix}
           b_1 - a_{1} \\
           b_2 - a_{2} \\
           \vdots \\
           b_n - a_{n}
         \end{pmatrix}
\end{align}
$$

## Euclidian Length

The distance between the two points is given as the norm of the vector describing the points.

$$
|\overrightarrow{AB}| = \sqrt{(b_1-a_{1)^{2}}+ (b_2-a_{2)^{2}}+ \dots}
$$

# Vector Addition

The sum of two vectors $a, b \in \mathbb{R}^n$ is defined component-wise:
$$
\begin{align}
    a = \begin{pmatrix}
           a_{1} \\
           a_{2} \\
           \vdots \\
           a_{n}
         \end{pmatrix},
    b = \begin{pmatrix}
           b_{1} \\
           b_{2} \\
           \vdots \\
           b_{n}
         \end{pmatrix} \Rightarrow
	a + b = \begin{pmatrix}
           a_{1} + b_{1} \\
           a_{2} + b_{2} \\
           \vdots \\
           a_{n} + b_{n}
         \end{pmatrix}
\end{align}
$$

# Multiplication with a Scalar

The multiplication $a \in \mathbb{R}^n$ with a number $s \in \mathbb{R}$ is defined component-wise:

$$
\begin{align}
    a = \begin{pmatrix}
           a_{1} \\
           a_{2} \\
           \vdots \\
           a_{n}
         \end{pmatrix} \Rightarrow
	a \cdot s = \begin{pmatrix}
           a_{1} \cdot s \\
           a_{2} \cdot s \\
           \vdots \\
           a_{n} \cdot s
         \end{pmatrix}
\end{align}
$$

# Euclidian Scalar Product

The Euclidian scalar product of two $n$-dimensional vectors is defined by:

$$
\begin{align}
    a = \begin{pmatrix}
           a_{1} \\
           a_{2} \\
           \vdots \\
           a_{n}
         \end{pmatrix},
    b = \begin{pmatrix}
           b_{1} \\
           b_{2} \\
           \vdots \\
           b_{n}
         \end{pmatrix} \quad \Rightarrow \quad
	<a, b> = a \cdot b := \sum\limits_{i=1}^n a_i \cdot b_i
\end{align}
$$

## Axioms

$\forall a, b, c \in \mathbb{R}^n, s \in \mathbb{R}$
- $<s \cdot a, b> = s \cdot <a, b>$
- $<a, b> = <b, a>$
- $<a+c, b> = <a, b> + <c, b>$ 
- $<a, a> = ||a||^{2}$
- $<a+b, a+b> = <a, a> + 2<a, b> + <b, b>$
- $<a-b, a-b> = <a, a> - 2<a, b> + <b, b>$
- $<a+b, a-b> = <a, a> - <b, b>$

# Norm of a Vector (Length)

Formula is derived by the [[Theorem of Pythagoras]].

$$
\begin{align}
    a = \begin{pmatrix}
           a_{1} \\
           a_{2} \\
           \vdots \\
           a_{n}
         \end{pmatrix} \Rightarrow
    ||a|| = \sqrt{\sum\limits_{i=1}^n a_i^2}
\end{align}
$$

## Axioms

For all vectors $v, w \in \mathbb{R}^n$ we have:
- $||v + w|| = ||v^2|| + 2 <v, w> + ||v^2||$
- $||v - w|| = ||v^2|| - 2 <v, w> + ||w^2||$
- $||v||^2 + ||w||^2 = <v-w, v+w>$
- $||\alpha \cdot v|| = |\alpha| \cdot ||v||, \forall \alpha \in \mathbb{R}$
- $||v + w|| \le ||v|| + ||w||$ (triangular [[Inequalities|inequality]])

# Orthogonality

Two vectors $a, b \in \mathbb{R}^n$ are called orthogonal (in symbols ($a \perp b$) if $<a, b> = 0$. This means they have a 90° angle between them.

## Orthogonal Decomposition / Projection

Given $a \in \mathbb{R}^n, b \in \mathbb{R}^n\backslash \{0\}$, the orthogonal decomposition of $a$ w.r.t $b$ is given by

$$
a^{\perp} = a - \frac{<a, b>}{||b||^2}, \hspace{10pt} a^{||} = \frac{<a, b>}{||b||^2}b
$$

![[Vectors 2023-10-28 21.01.35.excalidraw]]

# Angles between Vectors

Consider the angle between arbitrary vectors. 
$$
\forall a, b \in \mathbb{R}^n\backslash \{0\}: \cos(\rho_{a, b}) = \frac{\langle a, b \rangle}{||a|| \cdot ||b||}
$$

# [[Inequalities]]

- Caucky-Schwarz inequality: $\forall a, b \in \mathbb{R}^{n}: |\langle a, b \rangle| \le ||a|| \cdot ||b||$
- Triangle Inequality: $\forall a, b \in \mathbb{R}^n: ||a + b|| \le ||a|| + ||b||$