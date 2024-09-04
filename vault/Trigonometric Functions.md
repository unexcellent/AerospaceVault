#uni/courses/math0 

Using similarity, we can reduce the study of right-angled triangles to a prototypical situation.
Consider a circle of radius 1.
- area of the circle $= \pi$
- circumference $=2 \pi$

The trigonometric functions are produced by similarity of all [[Triangles#Right-Angled Triangles|right-angled triangles]].

# Sine

$$
\sin \rho = \frac{\text{length of opposite cathetus}}{\text{length of hypothenuse}}
$$

![[Drawing 2023-10-08 13.51.46.excalidraw]]

```functionplot
---
xLabel: x in pi
yLabel: y
bounds: [-2, 2, -1.5, 1.5]
grid: true
color: blue
---
g(x)=sin(x * PI)
```

## Roots

| Angle | $\sin$ Angle         |
| ----- | -------------------- |
| $0º$  | $0$                  |
| $30º$ | $\frac{1}{2}$        |
| $45º$ | $\frac{1}{\sqrt{2}}$ |
| $60º$ | $\frac{\sqrt{3}}{2}$ |
| $90º$ | $1$                  |

# Cosine

$$
\cos \rho = \frac{\text{length of adjacent cathetus}}{\text{length of hypothenuse}}
$$

![[Trigonometric Functions 2023-10-08 13.52.49.excalidraw]]

```functionplot
---
xLabel: x in pi
yLabel: y
bounds: [-2, 2, -1.5, 1.5]
grid: true
---
g(x)=cos(x * PI)
```
## Roots

| Angle | $\cos$ Angle         |
| ----- | -------------------- |
| $0º$  | $1$                  |
| $30º$ | $\frac{\sqrt{3}}{2}$        |
| $45º$ | $\frac{1}{\sqrt{2}}$ |
| $60º$ | $\frac{1}{2}$         |
| $90º$ | $0$                  |

# Tangens

$$
\tan \rho = \frac{\text{length of opposite cathetus}}{\text{length of adjacent cathetus}}
$$
![[Trigonometric Functions 2023-10-08 13.56.05.excalidraw]]

```functionplot
---
xLabel: x in pi
yLabel: y
bounds: [-2, 2, -1.5, 1.5]
grid: true
---
g(x)=tan(x * PI)
```

## Roots

| Angle | $\tan$ Angle  |
| ----- | ------------- |
| $0º$  | $0$           |
| $30º$ | $\frac{1}{\sqrt{3}}$ |
| $45º$ | $1$           |
| $60º$ | $\sqrt{3}$    |
| $90º$ | $-$           |

# Cotangens

$$
\cot \rho = \frac{\text{length of adjacent cathetus}}{\text{length of opposite cathetus}}
$$

![[Trigonometric Functions 2023-10-08 13.53.32.excalidraw]]
```functionplot
---
xLabel: x in pi
yLabel: y
bounds: [-2, 2, -1.5, 1.5]
grid: true
---
g(x)=1 / tan(x * PI)
```

# Basic Properties

## Periodicity

$\forall x \in \mathbb{R}, k \in \mathbb{Z}:$
- $\sin(x+k \cdot 2\pi) = \sin(x)$ 
- $\cos(x+k \cdot 2\pi) = \cos(x)$
- $\tan(x+k \cdot 2\pi) = \tan(x)$
- $\cot(x+k \cdot 2\pi) = \cot(x)$

## Zeros (Minkowski Notation)

- $\{x \in \mathbb{R} | \sin x = 0\} = \{\pi \cdot k | k \in \mathbb{Z}\} = \pi \mathbb{Z}$
- $\{x \in \mathbb{R} | \cos x = 0\} = \frac{\pi}{2} + \pi \mathbb{Z}$
- $\{x \in \mathbb{R} | \tan x = 0\} = \{\pi \cdot k | k \in \mathbb{Z}\} = \pi \mathbb{Z}$
- $\{x \in \mathbb{R} | \cot x = 0\} = \frac{\pi}{2} + \pi \mathbb{Z}$

## Symmetry

- $\sin(-x) = -\sin x$ <- odd
- $\cos x = \cos(-x)$ <- even
- $\tan(-x) = -\tan x$ <- odd
- $\cot x = \cot(-x)$ <- even

## [[Theorem of Pythagoras]]

$\sin^2 x + \cos^2 x = 1$

## Translation

- $\sin(x + \frac{\pi}{2}) = \cos(x)$
- $\cos(x + \frac{\pi}{2}) = \sin(x)$

## Addition Formula

- $\sin(x+y) = \sin x \cdot \cos y + \cos x \cdot \sin y$
- $\cos(x+y) = \cos x \cdot \cos y - \sin x \cdot \sin y$
- $\tan(x+y) = \frac{\tan x + \tan y}{1 - \tan x \cdot \tan y}$

# Laws from the General [[Triangles|Triangle]]

![[Pasted image 20231008141846.png]]

## Area Formula

- $A = \frac{1}{2} \cdot a \cdot b \cdot \sin \gamma$
- $A = \frac{1}{2} \cdot b \cdot c \cdot \sin \alpha$
- $A = \frac{1}{2} \cdot a \cdot c \cdot \sin \beta$

## Law of Sines

$\frac{a}{\sin \alpha} = \frac{b}{\sin \beta} = \frac{c}{\sin \gamma}$

## Law of Cosines

- $a^2 = b^2 + c^2 - 2bc \cos \alpha$
- $b^2 = a^2 + c^2 - 2ac \cos \beta$
- $c^2 = a^2 + b^2 - 2ab \cos \gamma$

# Inverse Trigonometric Functions

Consider: 
- $\sin : [-\frac{\pi}{2}, \frac{\pi}{2}] \rightarrow [-1, 1]$
- $\cos : [0, \pi] \rightarrow [-1, 1]$

-> With this choice of domain and codomain, $\sin$ and $\cos$ are bijective and have inverse functions

-> We denote these inverse functions by $\arcsin$ and $\arccos$
- $\arcsin: [-1, 1] \rightarrow [-\frac{\pi}{2}, \frac{\pi}{2}], y \mapsto x$ with $\sin x = y$
- $\arccos: [-1, 1] \rightarrow [0, \pi], y \mapsto x$ with $\cos x = y$

=> The same holds true for $\tan$ and $\cot$