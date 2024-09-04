#uni/courses/materials 

Methods for [[Material Testing|testing]] the [[Hardness]] of a [[Material]].

Hardness is usually tested by creating a small indention with a indenter.

![[Pasted image 20240604140039.png]]

# Methods

## Brinell

Indention via a 10mm sphere of steel or tungsten carbide

![[Pasted image 20240604140843.png]]

The hardness is calculated via
$$
\text{HBW} = \frac{2P}{\pi \cdot D \cdot (D - \sqrt{D^{2} - d^{2}})}
$$
-> $P$: load
-> $D$: diameter of the sphere
-> $d$: diameter of the indention

![[Pasted image 20240604141346.png]]

### Advantages
- Determination of a medium hardness at heterogeneous materials

### Disadvantages
- Not applicable to thin materials and layers ($s \ge 8 \cdot h$) 
- Very hard materials (test load becomes too large)

## Vickers

Indention via a diamond pyramid

![[Pasted image 20240604140854.png]]

The hardness is calculated via
$$
HV = 1.854 \cdot \frac{P}{d^{2}_{1}}
$$
-> $P$: load
-> $d_{1}$: diagonal length of the pyramid base

![[Pasted image 20240604141551.png]]

### Advantages
- Applicable to a wide range of materials (from soft to very hard) 
- Also for thin plates / specimens
- More precise compared to Brinell due to pyramidal imprint

## Knoop

Indention via a diamond pyramid

![[Pasted image 20240604141043.png]]

The hardness is calculated via
$$
HV = 1.854 \cdot \frac{P}{d^{2}_{1}}
$$
-> $P$: load
-> $l$: diagonal length of the long side of the pyramid

## Rockwell

Indention via a diamond cone

![[Pasted image 20240604141155.png]]


### Advantages
- Quick and automate-able

### Disadvantages
- Small indenter, sensitive to local effects
- Reduced accuracy at high hardness
- Various scales
