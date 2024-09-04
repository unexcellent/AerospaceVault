#uni/courses/thermo1 

Aircraft Engines are [[Brayton Cycle#Open Brayton Cycle|open Brayton cycle]] engines with additional features.
![[Pasted image 20240821114233.png]]

- Diffuser in front of the engine that slows down the airflow to [[Stagnation Point|stagnation]] 
- Turbine produces exactly the amount of [[Thermodynamic Work|work]] needed by the compressor 
- Additional [[Pressure]] after turbine is used in nozzle to accelerate flow to faster than input $c_{0}$
- Speed differential in flow $c_{5} - c_{0}$ causes thrust

# Diffusers and Nozzles

Diffusers and Nozzles convert flow velocity into [[Temperature]] and [[Pressure]] and vice versa
- diffusers and nozzles are considered [[Thermodynamic System#Steady System|steady]], [[Adiabatic Process|adiabatic]] and do not perform work
- change of cross sectional area leads to change of velocity for a constant mass flow rate $$\dot{m} = \rho_{in} \cdot c_{in} \cdot A_{in} = \rho_{out} \cdot c_{out} \cdot A_{out}$$
- change in velocity leads to change in enthalpy $$0 = \left( h_{in} + \frac{c_{in}^{2}}{2} \right) - \left( h_{out} + \frac{c_{out}^{2}}{2} \right)$$
- for [[Ideal Gas|ideal gasses]] $$ T_{out} = T_{in} + \frac{c_{in}^{2} - c_{out}^{2}}{2 c_{p}}$$
- if assumed [[Isentropic Process|isentropic]] $$p_{out} = p_{in} \cdot \left( \frac{T_{out}}{T_{in}} \right)^{\frac{\gamma}{\gamma-1}}$$
# Aircraft Engine Cycle

![[Pasted image 20240821120202.png|400]]

## Net Work

$$
|w_{net}| = w_{T} = w_{C} = (h_{4} - h_{5}) - (h_{1} - h_{0})
$$
-> $w_{T}$: [[Thermodynamic State#Specific Property|specific]] turbine [[Thermodynamic Work|work]]
-> $w_{C}$: [[Thermodynamic State#Specific Property|specific]] compressor [[Thermodynamic Work|work]]
-> $h$: [[Thermodynamic State#Specific Property|specific]] [[Enthalpy]]

## Energy Balance Diffuser

$$
h_{1} - h_{0} = \frac{c_{0}^{2}- c_{1}^{2}}{2}
$$
-> $h$: [[Thermodynamic State#Specific Property|specific]] [[Enthalpy]]
-> $c$: flow velocity

## Energy Balance Nozzle

$$
h_{5} - h_{4} = \frac{c_{4}^{2}- c_{5}^{2}}{2}
$$
-> $h$: [[Thermodynamic State#Specific Property|specific]] [[Enthalpy]]
-> $c$: flow velocity

# Efficiency

The maximum [[Thermal Efficiency]] is
$$
\eta_{th} = 1 - \frac{1}{\left( \frac{p_{2}}{p_{0}} \right)^\frac{\gamma - 1}{\gamma}}
$$
-> $p$: [[Pressure]]
-> $\gamma$: [[Isentropic Exponent]]