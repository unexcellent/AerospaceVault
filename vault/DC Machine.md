#uni/courses/electrical 

A machine, that can act as a [[Motor]] and [[Generator]] using DC current.

# Components

![[Pasted image 20240522101342.png]]

## Communicator

![[Pasted image 20240522101953.png|500]]

### Design

- Consists of individual [[Copper]] bars electrically insulated from each other
- Beginnings and endings of the armature coils are connected to the bars in sequence
- Contacting of the armature winding from the outside via stationary carbon brushes

### Effect

- Commutator acts like a rotation angle dependent switch, which keeps the [[Current|current]] pattern of the armature winding—and thus the direction of the armature transverse [[Magnetic Flux Density|flux density]] $\overrightarrow{B}_{A}$ — almost constant even when the rotor is rotating
- The commutating coils, whose current directions change from ⊙ to ⊗ (left) and from ⊗ to ⊙ (right), respectively, are located in the armature slots shown blank


# Equivalent Circuit

## Separately Excited

![[Pasted image 20240522130908.png]]

$$
V_{A} = R_{A} \cdot I_{A} + V_{i}
$$
-> $V_{A}$: Armature circuit [[Voltage]]
-> $R_{A}$: Armature circuit [[Electrical Resistance|resistance]]
-> $I_{A}$: Armature circuit [[Current]]
-> $V_{i}$: Induced [[Voltage]]

$$
V_{i} = k_{V} \cdot \Phi_{E} \cdot n_{m}
$$
-> $V_{i}$: Induced [[Voltage]]
-> $k_{V}$: Voltage constant
-> $\Phi_{E}$: Air gap [[Magnetic Flux|flux]] per excitation pole
-> $n_{m}$: Rotation rate in turns per time

$$
V_{E} = R_{E} \cdot I_{E}
$$
-> $V_{E}$: Excitation circuit [[Voltage]]
-> $R_{E}$: Excitation circuit [[Electrical Resistance|resistance]]
-> $I_{E}$: Excitation circuit [[Current]]

$$
T_{e} = k_{T} \cdot \Phi_{E} \cdot I_{A}
$$
-> $T_{e}$: [[Torque]] on the entire rotor
-> $k_{T}$: Torque constant
-> $\Phi_{E}$: Air gap [[Magnetic Flux|flux]] per excitation pole
-> $I_{A}$: Armature circuit [[Current]]

$$
T_{e} - T_{fric} - T_{load} = 0
$$
-> $T_{e}$: [[Torque]] on the entire rotor
-> $T_{fric}$: [[Torque]] lost to friction
-> $T_{load}$: Load [[Torque]]

$$
k_{V} = 4p \cdot N_{A}
$$
-> $k_{V}$: Voltage constant
-> $p$: Number of pole pairs
-> $N_{A}$: Number of armature coil windings

$$
k_{T} = \frac{k_{V}}{2\pi}
$$
-> $k_{T}$: Torque constant
-> $k_{V}$: Voltage constant

$$
\Phi_{E} = k_{\Phi} \cdot I_{E}
$$
-> $\Phi_{E}$: Air gap [[Magnetic Flux|flux]] per excitation pole
-> $k_{\Phi}$: Flux constant
-> $I_{E}$: Excitation circuit [[Current]]

$$
k_{\Phi}= \frac{L_{E}}{N_{E}}
$$
-> $k_\Phi$: Flux constant
-> $L_{E}$: Excitation [[Inductance]]
-> $N_{E}$: Number of excitation coil windings

$$
P = \omega_{m} \cdot T_{e} = V_{A} \cdot I_{A} + V_{E} \cdot I_{E}
$$
-> $P$: [[Electrical Power|power]]
-> $\omega_{m}$: Rotation rate in $\pi$ per time
-> $T_{e}$: [[Torque]] on the entire rotor
-> $V_{A}$: Armature [[Voltage]]
-> $I_{A}$: Armature circuit [[Current]]
-> $V_{E}$: Excitation circuit [[Voltage]]
-> $I_{E}$: Excitation circuit [[Current]]

## Shunt-Wound

![[Pasted image 20240523195548.png]]

Assumption:
- $\Phi_{E} = \text{const.}$

### Special Case 1

With $n_{m} = 0$, $V_{i} = 0$
$$
I_{A,st} = I_{A} = \frac{V_{A}}{R_{A}}
$$
-> $I_{A,st}$: Starting [[Current]]
-> $I_{A}$: Armature [[Current]]
-> $V_{A}$: Armature [[Voltage]]
-> $R_{A}$: Armature [[Electrical Resistance|resistance]]

### Special Case 2

With $I_{A} = 0$, $V_{i} = V_{A}$
$$
n_{0} = \frac{V_{A}}{k_{V} \cdot \Phi_{E}} 
$$
-> $n_{0}$: No-load rotation rate
-> $V_{A}$: Armature [[Voltage]]
-> $k_{V}$: Voltage constant
-> $\Phi_{E}$: Air gap [[Magnetic Flux|flux]] per excitation pole

## Series Wound

![[Pasted image 20240523200405.png]]

$$
I_{E} = k_{E} \cdot I_{A}
$$
$$
k_{E} = \frac{R_{p}}{R_{E} + R_{p}}
$$
-> $I_{E}$: Excitation circuit [[Current]]
-> $k_{E}$: Excitation constant
-> $I_{A}$: Armature circuit [[Current]]
-> $R_{p}$: Potentiometer [[Electrical Resistance|resistance]]
-> $R_{E}$: Excitation [[Electrical Resistance|resistance]]

