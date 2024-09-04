#uni/courses/mech2 

# Cuboid

Given a cuboid
![[Bending 2024-06-17 19.02.35.excalidraw|600]]
with $x_{tot} >> y_{tot}, z_{tot}$.

The [[Stress]] at each point of the cuboid is given by
$$
\sigma(x,y,z) = 
\underbrace{\frac{N(x)}{y_{tot} \cdot z_{tot}}}_\text{Normal Stress}
+ \underbrace{\frac{M_{y}(x)}{I_{zz}} \cdot z}_\text{Bending around $y$}
- \underbrace{\frac{M_{z}(x)}{I_{yy}} \cdot y}_\text{Bending around $z$}
$$
-> $N$: [[Stress Resultants#Normal Forces|normal force]]
-> $M_{y}$: [[Torsional Moment]] around $y$-axis
-> $M_{z}$: [[Torsional Moment]] around $z$-axis
-> $I_{zz}$: [[Moment of Inertia]] around $z$-axis
-> $I_{yy}$: [[Moment of Inertia]] around $y$-axis

![[Pasted image 20240617192510.png]]

