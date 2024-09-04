#uni/courses/thermo1 

Symbol: $G$
Unit: $J$

The Gibbs energy change is the maximum amount of non-volume expansion [[Thermodynamic Work|work]] that can be extracted from a [[Isothermal Process|isothermal]], [[Isobaric Process|isobaric]] [[Thermodynamic System#Closed System|closed system]].
$$
G = U + pV - TS = H - TS
$$
-> $U$: [[Internal Energy]]
-> $p$: [[Pressure]]
-> $V$: [[Volume]]
-> $T$: [[Temperature]]
-> $S$: [[Entropy]]
-> $H$: [[Enthalpy]]

# Differential

$$
dG = -S \ dT + V \ dp
$$
-> $T$: [[Temperature]]
-> $S$: [[Entropy]]
-> $p$: [[Pressure]]
-> $V$: [[Volume]]

# First Derivative

## [[Isobaric Process]]

$$
\left( \frac{\partial G}{\partial T} \right)_{p} = -S
$$

## [[Isothermal Process]]

$$
\left( \frac{\partial G}{\partial p} \right)_{T} = V
$$

# Theorem of Schwarz

$$
-\left( \frac{\partial S}{\partial p} \right)_{T}
= \left( \frac{\partial V}{\partial T} \right)_{p}
= \frac{\partial^{2} G}{\partial T \ \partial p}
$$