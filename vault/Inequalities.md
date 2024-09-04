#uni/courses/math0 

In addition to identities, inequalities play an essential role in math, we have:
- $x \lt y$, $x \gt y$: strict inequalities
- $x \le y$, $x \ge y$: non-strict inequalities

# Order Properties

- Reflexivity: $x \le x \hspace{10pt} \forall x \in \mathbb{R}$
- Transitivity: $\forall x,y,z \in \mathbb{R}: (x \le y \wedge y \le z) \Rightarrow x \le z$
- Antisymmetry: $\forall x,y \in \mathbb{R}: (x \le y \wedge y \le x) \Rightarrow x = z$
- Totality: $\forall x,y \in \mathbb{R}: x \le y \vee x \le y$

In Practice, one often encounters inequalities of the form $f(x) \le 0$ involving [[Function|functions]] $f : \mathbb{R}^n \rightarrow \mathbb{R}, n \in \mathbb{N}$ and is interested in the solution [[Set|set]]: $\mathbb{L} := \{x \in \mathbb{R}^n | f(x) \le 0\}$.

To solve such inequalities, one uses the following properties.
- $a \lt b, c \in \mathbb{R} \Rightarrow a + c \lt b + c$
- $(a \lt b \wedge c \lt d) \Rightarrow a \cdot c \lt b \cdot d$
- $(a \lt b \wedge c \gt 0) \Rightarrow a \cdot c \lt b \cdot c$
- $(0 \lt a \lt b \wedge 0 \lt c \lt d) \Rightarrow a \cdot c \lt b \cdot d$
- $(a \lt b \wedge c \lt 0) \Rightarrow a \cdot c \gt b \cdot c$
- $0 \lt a \lt b \Rightarrow \frac{1}{a} \gt \frac{1}{b}$

# Example

For all $a, b \ge 0$, we have geometric mean less or equal to arithmetic mean.
-> $\sqrt{a \cdot b} \le \frac{a + b}{2}$

## Proof

$\sqrt{a \cdot b} \le \frac{a + b}{2}$
$\Leftrightarrow (\sqrt{a \cdot b})^2 \le (\frac{a + b}{2})^2$
$\Leftrightarrow (\sqrt{a \cdot b})^2 \le (\frac{a + b}{2})^2$
$\Leftrightarrow a \cdot b \le \frac{1}{4} (a^2+2ab+b^2)$
$\Leftrightarrow 4ab \le a^2+2ab+b^2$
$\Leftrightarrow 0 \le a^2-2ab+b^2$
$\Leftrightarrow 0 \le (a-b)^2$
