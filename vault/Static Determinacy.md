#uni/courses/mech1 

A System is statically determined, if
- all bearing reactions can be calculated from the equilibrium conditions.
- all [[Degrees of Freedom|degrees of freedom]] of the system are uniquely constrained.
- no pole exists for any structural element

# Necessary Criteria

## Counting Criterion

With:
- $S$ = Number of [[Mechanical Supports|support reactions]] (sum of al r-values of all supports)
- $I$ = Number of intermediate reactions of the joints
	- For moment joints: $I = 2 \cdot (\text{Number of connected Elements}-1)$
- $E$ = Number of connecting elements (i.e. bars)
$$
S + I - 3 \cdot E = 0
$$

![[Static Determinacy 2023-11-02 16.46.32.excalidraw]]
- $S = 2 + 1$ (red)
- $I = 2 + 4 + 6 + 4 + 2 = 18$ (green)
- $E = 7$ (blue)

The equation above states the degree of indeterminacy with $0$ meaning the system is determinate. A result of $2$ would mean indeterminacy of degree $2$.

# Pole Criterion

Fulfilled if there is no contradiction in the [[Pole Plan]]