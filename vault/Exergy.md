#uni/courses/thermo1 

Symbol: $Ex$
Unit: $J$

The exergy of [[Heat]] as well as all [[Thermodynamic Work|work]] and energy forms, is the part that is, at least in principle, capable of doing work or being transformed into work.
$$
Ex_{q} = \int \frac{T_{in}-T_{out}}{T_{in}} \ dQ_{in} = \frac{T_{in} - T_{out}}{T_{in}} \cdot Q_{in}
$$
-> $T_{in}$: [[Temperature]] inside the system
-> $T_{out}$: [[Temperature]] outside the system
-> $Q_{in}$: [[Heat]] in the system

# Open System

$$
\dot{Ex}_{h} = \dot{m} \cdot \big( (h_{in} - h_{out}) - T_{out} (s_{in} - s_{out}) \big)
$$
-> $\dot{m}$: [[Mass]] flow
-> $h_{in}$: [[Thermodynamic State#Specific Property|specific]] [[Heat]] inside the system
-> $h_{out}$: [[Thermodynamic State#Specific Property|specific]] [[Heat]] outside the system
-> $T_{out}$: [[Temperature]] outside the system
-> $s_{in}$: [[Thermodynamic State#Specific Property|specific]] [[Entropy]] inside the system
-> $s_{out}$: [[Thermodynamic State#Specific Property|specific]] [[Entropy]] outside the system

# Closed System

$$
Ex_{u} = U_{in} - U_{out} - T_{out}(S_{in} - S_{out}) + p_{out} (V_{in} - V_{out})
$$
-> $U_{in}$: [[Internal Energy]] inside the system
-> $U_{out}$: [[Internal Energy]] outside the system
-> $T_{out}$: [[Temperature]] outside the system
-> $S_{in}$: [[Entropy]] inside the system
-> $S_{out}$: [[Entropy]] outside the system
-> $p_{out}$: [[Pressure]] outside the system
-> $V_{in}$: [[Volume]] inside the system
-> $V_{out}$: [[Volume]] outside the system

# Exergy Loss

$$
ex_{loss} = T_{out} \cdot s_{irr}
$$
-> $T_{out}$: [[Temperature]] outside the system
-> $s_{irr}$: [[Thermodynamic Process#Irreversible Process|irreversible]] [[Thermodynamic State#Specific Property|specific]] [[Entropy]] 