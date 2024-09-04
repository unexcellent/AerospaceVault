#uni/courses/math1 

Are a [[Set|set of numbers]] denoted by $\mathbb{C}$, which stem from solving [[Polynomial and Rational Functions|polynomial]] equations (solve $x^{2} + 1 = 0$).
Since $\sqrt{-1}$ is not defined in the real numbers, we introduce the imaginary unit $i = \sqrt{-1}$.
A complex number $a$ has a real part $a_{r} \in \mathbb{R}$ and an imaginary part $a_{i} \in \mathbb{R}$ with $a = (a_{r}, a_{i}) = a_{r} + i \cdot a_{i}$

# Geometric Form

Given $a \in \mathbb{C}$
![[Complex Numbers 2023-12-22 14.30.51.excalidraw]]
$$
a = (|a| \cdot \cos \alpha, |a| \cdot \sin \alpha ) = |a| \cdot (\cos \alpha , i \cdot \sin \alpha )
$$
$$
\alpha = \tan^{-1}\left(\frac{a_{i}}{a_{r}}\right)
$$

# Exponential Form

Given $\alpha \in \mathbb{R}$, the Euler formula states
$$
e^{i \alpha} = \cos \alpha + i \cdot \sin \alpha
$$
-> $e$: Euler's number
-> $\alpha$: angle of a complex number

A complex number $a$ can therefore be written as:
$$
a = |a| \cdot e^{i \alpha} = |a| \cdot e^{i \cdot \tan^{-1}\left(\frac{a_{i}}{a_{r}}\right)}
$$

# Operations

## Adding two Complex Numbers

Given $a, b \in \mathbb{C}$
$$
(a_{r}, a_{i}) + (b_{r}, b_{i}) = (a_{r} + b_{r}, a_{i} + b_{i})
$$

## Multiplying by a Real Number

Given $a \in \mathbb{C}$, $\lambda \in \mathbb{R}$
$$
\lambda \cdot (a_{r}, a_{i}) = (\lambda \cdot a_{r}, \lambda \cdot a_{i})
$$

## Multiplying two Complex Numbers

Given $a, b \in \mathbb{C}$
$$
a \cdot b = (a_{r} \cdot b_{r} - a_{i} \cdot b_{i}) + i(a_{r} \cdot b_{i} + a_{i} \cdot b_{r})
$$

### From the Geometric Form

Given $a = |a| \cdot (\cos \alpha, i \cdot \sin \alpha)$, $b = |b| \cdot (\cos \beta, i \cdot \sin \beta)$
$$
a \cdot b = |a|\cdot|b| \cdot ( \cos (\alpha + \beta), i \cdot \sin(\alpha + \beta)) 
$$

## Modulus

Defines the distance of a complex number to the origin. Based on the [[Vector#Euclidian Length|euclidian length of vectors]].

Given $a, b \in \mathbb{C}$
$$
|a| = \sqrt{a_{r}^{2} + a_{i}^{2}}
$$

### Properties

- $|a \cdot b| = |a| \cdot |b|$

## Conjugate

Mirrors the complex number on the real axis.

Given $a,b \in \mathbb{C}$
$$
\overline{a} = a_{r} - i \cdot a_{i}
$$

### Properties

- $a \cdot \overline{a} = a_{r}^{2} + a_{i}^{2} = |a|^{2}$
- $a^{-1} = \frac{\overline{a}}{|a|^{2}}$
- $\overline{\overline{a}} = a$
- $\overline{a + b} = \overline{a} + \overline{b}$
- $\overline{a \cdot b} = \overline{a} \cdot \overline{b}$

## Powers of Complex Numbers

Given $a = |a| \cdot e^{i \alpha}$, $n \in \mathbb{R}$
$$
a^{n}= |a|^{n} \cdot e^{i \cdot n \cdot \alpha} 
$$