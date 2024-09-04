#uni/courses/electrical 

A kind of [[Transistor]].

Circuit symbol:
![[Pasted image 20231222172408.png|150]]

# Operating Principle

- BJTs correspond in their structure to two [[Semiconductor#P-N Junction|p-n junctions]]
- Depending on their structure, a distinction is made between n-p-n and p-n-p types:

![[Pasted image 20231222172606.png]]

The bipolar transistor can be operated in three ways:
- emitter circuit (the most common type, as it is particularly suitable for amplifier circuits),
- collector circuit (high input [[Electrical Resistance|resistance]] with low output [[Electrical Resistance|resistance]]) or
- base circuit (low input [[Electrical Resistance|resistance]] with high output [[Electrical Resistance|resistance]]).

The function of the transistor is explained using the emitter circuit of an npn bipolar transistor:

![[Pasted image 20231222173439.png|250]]

- Initially, there is only a positive voltage between the collector and the emitter $V_{CE} > 0$.
- The transistor is in reverse mode. No current can flow through the collector and base: $I_C = 0$.
- If now a positive base-emitter voltage $V_{BE} > 0$ is applied, which exceeds the diffusion voltage of the transistor (for silicon transistors at $V_{D} = 0.7 V$), a current starts to flow through collector and emitter, i. e. the transistor turns conductive.

The current through the transistor depends on the base-collector voltage and the base current and corresponds to the following characteristic diagram:

![[Pasted image 20231222173643.png]]

![[Pasted image 20231222173712.png]]

- The output characteristic field can be divided into three areas:
	- Saturation area
	- Linear range
	- Breakdown area
- When designing the circuit, make sure to operate the transistor in the saturation region.

- The main characteristic of a BJT transistor can be described as the current multiplication of the base current $I_B$ with the collector current $I_C$.
- In normal operation, $I_B ≪ I_C$.
- The current gain of a transistor corresponds to the ratio of the collector current $I_C$ to the base current $I_B$ and is defined as the gain factor $β = \frac{d I_{C}}{dI_{B}}$. 
- Typical values for $β$ range from $10–250$.
- Note: $V_{CE}$ assumed constant.