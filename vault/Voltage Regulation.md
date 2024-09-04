#uni/courses/electrical 

# Ideal Voltage Source

The ideal [[Electrical Energy Source#DC Voltage Voltage Source|voltage source]] is defined by:
- has no internal [[Electrical Resistance|resistance]]
- the [[Voltage]] does not drop regardless of the load resistance

![[Pasted image 20240518151601.png|400]]

# Voltage Divider

-> [[Resistor#Voltage Divider]]

# Zener Diode

Voltage regulation using a [[Zener Diode]]
![[Pasted image 20240518151948.png]]

$$
V_{out} \approx V_{Z,0}
$$
$$
I_{Z} \approx -I_{BR} \cdot e^{\frac{-V_{Z} - V_{Z,0}}{n_{BR} \cdot V_{T}}} \quad \text{with } V_{Z} < 0, \ n_{BR} \approx 1
$$
$$
P_{D} \approx V_{Z,0} \cdot \left( \frac{V_{R}}{R} - I_{out} \right)
$$
-> $V_{Z,0}$: Zener [[Voltage]] as specified in the data sheet
-> $V_{Z}$: Cutoff region
-> $I_{BR}$: Breakdown current as specified in the data sheet
-> $n_{BR}$: Ideality factor
-> $V_T$: Thermal voltage
-> $P_{D}$: [[Electrical Power]] within the diode
-> $V_{R}$: [[Voltage]] across the [[Resistor]]
-> $R$: [[Electrical Resistance|Resistance]] of the resistor

![[Pasted image 20240518152723.png]]

# Zener Diode and Transistor

Addition of a [[Bipolar Junction Transistor]].
![[Pasted image 20240518153135.png]]

- Loss reduction during unloaded operation
- Improvement of the line regulation by a factor of $\beta$
- Improvement of the load regulation by a factor of $\beta$
- Nominal output voltage$V_{out} \approx V_{Z,0}-0.7V$
- Maximum output voltage without load comparatively high $V_{out,max} \approx V_{Z,0}$
- Minimum voltage drop (even at low load) to be considered $V_{R} \ge 0.7V$

# Power MOSFET

![[Pasted image 20240518153551.png|500]]

Investigation of losses using a [[MOSFET]] as a Unipolar Power Output Stage in linear operation:
- Input: $I_{out} = I_{D}$ controlled via $V_{GS}$
- Output: $V_{out} = R_{load} \cdot I_{D}$
- Power within $R_{load}$: $P_{load} = R_{load} \cdot I^{2}_{D}$
- [[Voltage]] across the MOSFET: $V_{DS} = V_{in} - R_{load} \cdot I_{D}$
- [[Electrical Power|Power]] within the MOSFET: $P_{loss} = I_{D} \cdot (V_{in} - R_{load} \cdot I_{D})$

![[Pasted image 20240518154223.png|500]]

Low-loss operating points of the [[MOSFET]] for:
- Open circuit ($I_{D} = 0$): $V_{DS} = V_{in}$
- Short circuit ($V_{DS} = 0$): $I_{SC} = I_D = \frac{V_{in}}{R_{load}}$

Beyond these operating points, high power dissipation results in the [[Semiconductor]].

# Half Bridge

![[Pasted image 20240518154644.png|400]]
-> $S_{B}$: Bottom switch
-> $S_{T}$: Top switch
-> $S=0$: Switch is open
-> $S=1$: Switch is closed

Very low-loss operation possible

Available voltage levels (neglecting the on-state resistance):
- if $S_{B} = 0$, $S_{T} = 0$ then $V_{out} \in [0, V_{in}]$
- if $S_{B} = 0$, $S_{T} = 1$ then $V_{out} = V_{in}$
- if $S_{B} = 1$, $S_{T} = 0$ then $V_{out} = 0$
- if $S_{B} = 1$, $S_{T} = 1$ then short circuit

## Loaded with LED and Resistor

![[Pasted image 20240518155237.png|500]]
![[Pasted image 20240518155326.png|450]]

- [[Light Emitting Diode|LED]] [[Voltage]] almost independent from [[Current|current]]
- High current fluctuations

## Loaded with LED and Inductor

![[Pasted image 20240518155701.png|500]]
![[Pasted image 20240518155740.png|450]]

Limited current slope:
$$
i_{LED}'(t) = \frac{v_{L}}{L}
$$
- if $S_{B} = 0$, $S_{T} = 1$ then $i_{LED}'(t) = \frac{V_{in} - V_{LED}}{L}$
- if $S_{B} = 1$, $S_{T} = 0$ then $i_{LED}'(t) = - \frac{V_{LED}}{L}$

## Loaded with Resistor and Inductor

![[Pasted image 20240518160219.png|450]]
![[Pasted image 20240518160244.png|450]]

### Current slope

$$
i_{out}'(t) = \frac{v_{out} - R \cdot i_{out}}{L}
$$
- Linear differential equation of 1st order
- Solution $i_{out}(t) = (i_{out}(0) - I_{out}) \cdot e^{-\frac{t}{\tau}} + I_{out}$
- if $S_{B} = 0$, $S_{T} = 1$ then $I_{out} = \frac{V_{in}}{R}$
- if $S_{B} = 1$, $S_{T} = 0$ then $I_{out} = 0$

### Transient Response

- Final value: $I_{avg} = \frac{V_{in}}{2R}$
- Current ripple: $\Delta I = I_{max} - I_{avg} = \frac{V_{in}}{2R} \cdot \frac{1-e^{-\frac{T_{S}}{2\tau}}}{1+e^{-\frac{T_{S}}{2\tau}}}$
- For $T_{S} << \tau$: $\Delta I \approx \frac{V_{in}}{8R} \cdot \frac{T_{S}}{\tau} = \frac{V_{in}}{8L} \cdot T_{S}$

### Pulse Width Modulation

- Duty cycle: $d$
- "On" Time: $t_{on} = d \cdot T_{S}$
- Target value: $I_{avg} = d \cdot \frac{V_{in}}{R}$
- Current ripple: $\Delta I = \frac{V_{in}}{R} \cdot (1-d) \cdot \frac{1-e^{-\frac{T_{S}}{2\tau}}}{1+e^{-\frac{T_{S}}{2\tau}}}$
- For $T_{S} << \tau$: $\Delta I \approx \frac{V_{in}}{2L} \cdot (1-d) \cdot d \cdot T_{S}$