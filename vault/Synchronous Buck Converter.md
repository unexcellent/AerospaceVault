#uni/courses/electrical 

[[Current]] containing a switch, an [[Inductor]], a [[Capacitor]] and a [[Diode]] used for [[DC-DC Conversion]].

![[Pasted image 20240521202812.png]]

- if $S=1$, $\bar{S}=0$, then $v_{SW}=V_{in}$ 
- if $S=0$, $\bar{S}=1$, then $v_{SW}=0$

![[Pasted image 20240521203624.png]]

Assumptions:
- $v_{SW} = 0$
- $i_{out} = 0$
- $v_{C}(t=0)=25V$
- $i_{L}(t=0)=0$

$$
i_{L}'(t) = \frac{v_{L}}{L} = \frac{v_{SW} - R_{L} \cdot i_{L} - v_{C}}{L}
$$
$$
v_{C}'(t) = \frac{i_{C}}{C} = \frac{i_{L} - i_{out}}{C}
$$

# Light Dampening

![[Pasted image 20240521204055.png|600]]
![[Pasted image 20240521204117.png|600]]
![[Pasted image 20240521204140.png|600]]

# Medium Dampening

![[Pasted image 20240521204320.png|600]]
![[Pasted image 20240521204337.png|600]]
![[Pasted image 20240521204349.png|600]]

# High Dampening

![[Pasted image 20240521204438.png|600]]
![[Pasted image 20240521204452.png|600]]
![[Pasted image 20240521204508.png|600]]