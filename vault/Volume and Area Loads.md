#uni/courses/mech1 

Volume and surface loads act continuously into/onto a volume/surface.

- [[Mechanical Beams|beams]] are one-dimensional structures - multidimensional loads are reduced to line loads
- [[Force|force]] density $\overrightarrow{f}(x)[\frac{N}{m}]$, $n(x)$ along beam axis, $q(x)$ across beam axis $\overrightarrow{f}(x) = \begin{pmatrix} n(x) \\  q(x) \end{pmatrix}$ 

- force density corresponds to one force per unit length
- infinitesimal single force at location $x$ is $d\overrightarrow{F}(x) = \overrightarrow{f}(x)dx$
$$
F_{Res} = \int^{\text{Load end}}_{\text{Load start}} dF = \int^{L_{e}}_{L_{s}} \overrightarrow{f}(x)dx
$$
![[Mechanical Beams 2023-11-09 09.05.10.excalidraw]]
$$
M_{Res} = F_{Res,z} \cdot a = \int^{L_{e}}_{L_{s}} x \cdot dF_{z} = \int^{L_{e}}_{L_{s}} x \cdot q(x) dx
$$