#uni/courses/electrical 

Induction machines are machines that act as [[Motor|motors]] and [[Generator|generators]] using three-phase AC current.

# Basic Facts

- More than $90 \%$ of all electromechanical energy converters are induction machines
- Power range: from a few watts to approx. $30 \ MW \ (p = 2)$
- Spectrum of the numbers of pole pairs: $1 \le p \le 30^{4}$

# Design

## Stator

![[Pasted image 20240808151724.png|400]]
- Iron lamination stack with $Z_{N1}$ slots
- Symmetrical, three-phase coil winding
- Number of pole pairs p (here: p = 1)
- Supply from a symmetrical rotary voltage system
- Develops a rotating field ($n_{syn} = \frac{f_{1}}{p}$)
- Phases A, B and C connected in star or delta

## Slip Ring Rotor

![[Pasted image 20240808152057.png|400]]

- Iron lamination stack with $Z_{N2}$ slots
- Symmetrical, three-phase coil winding
- Phases a, b and c connected in star or delta
- Ends of the phase windings connected to three or six slip rings
- Slip rings short-circuited via
	- -> series [[Resistor|resistors]] during starting and
	- -> directly during rated operation
- No active power supply from outside

![[Pasted image 20240808152346.png|450]]

## Squirrel Cage Rotor

![[Pasted image 20240808152710.png|400]]

- Iron lamination stack with $Z_{N2}$ slots
- Cage made of bars in the slots and two end rings (axial front and back)
- Bar materials: [[Copper]], [[Aluminum]]
- No active power supply from outside

# Stator Voltage

![[Pasted image 20240808153008.png]]
$$
\underline{V}_{1} = V_{1} \cdot e^{j \cdot \varphi_{V}}, \qquad 
\overrightarrow{v}_{1}(t) = \sqrt{2} \cdot \underline{V}_{1} \cdot e^{j \cdot \omega_{1} \cdot t}
$$
-> $\underline{V}_{1}$: complex stator [[Voltage]]
-> $V_{1}$: [[Voltage#Effective Voltage|effective voltage]]
-> $\varphi_{V}$: initial phase shift
-> $\omega_{1}$: stator angular phase velocity

# Stator Current

$$
\underline{I}_{1} = I_{1} \cdot e^{j \cdot \varphi_{I}}, \qquad 
\overrightarrow{i}_{1}(t) = \sqrt{2} \cdot \underline{I}_{1} \cdot e^{j \cdot \omega_{1} \cdot t}
$$
-> $\underline{I}_{1}$: complex stator [[Current]]
-> $V_{1}$: [[Current#Effective Current|effective current]]
-> $\varphi_{I}$: initial phase shift
-> $\omega_{1}$: stator angular phase velocity

# Angular Velocity

$$
\omega_{\text{m}} = \omega_{\text{syn}} = 2\pi \cdot \frac{f_{1}}{p}, \qquad 
w_{2} = 2\pi \cdot f_{2}  = p \cdot(\omega_{\text{syn}} - \omega_{\text{m}})
$$
-> $\omega_{\text{m}}$: mechanical angular velocity
-> $\omega_{\text{syn}}$: mechanical angular velocity of the rotor relative to the stator
-> $f_{1}$: stator current frequency
-> $p$: number of pole pairs
-> $f_{2}$: rotor current frequency

# Slip

Slip is the normalized deviation of the mechanical speed from the synchronous speed.
$$
s = \frac{\omega_{\text{syn}} - \omega_{\text{m}}}{\omega_{\text{syn}}} = \frac{f_{2}}{f_{1}}
$$
-> $\omega_{\text{m}}$: mechanical angular velocity
-> $\omega_{\text{syn}}$: mechanical angular velocity of the rotor relative to the stator
-> $f_{1}$: stator current frequency
-> $f_{2}$: rotor current frequency

# Leakage

The [[Current]] in the stator generates beside the main [[Magnetic Field]] also a leakage [[Magnetic Field|field]].
The leakage can be represented as an [[Inductance]] $L_{A, \sigma}$.
$$
L_{A} = L_{A,m} + L_{A,\sigma}, \qquad \sigma_{A} = \frac{L_{A,\sigma}}{L_{A,m}}
$$
-> $L_{A}$: total phase [[Inductance]]
-> $L_{A,m}$: main [[Magnetic Field|field]] [[Inductance]]
-> $L_{A,\sigma}$: leakage [[Magnetic Field|field]] [[Inductance]]
-> $\sigma_{A}$: leakage coefficient

# Steady State Operations

$$
\underline{I}'_{2} = \frac{1}{n_{\text{wr}}} \cdot \underline{I}_{2}, \quad
R'_{2} = n_{\text{wr}}^{2} \cdot R_{2}, \quad
L'_{2} = n_{\text{wr}}^{2} \cdot L_{2}, \quad
n_{\text{wr}} = \frac{N_{1}ξ_{1(1)}}{N_{2}ξ_{2(1)}}
$$
-> $\underline{I}'_{2}$: rotor [[Current]] converted to the stator
-> $R_{2}'$: rotor [[Electrical Resistance|resistance]] converted to the stator
-> $L'_{2}$: rotor [[Inductance]] converted to the stator
-> $n_{\text{wr}}$: winding ratio
-> $N_{1}ξ_{1(1)}, N_{2}ξ_{2(1)}$: effective number of turns

# Torque

$$
T_{\text{po}} = \frac{3}{2} \cdot p \cdot (1-\sigma) \cdot \frac{V_{1}^{2}}{\omega_{1}^{2} \cdot L_{\sigma}}, \quad
T_{e} = T_{\text{po}} \cdot \frac{2 s_{0} s_{\text{so}}}{s_{0}^{2} + s_{\text{so}}^{2}}
$$
$$
s_{\text{po}} = \frac{R_{2}}{\sigma \cdot \omega_{1} \cdot L_{2}}
$$
-> $T_{e}$: [[Torque]]
-> $T_{\text{po}}$: pull-out [[Torque]]
-> $p$: number of pole pairs
-> $\sigma$: [[Induction Machine#Leakage|leakage coefficient]]
-> $V_{1}$: stator branch [[Voltage]]
-> $\omega_{1}$: stator branch angular phase velocity
-> $L_{\sigma}$: leakage [[Inductance]]
-> $s_{\text{po}}$: pull-out [[Induction Machine#Slip|slip]]

# Equivalent Circuit Diagram

![[Pasted image 20240808163022.png]]