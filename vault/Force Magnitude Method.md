#uni/courses/mech1 #uni/courses/mech2 

Method for calculating the [[Force|forces]] in [[Static Determinacy|statically indeterminate]] systems.

# One-Fold Statically Indeterminate Trusses

Given a statically indeterminate system
![[Force Magnitude Method 2024-07-03 16.35.56.excalidraw|300]]

Two systems need to be created, that are each statically determinate.

The 0-System should have an element removed and contain all external forces.
![[Force Magnitude Method 2024-07-03 16.41.24.excalidraw|300]]

The 1-System should have all external forces removed and a force of magnitude 1 replacing the removed element.
![[Force Magnitude Method 2024-07-03 16.45.42.excalidraw|300]]

The all truss forces in each system should then be calculated.

With these partial forces, the influence numbers can then be calculated as
$$
\delta_{10} = \sum_{k} \frac{S^{(0)}_{k} \cdot S^{(1)}_{k} \cdot l_{k}}{E_{k} \cdot A_{k}}
$$
$$
\delta_{11} = \sum_{k} \frac{S^{(1)}_{k} \cdot S^{(1)}_{k} \cdot l_{k}}{E_{k} \cdot A_{k}}
$$
-> $S^{(0)}_{k}$: force of truss $k$ in the 0-System
-> $S^{(1)}_{k}$: force of truss $k$ in the 1-System
-> $l_{k}$: length of truss $k$
-> $E_{k}$: [[Modulus of Elasticity]] of truss $k$
-> $A_{k}$: cross-sectional area of truss $k$

With the influence numbers, the truss force of the removed truss $X$ can then be calculated via
$$
X = -\frac{\delta_{10}}{\delta_{11}}
$$

With $X$ now known, the system is statically determinate.