#uni/courses/mech1 

In a static system, there can be no displacement and therefore no [[Mechanical Work|work]]. However, it is still useful for solving systems quickly.
Virtual work and virtual displacements are prefixed by a $\delta$.

For translation:
$$
\delta W = \overrightarrow{F} \cdot \delta \overrightarrow{u}
$$

For rotation:
$$
\delta W = F \cdot \delta \varphi \cdot r
$$
Line loads should be reduced into their resultant [[Force|force]].

# Solving Systems

![[Pasted image 20231214141701.png]]

A static system must first be changed to allow for movement.

![[Pasted image 20231214141813.png]]

The virtual work is then the sum of all contributing forces with their distance.
$$
\delta W = A_{H} \cdot \delta u - F \cdot \delta u
$$
Since the equilibrium condition still holds, the conducted work must be zero:
$$
\delta u \cdot( A_{H} - F) = 0 \qquad \forall \delta u \in \mathbb{R}
$$
This must hold true for all possible $\delta u$, which results in:
$$
A_{H} - F = 0 \quad \Rightarrow \quad A_{H} = F
$$
