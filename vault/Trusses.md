#uni/courses/mech1 

[[Mechanical Supports|Supporting Structures]] consisting of (straight) bars connected to each other in nodes.
![[Pasted image 20231102093437.png]]

Ideal trusses are based on idealizing assumptions:
- The bar axes (geom. location of the gravity axis) are always straight
- Bar axes intersect at one point (node) each
- Pins connect bars with frictionless joints
- External forces act only on nodes

-> only tensile and compressive forces act, no moment effect

# Convention on Bar Forces

![[Trusses 2023-11-02 09.38.09.excalidraw]]

Tensile Forces: positive bar force
Compressive Forces: negative bar forces

# Equilibrium Conditions for Cut out Nodes

- $\sum F_{x} = 0$
- $\sum F_{y} = 0$
- $\sum M = 0$

With $n$ nodes, $b$ bars and $s$ support reactions, the [[Static Determinacy#Counting Criterion|counting criterion]] is fulfilled in 2D via:
$$
s + b = 2n
$$