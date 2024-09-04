#uni/courses/math2 

Divergence describes the quantity of a [[Vector Field|vector fields]] source at each point i.e. how much field is "produced" or "consumed" at that point.
![[Divergence 2024-07-31 19.30.53.excalidraw|2000]]

Given the vector field $v$ the divergence is defined as
$$
\text{div } v := \langle \nabla, v \rangle = \sum^{n}_{i=1} \frac{\partial v_{i}}{\partial x_{i}}
$$
-> $\nabla$: [[Partial Derivative#Gradient|gradient]]
-> $\partial$: [[Partial Derivative]]

# Divergence Theorem

The divergence theorem states, that
$$
\iint_{R} \text{div } F \ dA = \int_{\partial R} \langle F, \hat{v} \rangle \ ds
$$
-> $R$: closed [[Regular Surface]]
-> $\partial R$: [[Boundary]] of $R$
-> $F$: [[Vector Field]]
-> $\hat{v}$: outward normal [[Vector Field|field]] on $\partial R$

![[Pasted image 20240731194803.png|500]]