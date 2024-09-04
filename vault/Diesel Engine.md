#uni/courses/thermo1 

The Diesel engine is an [[Heat Engine|internal combustion engine]] using diesel.

# Diesel Cycle

## Steps

1. Intake 
	- Piston from top dead center to bottom dead centre
	- Pure air is sucked in 
	
2. Compression 
	- Piston moves from bottom dead centre to top dead center and compresses the air 
	- At highest point, fuel is injected and auto-ignites 
	
3. Power stroke 
	- Hot gas expands piston from top dead center to bottom dead centre and transfers work to outside 
	
4. Exhaust 
	- Piston moves from bottom dead centre to top dead center and pushes exhaust gases out

## Processes

![[Pasted image 20240819162531.png|400]]
Using idealisations, the engine processes can be presented by 6 basic [[Thermodynamic Process|thermodynamic processes]]:

- **5 → 1**: [[Isobaric Process|Isobaric]] expansion (Air intake) 
- **1 → 2**: [[Adiabatic Process|Adiabatic]], [[Thermodynamic Process#Reversible Process|reversible]] compression 
- **2 → 3**: [[Isobaric Process|Isobaric]] [[Heat Conduction|heat transfer]] into system (fuel injection and combustion) 
- **3 → 4**: [[Adiabatic Process|Adiabatic]], [[Thermodynamic Process#Reversible Process|reversible]] expansion 
- **4 → 1**: [[Isochoric Process|Isochoric]] [[Heat Conduction|heat transfer]] out of the system 
- **1 → 5**: [[Isobaric Process|Isobaric]] compression (Exhaust venting)

# Efficiency

The maximum [[Thermal Efficiency]] of the Diesel engine is
$$
n_{th} = 1- \left( \frac{V_{2}}{V_{1}} \right)^{\gamma-1} \cdot \left( \frac{\alpha^\gamma}{\gamma \cdot \left( \alpha-1 \right)} \right)
\quad \text{with} \quad
\alpha = \frac{V_{3}}{V_{2}}
$$
-> $V$: [[Volume]]
-> $\gamma$: [[Isentropic Exponent]]
-> $\alpha$: Cutoff ratio