#uni/courses/mech1 

Pole plans analyze whether a system is movable.
If no rotation poles can be found, it is immovable.

# Pole Beams

Pole beams extend from poles orthogonal to the direction of motion of elements.
![[Pole Plan 2024-02-22 10.06.25.excalidraw]]

# Poles

There are two types of poles:
- **Main Poles:** Poles of rotation around a rigid body. The pole itself does not move. Designated as $(0, i)$
- **Relative Poles:** Poles around which a rigid body $i$ rotates with respect to another rigid body $j$. Designated as $(i, j)$

If two main poles $(0, i)$, $(0, j)$ are connected, they form a relative pole $(i, j)$ in the order $(0,i) - (i, j) - (0, j)$.
![[Pole Plan 2024-02-22 10.16.49.excalidraw|300]]![[Pole Plan 2024-02-22 10.20.01.excalidraw|300]]
# Displacement Figure

If the pole plan does not lead to a contradiction, i.e. there is only one pole per element, one can draw how the system can move.

![[Pole Plan 2024-02-22 13.59.12.excalidraw]]
![[Pole Plan 2024-02-22 14.03.51.excalidraw]]

# General Rules

- fixed two value supports are always main poles![[Pole Plan 2024-02-22 16.01.08.excalidraw|150]]
- Sliding two value supports have their pole in infinity![[Pole Plan 2024-02-22 16.02.53.excalidraw|150]]
- Sliding one value supports have a geometric place along the line perpendicular to the direction of motion. The pole is then located where this line intersects with another pole beam ![[Pole Plan 2024-02-22 16.12.16.excalidraw]]
- Rotary joints between two main poles are always the relative pole ![[Pole Plan 2024-02-22 16.21.16.excalidraw]]