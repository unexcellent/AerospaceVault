#uni/courses/electrical 

[[Power Electronic System]] for [[DC-DC Conversion]] with $V_{out} > V_{in}$ containing a [[Inductor]], a [[Diode]] and a [[Capacitor]]

![[Pasted image 20240521204811.png]]

# Switch Closed

![[Pasted image 20240521205011.png]]

Assumption:
- $V_{in} = \text{const.}$

$$
v_{L}(t) = V_{in} = L \cdot i_{L}(t)
$$
![[Pasted image 20240521205205.png]]

$$
i_{L}(t) = I_{S-} + \frac{V_{in}}{L} \cdot t
$$
![[Pasted image 20240521205348.png]]

# Switch Open

![[Pasted image 20240521205420.png]]

Assumptions:
- $V_{in} = \text{const.}$
- $V_{out} = \text{const.}$
- $V_{out} > V_{in}$

$$
v_{L}(t) = V_{in} - V_{out} = L \cdot i_{L}'(t)
$$
![[Pasted image 20240521205616.png]]

$$
i_{L}(t) = I_{S+} + \frac{V_{in} - V_{out}}{L} \cdot t
$$
![[Pasted image 20240521205656.png]]

# Control Law

$$
\frac{V_{out}}{V_{in}} = \frac{T_{S}}{t_{off}} = \frac{1}{1-d}
$$
with
$$
T_{S} = t_{on} + t_{off} = \frac{1}{f_{c}}
$$

# Current-Time Area

$$
\Delta Q = I_{out} \cdot t_{on} = I_{out} \cdot d \cdot T_{S}
$$

# Fluctuation of the Output 

$$
\Delta V_{out} = \Delta V_{C} = \frac{\Delta Q}{C} = \frac{V_{out}}{R_{load}} \cdot \frac{d \cdot T_{S}}{C}
$$