#uni/courses/mech2 

A coordinate system for a body where the [[Moment of Inertia|deviation moments]] disappear (the [[Moment of Inertia#Tensor Representation|moment tensor]] becomes [[Matrix#Diagonalizable Matrices|diagonal]]).
$$
I_{\eta \zeta} = \begin{pmatrix}
I_{\eta \eta} & 0 \\ 
0 & I_{\zeta \zeta}
\end{pmatrix}
= \begin{pmatrix}
\cos \alpha & \sin \alpha \\ 
- \sin \alpha & \cos \alpha
\end{pmatrix}
\cdot \begin{pmatrix}
I_{yy} & I_{yz} \\ 
I_{yz} & I_{zz}
\end{pmatrix}
\cdot \begin{pmatrix}
\cos \alpha & -\sin \alpha \\ 
\sin \alpha & \cos \alpha
\end{pmatrix}
$$
$$
I_{\eta \eta} = \sin^{2} \alpha \cdot I_{zz} + 2 \cos \alpha \cdot \sin \alpha \cdot I_{yz} + \cos^{2} \alpha \cdot I_{yy}
$$
$$
I_{\zeta \zeta} = \cos^{2} \alpha \cdot I_{zz} + 2 \cos \alpha \cdot \sin \alpha \cdot I_{yz} + \sin^{2} \alpha \cdot I_{yy}
$$

The angle of the axes $\alpha$ can be calculated via
$$
\alpha = \frac{1}{2} \cdot \arctan \left(\frac{2 \cdot I_{yz}}{I_{yy} - I_{zz}} \right)
$$

The individual axis transformations are given by
$$
\eta = y \cdot \cos \alpha + z \cdot \sin \alpha
$$
$$
\zeta = -y \cdot \sin \alpha + z \cdot \cos \alpha
$$
And the reverse transformations by
$$
y = \eta \cdot \cos \alpha - \zeta \cdot \sin \alpha
$$
$$
z = \eta \cdot \sin \alpha + \zeta \cdot \cos \alpha
$$