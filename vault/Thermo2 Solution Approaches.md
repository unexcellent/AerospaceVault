#uni/courses/thermo2 

# Kay's Rule

- given: partial volumes, mixture temperature, mixture pressure
- wanted: mixture volume using Kay's rule

1. read the component critical point temperatures from Table A-1
2. calculate reduced component pressures and temperatures via $T_{R,i} = \frac{T_{m}}{T_{cr,i}}$
3. read the component compressibility factor from the chart
4. calculate component mole fractions
5. calculate pseudo-critical temperature and pressure using $T'_{cr,m} = \sum y_{i} \cdot T_{cr,i}$ and $P'_{cr,m} = \sum y_{i} \cdot P_{cr,i}$
6. calculate reduced mixture pressure and temperature
7. read the mixture compressibility factor from the chart
8. calculate mixture volume using ideal gas equation

# Maximum Extractable Work During Combustion

## Using Gibbs Energy

9. Balance the reaction
10. Calculate the work using
$$
W_{rev} = \sum N_{R} \cdot \overline{g}^{\circ}_{f,R} - \sum N_{P} \cdot \overline{g}^{\circ}_{f,P}
$$

## Using The Generated Entropy

$$
W_{max} = X_{dest} = T_{0} \cdot S_{gen}
$$

# Entropy Generation During Combustion

11. Balance the reaction
12. Calculate the output heat using
$$
-Q_{out} = \sum N_{P} (\overline{h}^{\circ}_{f} + \overline{h} - \overline{h}^{\circ})_{P} - \sum N_{R} (\overline{h}^{\circ}_{f} + \overline{h} - \overline{h}^{\circ})_{R}
$$
13. Calculate the entropy for reactant and product
$$
S_{i} = N_{i} \cdot \big( \overline{s}^{\circ}_{i}(T, P_{0}) - R_{u} \cdot \ln(y_{i} \cdot \frac{P_{m}}{1\ atm}) \big)
$$
14. Calculate generated entropy using
$$
S_{gen} = S_{P} - S_{R} + \frac{Q_{out}}{T_{0}}
$$