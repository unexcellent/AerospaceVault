#uni/courses/mech1 

- connect supporting structures with their environment
- impede the movement of a system
- transfer forces to the environment
- delimit the system under consideration (e.g. walls as supports or the entire structure on its base).

![[Pasted image 20231026084818.png]]

# Support Types

## In 2D

### Sliding Support

![[Pasted image 20231026102554.png|300]]

- vertical movement ❌
- horizontal movement ✅
- rotational movement ✅

r = 1

### Fixed Support

![[Pasted image 20231026102853.png|300]]

- vertical movement ❌
- horizontal movement ❌
- rotational movement ✅

r = 2

### Clamping

![[Pasted image 20231026102945.png|300]]

- vertical movement ❌
- horizontal movement ❌
- rotational movement ❌

r = 3

### Displaceable Clamping

![[Pasted image 20231026103031.png|300]]
- vertical movement ❌
- horizontal movement ✅
- rotational movement ❌

r = 2

### Sliding Sleeve

![[Pasted image 20231026103139.png|300]]
- vertical movement ✅
- horizontal movement ✅
- rotational movement ❌

r = 1

# Examples

## Single Span Beam

![[Pasted image 20231102084241.png]]

From the equilibrium conditions, the support reactions can be calculated as follows:
$$
\overrightarrow{\sum} F_{H} = 0: A_{H} + F_{1H} = 0
$$
$$
\overrightarrow{\sum} F_{V} = 0: A_{V} + B_{V} - F_{1V} - F_{2} = 0
$$
To calculate the moment a point has to be chosen. The point $A$ is convenient for that because $A_H$ and $A_V$ have a lever of $0$ and can therefore be ignored.
$$
\sum M_{A} = 0: B_{V} \cdot l_{3} - F_{1V} \cdot l_{1}  - F_{2} \cdot l_{2} = 0
$$

Note: This only works if the metal is not stretched beyond linear growth (beyond the point of elasticity)

## Three-Hinged Frame

![[Mechanical Supports 2023-11-08 18.11.29.excalidraw|600]]
From the frame itself, there are not enough equations available to solve the system. But we can split the upper joint for that.

For the left side:
![[Mechanical Supports 2023-11-08 18.25.34.excalidraw]]
$$
\overrightarrow{\sum} F_{H} = 0 = F_{1} + G_{H} + A_{H}
$$
$$
\Big\uparrow{\sum} F_{V} = 0 = A_{V} - G_{V}
$$
$$
\overrightarrow{\sum} M_{A} = 0 = h \cdot (F_{1} + G_{H}) + G_{V} \cdot l_{1} 
$$

For the right side:
![[Mechanical Supports 2023-11-08 18.34.26.excalidraw]]
$$
\overrightarrow{\sum} F_{H} = 0 = B_{H} - G_{H}
$$
$$
\Big\uparrow{\sum} F_{V} = 0 = B_{V} + G_{V} - F_{2}
$$
$$
\overrightarrow{\sum} M_{B} = 0 = G_{V} \cdot (l-l_{1}) - G_{H} \cdot h
$$

See [[Drawing 2023-11-08 19.02.14.excalidraw]] for calculation of complete calculations.