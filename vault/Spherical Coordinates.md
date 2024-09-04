#uni/courses/math2 

In $\mathbb{R}^{3}$ all coordinates of a volume $U$ can either be described via cartesian coordinates $x,y$ or via polar coordinates by
$$
x = r \cdot \sin \phi \cdot \cos \theta
$$
$$
y = r \cdot \sin \phi \cdot \sin \theta
$$
$$
z = r \cdot \cos \phi
$$
![[Pasted image 20240624151135.png|500]]
This can be used for [[Integration#Integration by Substitution|integration by substitution]].

# Bounds

If it is a full sphere with radius 1 the bounds are
$$
0 \le \phi \le \pi
$$
$$
0 \le \theta \le 2\pi
$$
$$
0 \le r \le 1
$$

# Jacobian

The [[Determinant of a Matrix|determinant]] [[Vector-Valued Function#Jacobian|jacobian]] the transformation is then
$$
\det J(r, \phi, \theta) = r^{2} \cdot \sin \phi
$$