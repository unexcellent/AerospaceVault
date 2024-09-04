#uni/courses/thermo1 

Symbol: $H$
Unit: $J$

Enthalpy is an energy-like property where the value is entirely determined by the current [[Thermodynamic State|state]] of the [[Thermodynamic System|system]] and not by its history.
$$
H = U + p \cdot V
$$
-> $U$: [[Internal Energy]]
-> $p$: [[Pressure]]
-> $V$: [[Volume]]

# Differential

$$
dH = T \ dS + V \ dp
$$
-> $T$: [[Temperature]]
-> $S$: [[Entropy]]
-> $p$: [[Pressure]]
-> $V$: [[Volume]]

# First Derivative

## [[Isobaric Process]]

$$
\left( \frac{\partial H}{\partial S} \right)_{p} = T
$$

## [[Isentropic Process]]

$$
\left( \frac{\partial H}{\partial p} \right)_{S} = -V
$$

# Theorem of Schwarz

$$
\left( \frac{\partial T}{\partial p} \right)_{S}
= \left( \frac{\partial V}{\partial S} \right)_{p}
= \frac{\partial^{2} H}{\partial S \ \partial p}
$$