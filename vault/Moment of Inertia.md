#uni/courses/mech2 

Symbol: $I$
Unit: $m^{4}$

A quantity, that determines the [[Torque]] needed for a desired [[Angular Acceleration]].
Rotational equivalent to [[Mass]].
$$
I_{yy} = \int_{\Omega} z^{2} \ dA + \underbrace{z_{G}^{2} \cdot A}_\text{Steiner}
$$
$$
I_{zz} = \int_{\Omega} y^{2} \ dA + \underbrace{y_{G}^{2} \cdot A}_\text{Steiner}
$$
$$
I_{zy} = I_{yz} =\int_{\Omega} y \cdot z \ dA - \underbrace{y_{G} \cdot z_{G} \cdot A}_\text{Steiner}
$$
-> $I_{yy}$,$I_{zz}$: moments of inertia
-> $I_{yz}$,$I_{zy}$: deviation moments
-> $\Omega$: plane surface
-> $y$,$z$: coordinates of an arbitrary point with respect to the (reference) coordinate system
-> $y_{G}$,$z_{G}$: [[Centroid]] coordinates in the reference system
-> $A$: area

# [[Tensor]] Representation

$$
I = \begin{pmatrix}
I_{yy} & I_{yz} \\ 
I_{zy} & I_{zz}
\end{pmatrix}
$$

# Inertial Extrema

The minimum/maximum moment of inertia can be calculated via
$$
I_{\text{max}/\text{min}} = \frac{I_{yy} + I_{zz}}{2} \pm \sqrt{\left( \frac{I_{yy} - I_{zz}}{2} \right)^{2} + I_{yz}^{2}}
$$

# Simple Shapes

## Rectangle

![[Moment of Inertia 2024-06-17 19.20.24.excalidraw]]
$$
I_{yy} = \frac{y_{tot} \cdot z_{tot}^{3}}{12}
$$
$$
I_{zz} = \frac{z_{tot} \cdot y_{tot}^{3}}{12}
$$
$$
I_{yz} = 0
$$

## Right-Triangle

![[Moment of Inertia 2024-07-07 11.03.09.excalidraw]]
$$
I_{yy} = \frac{y_{tot} \cdot z_{tot}^{3}}{36}
$$
$$
I_{zz} = \frac{y_{tot}^{3} \cdot z_{tot}}{36}
$$
$$
I_{yz} = \frac{y_{tot}^{2} \cdot z_{tot}^{2}}{72}
$$

## Circle

![[Moment of Inertia 2024-07-13 17.37.09.excalidraw|200]]
$$
I_{yy} = I_{zz} = \frac{\pi \cdot r^{4}}{4}
$$
$$
I_{yz} = 0
$$

## Half-Circle

![[Moment of Inertia 2024-07-07 11.10.03.excalidraw]]
$$
I_{yy} = 0.1098 \cdot r^{4}
$$
$$
I_{zz} = \frac{\pi \cdot r^{4}}{8}
$$
$$
I_{yz} = 0
$$