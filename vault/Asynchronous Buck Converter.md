#uni/courses/electrical 

[[Current]] containing a switch, a [[Resistor]], an [[Inductor]], a [[Capacitor]] and a [[Diode]] used for [[DC-DC Conversion]].

![[Pasted image 20240519132150.png]]

# Switch Closed

The current does not flow through the [[Diode]].

![[Pasted image 20240519132315.png]]

Assumptions:
- $V_{in} = \text{const.}$
- $V_{out} = \text{const.}$
- $V_{out} < V_{in}$

$$
v_{L}(t) = V_{in} - V_{out} = L \cdot i_{L}'(t)
$$
![[Pasted image 20240521200614.png]]

$$
i_{L}(t) = I_{S-} + \frac{V_{in} - V_{out}}{L} \cdot t
$$
![[Pasted image 20240521200631.png]]

# Switch Open

![[Pasted image 20240521200710.png]]

Assumption:
- $V_{out} = \text{const.}$

$$
v_{L}(t) = -V_{out} = L \cdot i_{L}'(t)
$$
![[Pasted image 20240521201658.png]]

$$
i_{L}(t) = I_{S+} - \frac{V_{out}}{L} \cdot t
$$
![[Pasted image 20240521201747.png]]

# Control Law

$$
\frac{V_{out}}{V_{in}} = \frac{t_{on}}{T_{S}} = d
$$
with
$$
T_{S} = t_{on} + t_{off} = \frac{1}{f_{c}}
$$

# Current-Time Area

$$
\Delta Q = \frac{1}{2} \cdot \frac{T_{S}}{2} \cdot \frac{\Delta I_{L}}{2}
$$
with
$$
\Delta I_{L} = \frac{V_{out}}{L} \cdot (1-d) \cdot T_{S}
$$

# Fluctuation of the Output Voltage

$$
\Delta V_{out} = \Delta V_{C}= \frac{\Delta Q}{C} = \frac{T_{S}^{2}}{8C} \cdot \frac{V_{out}}{L} \cdot (1-d)
$$