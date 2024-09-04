#uni/courses/mech1 #uni/courses/materials 

Strain is the the relative deformation of a [[Material|material]] under [[Stress]].

![[Pasted image 20240116101740.png]]
$$
\varepsilon = \frac{du}{dx} = \frac{L-L_{0}}{L_{0}}
$$
-> $u$: deformation of the material along the x-axis
-> $L$: length of the specimen while under strain
-> $L_0$: initial length of the specimen

# Elastic Strain

Strain, which originates from a [[Stress]].
$$
\varepsilon = \frac{\sigma}{E}
$$
-> $\sigma$: [[Stress]]
-> $E$: [[Hookes Law|Young's modulus]]

## Directional Elastic Strain

When a strain is applied in one axis, there is also a strain present in the other axes. The ratio is determined by the [[Poisson Ratio]].

$$
\varepsilon_{x} = \frac{1}{E} \cdot \sigma_{x} - \frac{v}{E} \cdot \sigma_{y} - \frac{v}{E} \cdot \sigma_{z}
$$
$$
\varepsilon_{y} = - \frac{v}{E} \cdot \sigma_{x} + \frac{1}{E} \cdot \sigma_{y} - \frac{v}{E} \cdot \sigma_{z}
$$
$$
\varepsilon_{z} = - \frac{v}{E} \cdot \sigma_{x} - \frac{v}{E} \cdot \sigma_{y} + \frac{1}{E} \cdot \sigma_{z}
$$
-> $v$: [[Poisson Ratio]]
-> $E$: [[Hookes Law|Young's modulus]]
-> $\sigma$: [[Stress]]

# Thermal Strain

Omnidirectional strain caused by [[Temperature]] changes.
$$
\varepsilon_{th} = \alpha \cdot \Delta T
$$
-> $\alpha$: [[Coefficient of Thermal Expansion]]
-> $\Delta T$: temperature difference