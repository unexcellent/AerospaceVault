#uni/courses/fluid1 

The time rate of change of total linear momentum of a [[Fluid]] volume equals the sum of all [[Force|forces]] acting on it.
$$
\frac{d \underline{P}}{dt} = \frac{d}{dt} \int_{\tilde{V}} \rho \cdot \underline{u} \ dV = \sum_{i} F_{i}
$$
-> $P$: [[Momentum]]
-> $t$: time
-> $V$: [[Volume]]
-> $\rho$: [[Density]]
-> $u$: [[Velocity]]
-> $F$: [[Force]]

The full conservation equation reads
$$
\int_{V} \frac{\partial (\rho \underline{u})}{\partial t} dV
+ \int_{S} \rho \cdot \underline{u} \cdot \langle \underline{u}, \underline{n} \rangle \ dS
= - \int_{S} p \cdot \underline{n} \ dS
+ \int_{S} \langle \underline{\underline{\tau}}, \underline{n} \rangle \ dS
+ \int_{F} \rho \cdot \underline{f} \ dV
+ \underline{F}
$$
-> $t$: time
-> $V$: [[Volume]]
-> $\rho$: [[Density]]
-> $u$: [[Velocity]]
-> $F$: [[Force]]
-> $S$: surface
-> $n$: normal vector
-> $p$: [[Pressure]]
-> $\tau$: [[Stress#Tensor Representation|stress tensor]]