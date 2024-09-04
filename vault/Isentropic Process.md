#uni/courses/thermo1 

A special [[Process Path]] where the [[Entropy]] is constant. Isentropic processes are therefore [[Adiabatic Process|adiabatic]] and [[Thermodynamic Process#Reversible Process|reversible]].

This leads to
$$
\frac{p_{2}}{p_{1}} = \left( \frac{T_{2}}{T_{1}} \right)^\frac{\gamma}{\gamma-1}
\quad \text{and} \quad
\frac{T_{2}}{T_{1}} = \left( \frac{V_{1}}{V_{2}} \right)^{\gamma - 1}
$$
-> $p_{1}$: [[Pressure]] at state 1
-> $p_{2}$: [[Pressure]] at state 2
-> $T_{1}$: [[Temperature]] at state 1
-> $T_{2}$: [[Temperature]] at state 2
-> $\gamma$: [[Isentropic Exponent]]
-> $V_{1}$: [[Volume]] at state 1
-> $V_{2}$: [[Volume]] at state 2

# Isentropic Efficiency

In reality isentropic processes don't exist, because some [[Entropy]] will still get produced.

## Compressor

![[Pasted image 20240828130531.png|400]]
$$
\eta = \frac{w_{\text{isentropic,t}}}{w_{\text{real,t}}} = \frac{h_{2*} - h_{1}}{h_{2} - h_{1}} = \frac{\int_{1}^{2} v \ dp}{h_{2} - h_{1}}
$$
-> $\eta$: [[Thermal Efficiency]]
-> $h_{1}$: [[Thermodynamic State#Specific Property|specific]] [[Heat]] of state 1
-> $h_{2*}$: isentropic [[Thermodynamic State#Specific Property|specific]] [[Heat]] of state 2
-> $h_{2}$: real [[Thermodynamic State#Specific Property|specific]] [[Heat]] of state 2
-> $v$: [[Thermodynamic State#Specific Property|specific]] [[Volume]]
-> $p$: [[Pressure]]

## Turbine

![[Pasted image 20240828130553.png|400]]
$$
\eta = \frac{w_{\text{real,t}}}{w_{\text{isentropic,t}}} = \frac{h_{2} - h_{1}}{h_{2*} - h_{1}} = \frac{\int_{1}^{2} v \ dp}{h_{2} - h_{1}}
$$
-> $\eta$: [[Thermal Efficiency]]
-> $h_{1}$: [[Thermodynamic State#Specific Property|specific]] [[Heat]] of state 1
-> $h_{2*}$: isentropic [[Thermodynamic State#Specific Property|specific]] [[Heat]] of state 2
-> $h_{2}$: real [[Thermodynamic State#Specific Property|specific]] [[Heat]] of state 2
-> $v$: [[Thermodynamic State#Specific Property|specific]] [[Volume]]
-> $p$: [[Pressure]]

## Nozzle

![[Pasted image 20240828130626.png|400]]
$$
\eta = \frac{c_{1}^{2} - c_{2}^{2}}{c_{1}^{2} - c_{2*}^2}
$$
-> $\eta$: [[Thermal Efficiency]]
-> $c$: flow velocity