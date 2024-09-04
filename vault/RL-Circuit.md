#uni/courses/electrical 

Type of [[Electric Circuit]] containing [[Resistor|resistors]] and [[Inductor|inductors]].

# Charging

![[Pasted image 20240514184339.png|400]]

$$
i(t) = I_{0} \cdot \left( 1 - e^{-\frac{t}{\tau}} \right)
\quad \text{with } \tau = \frac{L}{R} 
$$
$$
v_{L}(t) = V_{0} \cdot e^{-\frac{t}{\tau}}
\quad \text{with } \tau = \frac{L}{R} 
$$
-> $i$: [[Current]]
-> $I_0$: Initial current
-> $t$: time
-> $L$: [[Inductance]]
-> $R$: [[Electrical Resistance]]
-> $v$: [[Voltage]]
-> $V_0$: Initial voltage

![[Pasted image 20240514184057.png|400]]

# Discharging

![[Pasted image 20240514184316.png|400]]
$$
i(t) = I_{0} \cdot e^{-\frac{t}{\tau}}
\quad \text{with } \tau = \frac{L}{R}
$$
$$
v_{L}(t) = - V_{0} \cdot e^{-\frac{t}{\tau}}
\quad \text{with } \tau = \frac{L}{R}
$$
-> $i$: [[Current]]
-> $I_0$: Initial current
-> $t$: time
-> $L$: [[Inductance]]
-> $R$: [[Electrical Resistance]]
-> $v$: [[Voltage]]
-> $V_0$: Initial voltage

![[Pasted image 20240514184609.png|400]]

