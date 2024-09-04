#uni/courses/math2 

A [[Area#Connected|connected]] and [[Area#Compact|compact area]] $K \subseteq \mathbb{R}^{2}$ and a mapping $\varphi: K \to \mathbb{R}^{3}$ are called a regular surface if
- $\varphi$ is differentiable (there are no sharp edges on $\varphi(K)$)
- the [[Vector-Valued Function#Jacobian|jacobian]] of $\varphi$ $J_\varphi(u,v)$ has [[Rank of a Matrix|rank]] 2 for all [[Linear Independence of Vectors|linearly independent]] $u, v \in \dot{K}$
- $\varphi_{u}$, $\varphi_{v}$ are linearly independent for all linearly independent $u, v \in \dot{K}$

![[Pasted image 20240722150846.png]]

# Tangent Plane

The tangent [[Planes in Euclidian Space|plane]] to $\varphi(K)$ at $P_{0} = \varphi(w_{0})$ is given by
$$
x = \varphi(w_{0}) + \varphi_{u}(w_{0})\cdot(u-u_{0}) + \varphi_{v}(w_{0})\cdot(v-v_{0})
$$

# Area

The area of of $\varphi(K)$ is defined by
$$
\iint_{K} || \varphi_{u} \times \varphi_{v} || \ dA(u,v)
$$

# Properties

A regular surface is called
- **closed** if it has no [[Boundary]]
