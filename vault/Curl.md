#uni/courses/math2 

Curl quantifies the circulation of a [[Vector Field]] at each point.

![[Pasted image 20240731193723.png]]

Given the vector field $v$ the curl is defined as
$$
\text{curl } v := \nabla \times v =  \begin{pmatrix}
\partial_{2} v_{3} - \partial_{3} v_{2} \\ 
\partial_{3} v_{1} - \partial_{1} v_{3} \\ 
\partial_{1} v_{2} - \partial_{2} v_{1} \\ 
\end{pmatrix}
$$
-> $\nabla$: [[Partial Derivative#Gradient|gradient]]

# Stokes Theorem

Stokes theorem states that
$$
\iint_{\Sigma} \langle \text{curl } F, \hat{v} \rangle \ dS = \int_{C} \langle F, \hat{\tau} \rangle \ ds
$$
-> $\Sigma$: [[Oriented Surface]]
-> $C$: [[Boundary]] of $\Sigma$
-> $F$: [[Vector Field]]
-> $\hat{v}$: outward normal [[Vector Field|field]] on $C$
-> $\hat{\tau}$: unit tangent [[Vector Field|field]] on $C$
![[Pasted image 20240731195325.png|450]]
