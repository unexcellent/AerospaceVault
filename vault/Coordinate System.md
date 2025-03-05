#uni/courses/mech3 

A coordinate system describes the reference frame of the [[Position]], [[Velocity]] and [[Acceleration]] [[Vector|vectors]]. Coordinate systems are chosen to simplify a problem.
![[Pasted image 20241110165758.png|500]]

Coordinate systems can either be stationary, moving or rotating.

# Cartesian

The cartesian coordinate system is the default with one [[Position]] variables for each axis.
![[Pasted image 20241207140617.png|400]]
The parameters of the coordinate system are described as
$$
r_{P|\hat{O}}(t) = \begin{pmatrix}
X(t)\\ Y(t) \\ Z(t)
\end{pmatrix}_{XYZ}
$$
$$
v_{P}(t) = \dot{r}_{P|\hat{O}}(t) = \begin{pmatrix}
\dot{X}(t)\\ \dot{Y}(t) \\ \dot{Z}(t)
\end{pmatrix}_{XYZ}
$$
$$
a_{P}(t) = \ddot{r}_{P|\hat{O}}(t) = \begin{pmatrix}
\ddot{X}(t)\\ \ddot{Y}(t) \\ \ddot{Z}(t)
\end{pmatrix}_{XYZ}
$$
-> $r$: [[Position]]
-> $v$: [[Velocity]]
-> $a$: [[Acceleration]]

# Polar

[[Polar Coordinates|Polar]] defines the position based on the
- projected radius $r(t)$
- angle $\theta(t)$
- height $z(t)$

![[Pasted image 20241207141226.png|400]]

The parameters of the coordinate system are described as
$$
\overrightarrow{r}_{P|\hat{O}}(t) = r(t) \cdot \overrightarrow{e}_{r}(\theta(t)) + z(t) \cdot \overrightarrow{e}_{z}(\theta(t))
$$
$$
\overrightarrow{v}(t) = \begin{pmatrix}
\dot{r} \\ r \dot{\theta} \\ \dot{z}
\end{pmatrix}_{r \theta z}
$$
$$
\overrightarrow{a}(t) = \begin{pmatrix}
\ddot{r} - r \dot{\theta}^{2} \\ 
r \ddot{\theta} + 2 \dot{r} \dot{\theta} \\ 
\ddot{z}
\end{pmatrix}_{r \theta z}
$$
-> $r$: [[Position]]
-> $v$: [[Velocity]]
-> $a$: [[Acceleration]]
-> $\overrightarrow{e}_{r}$: planar [[Vector]] pointing towards $P$ with a length of $1$
-> $\overrightarrow{e}_{z}$: linear [[Vector]] pointing towards $P$ in the $z$ direction with a length of $1$

# Spherical

[[Spherical Coordinates|Spherical]] defines coordinates based on
- the radius $R(t)$
- the angle $\phi(t)$
- the angle $\theta(t)$

![[Pasted image 20241207142809.png|400]]
The parameters of the coordinate system are described as
$$
r(t) = R(t) \cdot e_{r} \big( \phi(t), \theta(t) \big)
$$
$$
v_{P}(t) = \begin{pmatrix}
\dot{R} \\ R \cdot \dot{\phi} \\ R \cdot \dot{\theta} \cdot \sin(\phi)
\end{pmatrix}_{R \phi \theta}
$$
$$
a_{P}(t) = \begin{pmatrix}
\ddot{R} - R \cdot \dot{\phi}^{2} - R \cdot \dot{\theta}^{2} \cdot \sin^{2} (\phi) \\ 
2 \cdot \dot{R} \cdot \dot{\theta} \cdot \sin(\phi) + 2 \cdot R \cdot \dot{\theta} \cdot \dot{\phi} \cdot \cos(\phi) + R \cdot \ddot{\theta} \cdot \sin(\phi) \\ 
2 \cdot \dot{R} \cdot \dot{\phi} + R \cdot \ddot{\phi} - R \cdot \dot{\theta}^{2} \cdot \sin(\phi) \cdot \cos(\phi)
\end{pmatrix}_{R \phi \theta}
$$
with
$$
e_{r} = \begin{pmatrix}
\sin(\phi) \cdot \cos(\theta) \\ 
\sin(\phi) \cdot \sin(\theta) \\
\cos(\phi)
\end{pmatrix}_{XYZ}
$$
$$
e_{\theta} = \begin{pmatrix}
-\sin(\theta) \\ 
\cos(\theta) \\ 
0
\end{pmatrix}_{XYZ}
$$
$$
e_{\phi} = e_{\theta}\times e_{r} = \begin{pmatrix}
\cos(\phi) \cdot \cos(\theta) \\ 
\cos(\phi) \cdot \sin(\theta) \\ 
-\sin(\phi)
\end{pmatrix}_{XYZ}
$$
