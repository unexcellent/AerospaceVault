#uni/courses/electrical 

Synchronous machines are machines that act as [[Motor|motors]] and [[Generator|generators]] using AC current.
![[Pasted image 20240808103248.png|400]]

# Design

- Stator: symmetrical, three-phase coil winding
- Rotor: Single-phase excitation winding carrying DC current

![[Pasted image 20240808104559.png]]
$$
v_{A}(t) + v_{B}(t) + v_{C}(t) \equiv 0
$$
The [[Magnetic Flux Density]] from the excitation winding can be expressed in rotor-fixed coordinates as
$$
B_{E}(\vartheta_{2}, t) = \hat{B}_{E} \cdot \cos(p \cdot \vartheta_{2}(t))
$$
-> $\vartheta_{2}$: rotor angle
-> $\hat{B}_{E}$: excitation [[Magnetic Flux Density]] amplitude
-> $p$: number of pole pairs

The [[Magnetic Flux Density]] of each stator branch is calculated by
$$
B_{1}(\vartheta_{1}, t) = \hat{B}_{1} \cdot \cos(p \cdot \vartheta_{1}) \cdot \cos(\omega_{1} t + \varphi)
$$
-> $\hat{B}_{1}$: [[Magnetic Flux Density]] amplitude of the stator branch
-> $p$: number of pole pairs
-> $\vartheta_{1}$: stator angle
-> $\omega_{1}$: stator phase angular velocity
-> $\varphi$: initial phase angle

## Equivalent Circuit Diagram

![[Pasted image 20240808113750.png|450]]
-> $\underline{V}_{1}$: stator [[Voltage]]
-> $\underline{I}_{1}$: stator [[Current]]
-> $\underline{V}_{p}$: synchronous generated [[Voltage]]
-> $R_{1}$: ohmic [[Electrical Resistance|resistance]] of a stator branch
-> $X_{d}$: synchronous [[Reactance]]

with
$$
X_{d} = \omega_{1} L_{d} = \omega_{1} \cdot (L_{1m} + L_{1\sigma})
$$
-> $\omega_{1}$: stator angular phase velocity
-> $L_{d}$: synchronous [[Inductance]]
-> $L_{1m}$: main [[Inductance]] of a stator branch
-> $L_{1\sigma}$: leakage [[Inductance]] of a stator branch