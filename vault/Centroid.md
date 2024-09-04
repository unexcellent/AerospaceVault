#uni/courses/mech2 

The centroid is the center of [[Mass]] of a body.

Given an equal mass distribution inside the body, the centroid coordinates are
$$
C(x,y) = \begin{pmatrix}
\frac{S_{x}}{A} \\ 
\frac{S_{y}}{A} \\ 
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{A} \cdot \int_{A} y \ dA \\
\frac{1}{A} \cdot \int_{A} x \ dA \\
\end{pmatrix}
$$
-> $x$: x-axis
-> $y$: y-axis
-> $S$: [[First Moment of Area]]
-> $A$: area

# Geometric Decomposition

Given a more complex shape
![[Centroid 2024-07-07 10.40.39.excalidraw]]
the shape can be decomposed into simpler shapes.
![[Centroid 2024-07-07 10.44.48.excalidraw]]
The centroid is then
$$
C = \frac{\sum_{i} C_{i} \cdot A_{i}}{\sum_{i} A_{i}}
$$