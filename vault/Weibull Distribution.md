#uni/courses/materials 

Symbol: $P_{f}$
Unit: $1$

Metric for characterizing the failure chance of a [[Ceramic Material]] under [[Stress|stress]].

Due to a high rate of imperfections, even ceramics without pores have a high scatter of failure at different tension levels.

![[Pasted image 20240616125938.png]]
$$
P_{f}(\sigma_{fs}) = 1 - e^{-\frac{V}{V_{0}} \cdot \left( \frac{\sigma_{fs} - \sigma_{u}}{\sigma_{o}} \right)^{m}}
$$
-> $V$: loaded volume
-> $V_{0}$: reference volume
-> $\sigma_{fs}$: [[Flexure Strength]]
-> $\sigma_{u}$: minimum tension
-> $\sigma_{o}$: scaling tension
-> $m$: Weibull modulus ([[Material]] property)