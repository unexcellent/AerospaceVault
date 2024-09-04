#uni/courses/math1 

Algorithm for calculating the [[Determinant of a Matrix|determinant]] of larger [[Matrix]].

Calculation of the determinant by eliminating one row and one column.

Choose a row $i$ which should be eliminated (ideally one with many zeros).

Then iterate the over the columns of the matrix $A \in \mathbb{R}^{n \times n}$ to create matrices without the row $i$ and the column $j$ $det(A_{ij})$.
$$
\det A = \sum\limits_{j=1}^{n} (-1)^{i+j} \cdot a_{ij} \cdot \det(A_{ij})
$$
Since $\det A = \det A^{T}$, the rows and columns can be switched.