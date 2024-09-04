#uni/courses/electrical 

Symbol: $\rho$

# Definition

Resistivity is a [[Material]] property describing the resistance of a material to electricity per unit length.

# Unit

Ohm-meters $[\Omega \cdot m]$

# Temperature Dependence

$\rho$ depends on the temperature. Usually the specific resistance for a material at 20°C ($\rho_{20}$) is provided as well as the change in resistance per degree in $°C^{-1}$ ($\alpha_{20}$). The specific resistance can then be calculated using the following formula:
$$
\rho(\vartheta) = \rho_{20} \cdot (1 + \alpha_{20} \cdot (\vartheta - 20°C))
$$
-> $\vartheta$: [[Temperature]]
-> $\rho_{20}$: resistivity at 20°C
-> $\alpha_{20}$: change in resistance per degree $[°C^{-1}]$

# Material Values

| Material     | $\rho_{20}$ in $[\frac{\Omega \cdot mm^{2}}{m}]$ | $\alpha_{20}$ in $[°C^{-1}]$ |
| ------------ | ------------------------------------------------ | ---------------------------- |
| Silver       | $0.016$                                          | $0.0038$                     |
| [[Copper]]   | $0.0175$                                         | $0.0039$                     |
| [[Aluminum]] | $0.028$                                          | $0.0038$                     |
| Wolfram      | $0.055$                                          | $0.0041$                     |
| Mangan       | $0.43$                                           | $1 \cdot 10^{-5}$            |
| Constantan   | $0.50$                                           | $-3 \cdot 10^{-5}$           |
