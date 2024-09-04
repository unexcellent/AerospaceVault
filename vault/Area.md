#uni/courses/math2 

Symbol: $A$

An area $A$ is a subset of [[Euclidean Space|Euclidean space]]

![[Pasted image 20240804112913.png|300]]
All points outside of $A$ are referred to as $A^{C}$.

# Classification

## Open

$A$ is called open if there exists an [[Open Ball]] $B_{\delta}$ for every point $x \in A$ such that $B_\delta(x)$ is part of $A$.
$$
\forall x \in A \quad \exists \delta > 0 : B_{\delta}(x) \subseteq A
$$

## Closed

$A$ is called closed if it is not [[Area#Open|open]].

## Bounded

$A$ is called bounded if there exists an [[Open Ball]] with a radius $M$ centered at $0$, that contains all points of $A$.
$$
\exists M > 0: A \subseteq B_{M}(0) \Leftrightarrow \forall x \in A; ||x|| \le M
$$

## Compact

$A$ is called compact if $A$ is [[Area#Closed|closed]] and [[Area#Bounded|bounded]].

## Connected

$A$ is called connected if any two points in $A$ can be joined by a [[Path|curve]] lying entirely in $A$.