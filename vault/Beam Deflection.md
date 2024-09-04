#uni/courses/mech2 

If a [[Torsional Moment|bending moment]] is applied to a [[Mechanical Beams|beam]], it is bend along a deflection curve.
![[Pasted image 20240713125809.png]]

In a [[Principal Axis System]] the curve equates to
$$
w_{y}''(x) = \phi_{y}'(x) = \frac{M_{z}(x)}{E \cdot I_{zz}}
$$
$$
w_{z}''(x) = -\phi_{z}'(x) = \frac{M_{y}(x)}{E \cdot I_{yy}}
$$
-> $w$: deflection curve
-> $\phi$: [[Twist Angle]]
-> $M$: [[Torsional Moment]]
-> $E$: [[Modulus of Elasticity]]
-> $I$: [[Moment of Inertia]]
$$
w(x) = w(0) - \phi(0) \ x - \frac{1}{EI} \cdot \left( \frac{M(0) \ x^{2}}{2} + \frac{Q(0) \ x^{3}}{6} - \frac{q(x) \ x^{4}}{24} \right)
$$


# Boundary Conditions

## Hinged Support

![[Pasted image 20240713131428.png]]

Kinematic boundary conditions:
$$
w = 0, \quad w' \neq 0
$$
Static boundary conditions:
$$
M = 0, \quad Q \neq 0
$$

## Parallel Support

![[Pasted image 20240713131743.png]]
Kinematic boundary conditions:
$$
w \neq 0, \quad w' = 0
$$
Static boundary conditions:
$$
M \neq 0, \quad Q = 0
$$

## Clamped

![[Pasted image 20240713131906.png]]
Kinematic boundary conditions:
$$
w = 0, \quad w' = 0
$$
Static boundary conditions:
$$
M \neq 0, \quad Q \neq 0
$$

## Free End

![[Pasted image 20240713131953.png]]
Kinematic boundary conditions:
$$
w \neq 0, \quad w' \neq 0
$$
Static boundary conditions:
$$
M = 0, \quad Q = 0
$$

# With the Principle of Virtual Work

Beam deflection at a specific point $b$ can also be calculated using the [[Principle of Virtual Work]] by applying a force with magnitude 1 at $b$ creating a virtual moment $\overline{M}$
$$
w(b) = \int_\text{Beam length} \frac{\overline{M}(x) \cdot M(x)}{EI} dx
$$

# Example

![[Pasted image 20240713134514.png]]
$$
w(x) = w(0) - \phi(0) \cdot x - \frac{1}{EI} \cdot \left( \frac{M(0) \cdot x^{2}}{2} + \frac{Q(0) \cdot x^{3}}{6} - \frac{q \cdot x^{4}}{24} \right)
$$
Now the 4 constants $w(0)$, $\phi(0)$, $M(0)$ and $Q(0)$ have to be determined
$$
w(0) = 0, \quad M(0) = 0
$$
$$
w(L) = 0, \quad Q(L) = 0
$$
The formula therefore simplifies to
$$
w(x) = -\phi(0) \cdot x - \frac{1}{EI} \left( Q(0) \cdot \frac{x^{3}}{6} - q_{0} \cdot \frac{x^{4}}{24} \right)
$$
Inserting at the point $x=L$ gives
$$
0 = -\phi(0) \cdot L - \frac{1}{EI} \left( Q(0) \cdot \frac{L^{3}}{6} - q_{0} \cdot \frac{L^{4}}{24} \right)
$$
and
$$
0 = w'(L) = -\phi(0) - \frac{1}{EI} \left( Q(0) \cdot \frac{L^{2}}{2} - q_{0} \cdot \frac{L^{3}}{6} \right)
$$
Solving for the two unknowns results in
$$
\phi(0) = - \frac{q_{0} \cdot L^{3}}{48 \cdot EI}
$$
$$
Q(0) = \frac{3}{8} q_{0}\cdot L
$$
Resulting in the final deflection curve
$$
w(x) = \frac{q_{0}}{48 \cdot EI} (L^{3}x - 3Lx^{3} + 2 x^{4})
$$
![[Pasted image 20240713140254.png]]