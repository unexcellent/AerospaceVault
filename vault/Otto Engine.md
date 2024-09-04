#uni/courses/thermo1 

The Otto engine is an [[Heat Engine|internal combustion engine]] using gasoline.

# Otto Cycle

## Steps

1. Intake
	- Piston from top dead center to bottom dead center
	- Fuel air mixture is sucked in

2. Compression
	- Piston moves from bottom dead center to top dead center and compresses [[States of Matter#Gas|gas]] mixture 
	- At highest point, ignition of mixture using a spark (spark ignition engine)

3. Power Stroke
	- Hot gas expands piston from top dead center to bottom dead center and transfers [[Thermodynamic Work|work]] to outside

4. Exhaust
	- Piston moves from bottom dead center to top dead center and pushes exhaust gases out

## Processes

![[Pasted image 20240819152606.png|400]]
Using idealisations, the engine processes can be presented by 6 basic [[Thermodynamic Process|thermodynamic processes]]: 
- **5 → 1**: [[Isobaric Process|Isobaric]] expansion (Fuel mixture intake) 
- **1 → 2**: [[Adiabatic Process|Adiabatic]], [[Thermodynamic Process#Reversible Process|reversible]] compression 
- **2 → 3**: [[Isochoric Process|Isochoric]] [[Heat Conduction|heat transfer]] into system (Combustion) 
- **3 → 4**: [[Adiabatic Process|Adiabatic]], [[Thermodynamic Process#Reversible Process|reversible]] expansion 
- **4 → 1**: [[Isochoric Process|Isochoric]] [[Heat Conduction|heat transfer]] out of the system 
- **1 → 5**: [[Isobaric Process|Isobaric]] compression (Exhaust venting)

# Efficiency

The maximum [[Thermal Efficiency]] of the Otto engine is 
$$
\eta_{th} = 1 - \left( \frac{V_{2}}{V_{1}} \right)^{\gamma - 1}
$$
-> $\eta_{th}$: [[Thermal Efficiency]]
-> $V_{1}$: [[Volume]] at stage 1
-> $V_{2}$: [[Volume]] at stage 2
-> $\gamma$: [[Isentropic Exponent]]