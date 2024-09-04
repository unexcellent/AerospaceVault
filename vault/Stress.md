#uni/courses/mech1 #uni/courses/mech2 #uni/courses/materials 

Symbol: $\sigma$
Unit: $Pa = \frac{N}{m^{2}}$

Stress is a measure of the internal forces a [[Material]] is subjected to.

![[Pasted image 20240113125540.png]]
$$
\sigma \cdot \overrightarrow{n} := \frac{dF}{dA} = \frac{F}{A} = \varepsilon \cdot E
$$
-> $\overrightarrow{n}$: normal direction of the cut
-> $F$: [[Force]]
-> $A$: Cross-sectional area
-> $\varepsilon$: [[Strain]]
-> $E$: [[Hookes Law|Young's modulus]]

![[Pasted image 20240113130928.png]]
$$
\sigma_{y} = \frac{dF_{y}}{dA_{y}}
$$
$$
\tau_{yx} = \frac{dF_{x}}{dA_{y}}
$$
$$
\tau_{yz} = \frac{dF_{z}}{dA_{y}}
$$
-> $F_{x}$: [[Force]] component in the $x$-direction
-> $A_{y}$: Cross-sectional area orthogonal to the $y$-direction
-> $\sigma$: normal stress
-> $\tau_{yx}$: shear stress in the $x$-direction of an area orthogonal to the $y$-direction

There are a total of 3 stresses per coordinate system axis.

# Tensor Representation


$$
\sigma = [\sigma_{ij}] = \begin{pmatrix}
\sigma_{xx} & \tau_{xy} & \tau_{xz} \\ 
\tau_{yx} & \sigma_{yy} & \tau_{yz} \\ 
\tau_{zx} & \tau_{zy} & \sigma_{zz}
\end{pmatrix} \left[\frac{N}{m^{2}}\right]
$$

 with $\tau_{xy} = \tau_{yx}$, $\tau_{xz} = \tau_{zx}$ and $\tau_{yz} = \tau_{zy}$ since the [[Tensor]] is [[Matrix#Symmetric Matrices|symmetric]].

# Changes in Position

For a point $P(𝑥, 𝑦, 𝓏)$ the stress state $σ_{ij}(𝑥, 𝑦, 𝓏)$ is considered

For the infinitesimal adjacent point $P’(𝑥 + 𝑑𝑥, 𝑦 + 𝑑𝑦, 𝓏 + 𝑑𝓏)$ it holds:
$$
\sigma_{ij}(x+dx,y+dy,z+dz) = \sigma_{ij} + \dfrac{\partial \sigma_{ij}(x,y,z)}{\partial x} dx + \dfrac{\partial \sigma_{ij}(x,y,z)}{\partial y} dy + \dfrac{\partial \sigma_{ij}(x,y,z)}{\partial z} dz
$$

# Bending Stress

When a [[Mechanical Beams|beam]] is subjected to [[Stress Resultants#Shear Forces|shear forces]] or bending [[Moment|moments]], a stress is created.
$$
\sigma(x,y,z) = \frac{N(x)}{A} + \frac{M_{y} \cdot z}{I_{yy}} - \frac{M_{z} \cdot y}{I_{zz}}
$$
-> $x$,$y$,$z$: coordinates
-> $N$: [[Stress Resultants#Normal Forces|normal force]]
-> $A$: cross-sectional area
-> $M$: [[Moment]]
-> $I$: [[Moment of Inertia]]

The maximum stress is always in the [[Centroid]] line of the beam.