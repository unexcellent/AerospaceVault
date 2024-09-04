#uni/courses/math0 
#uni/courses/math1 

Method of solving [[Linear Systems of Equations]].
Based on two observations:
- If the [[Matrix|matrix]] $A$ has upper-triangular form, then $Ax=b$ can be solved easily, e.g.:
$$
\begin{align}
1x_1 + 1x_2 + 2 = 2 \\
1x_2 - 4x_3 = -4 \\
-5x_3 = -3 \\
\Leftrightarrow \\
\begin{pmatrix}
1 & 1 & 2 \\
0 & 1 & -4 \\
0 & 0 & -5
\end{pmatrix}x = 
\begin{pmatrix}
2 \\
-4 \\
-3
\end{pmatrix}
\end{align}
$$
- The solution set $\mathbb{L}$ of and SLE does not change if 
	- lines are switched
	- lines are multiplied by a scalar $\lambda \in \mathbb{R}\backslash \{0\}$
	- two lines are added while keeping one of the original lines

# Step 1

Is $a_{11} \neq 0$? ($a_{11}$ is a pivot element)
- If yes go to next step
- If no look for an element $a_{k1} \neq 0$ (one of the elements of the first column) and you swap the entire row with the row number $1$. Start over from Step 1

# Step 2

For $i=2, \cdots, m$ (for all the rows $2$ to $m$) Add $\left(- \frac{a_{i1}}{a_{11}}\right)\times \text{ the first row}$. This is going to produce a new matrix with all zeros in the first columns except $a_{11}$. 

# Step 3

Repeat Step 1 and Step 2 for the system of equations consisting in all the remaining equations from row $2$ to row $m$ of the new matrix.

How does the new matrix $(\widetilde{A}|\widetilde{b})$ look like?
$$
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_1n & b_1 \\ 
0 & \widetilde{a}_{22}  & \cdots & \widetilde{a}_{2n} & \widetilde{b}_{2} \\ 
0 & 0  & \cdots & \widetilde{a}_{3n} & \widetilde{b}_{3} \\ 
\end{pmatrix}
$$
Remark: The system has a solution only if $\widetilde{b}_{r+1} = \widetilde{b}_{r+2} = \cdots = \widetilde{b}_{m}=0$ 

