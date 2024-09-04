#uni/courses/electrical 

Main actor of [[Electrical Capacitance]]

# Charge

$$
Q = C \cdot V
$$

# Current

$$
i_C = \frac{dq_{c}(t)}{dt} = C \frac{dv_{c}(t)}{dt}
$$

# Parallel Connection

$$
v_{1}(t) = v_{2}(t) = \cdots = v_{n}(t)
$$
$$
i(t) = i_{1}(t) + i_{2}(t) = \cdots = i_{n}(t)
$$
$$
C_{tot} = C_{1} + C_{2} + \cdots + C_{n}
$$

# Series Connection

$$
i_{1}(t) = i_{2}(t) = \cdots = i_{n}(t)
$$
$$
v(t) = v_{1}(t) + v_{2}(t) = \cdots = v_{n}(t)
$$
$$
\frac{1}{C_{tot}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \cdots + \frac{1}{C_{n}}
$$

# Charging a Capacitor

$$
v_{C}(t) = V_{0} \cdot (1-e^{\frac{-t}{\tau}})
$$
$$
i(t) = I_{0} \cdot e^{\frac{-t}{\tau}}
$$
with $\tau = R \cdot C$.

# Discharging a Capacitor

$$
v_{C}(t) = V_{0} \cdot e^{- \frac{t}{\tau}}
$$
$$
i(t) = -I_{0} \cdot e^{- \frac{t}{\tau}} \qquad I_{0} = \frac{V_{0}}{R}
$$

# Total Energy Content
$$
W_{el} = \frac{1}{2} \cdot C \cdot V^{2} = \frac{1}{2} \cdot \varepsilon \cdot \frac{A}{d} \cdot V^{2}
$$

# Effect on an [[AC Circuit]]

![[Pasted image 20240804173829.png]]