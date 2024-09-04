#uni/courses/electrical 

Symbol: $V$

Voltage causes a current flow in the consumer. It describes the energy to transport a given quantity of charge.
$$
V = \frac{W}{Q}
$$
Using [[Ohm's Law]] we find:
$$
V = R \cdot I = \rho \cdot \frac{l}{A}
$$
It can also be defined as the difference in potential between two points
$$
V = \varphi_{A} - \varphi_{B}
$$

# Unit

Volt $[V]$
$$
1 V = 1 \frac{J}{As} = 1 \frac{W}{A}
$$

# In an [[AC Circuit]]

When the voltage is alternating in a sinus pattern, it can be expressed as a time varying quantity
$$
v(t) = \hat{V} \cdot \sin(\omega t + \varphi_{V})
$$
-> $\hat{V}$: voltage amplitude
-> $\omega$: angular velocity
-> $t$: time
-> $\varphi_{V}$: phase shift

## Effective Voltage

The effective voltage is a measure of the amount of voltage that can actually perform work
$$
V_{\text{RMS}} = \frac{\hat{V}}{\sqrt{2}}
$$

## Complex Form

$$
\underline{V} = V_\text{RMS} \cdot e^{j \varphi_{V}}
$$