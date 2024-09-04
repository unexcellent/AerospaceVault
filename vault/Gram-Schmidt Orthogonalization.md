#uni/courses/math1 

Given a set of [[Linear Independence of Vectors|linearly independent vectors]] $\{v_{1}, \cdots, v_{m}\}$ one can construct an [[Vector Space#Orthogonality|orthonormal system]] $\{u_{1}, \cdots, u_{m}\}$ with
$$
\text{span}(v_{1}, \dots, v_{m}) = \text{span}(u_{1}, \dots, u_{m})
$$
by using the recursive Gram-Schmidt orthogonalization algorithm.

1. Set $u_{1} = \frac{v_1}{||v_{1}||}$
2. Set $\widetilde{u}_{k+1} = v_{k+1} - \sum^{k}_{j=1} \langle v_{k+1}, u_{j} \rangle \cdot u_{j}$
3. Set $u_{k+1} = \frac{\widetilde{u}_{k+1}}{||\widetilde{u}_{k+1}||}$
4. If $k<m$, repeat with step 2