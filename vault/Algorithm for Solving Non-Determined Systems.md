#uni/courses/mech1 

1. Calculate the degree of determinacy $m$ via [[Static Determinacy#Counting Criterion]]
2. Create $m+1$ O-systems with each being statically determined
3. Calculate the truss-force $S_{i}^{k}$ with i referring to the truss and k referring to the system
	- use one truss force as the base line and replace one other with $1$ and omit the others
	- solve each statically determined system
4. Calculate all possible combinations of $\delta_{k_{1}k_{2}} = \delta_{k_{2}k_{1}} = \displaystyle\sum_{i} \dfrac{S_{i}^{k_{1}} \cdot S_{i}^{k_{2}} \cdot l_{i}}{(EA)_{i}}$ 
5. The following systems of equations can be created with all $\delta$-values
	- $0 = \displaystyle\sum_{k_{2}=0}^{m} \delta_{k_{1}k_{2}} \cdot X_{k_{2}} \quad \forall k_{1} \in (0, m]$ with $X_{0} = 1$
6. Solve for all $X$
7. Each unknown force of the system $S_{i}$ can then be calculated with
	- $S_{i} = \displaystyle\sum_{k_{2}=0}^{m} S^{k_{2}}_{i} \cdot X_{k_{2}}$
