#uni/courses/mech1

When [[External Work]] is applied to an elastic body, it deforms according to the [[Strain Energy]].

![[Pasted image 20240211132008.png|400]]

Do the linearity principle, the displacement of different [[Force|forces]] can be simply added.
$$
\overrightarrow{u}_{0} = \sum_{i=1}^{n} \overrightarrow{u}_{i} 
$$
**Note**: the resulting displacement $\overrightarrow{u}_{0i}$ of force $\overrightarrow{F}_{i}$ may not be in the direction of $\overrightarrow{F}_{i}$.

The resulting displacement of the forces can be calculated using a force effect $\overrightarrow{f}_{i}$ parallel to the external force.

![[Pasted image 20240211133627.png|350]]
$$
f_{ii} = \delta_{ii} \cdot F_{i}
$$
-> $\delta_{ii}$: influence number describing location and direction of force

# Total Work on the System

$$
\Pi = \frac{1}{2} \cdot \sum^{n}_{i=1} \sum^{n}_{k=1} F_{i} \cdot \delta_{ik} \cdot F_{k}
$$
-> $\Pi$: Deformation work
-> $F_{i}$: force with index $i$
-> $\delta_{ik}$: influence number describing effect of force $k$ on point $i$

with
$$
\delta_{ik} = \delta_{ki}
$$