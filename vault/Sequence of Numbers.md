#uni/courses/math1 

A sequence is a [[Function|map]] from $\mathbb{N}$ to $\mathbb{R}$: $n \in \mathbb{N} \mapsto a_{n} \in \mathbb{R}$ ($n$ is associated to $a_{n}$). It is denoted by $(a_{n})_{n \in \mathbb{N}}$ or simplified ($a_{n}$).

# Bounds

![[Pasted image 20231220092650.png]]

A sequence $(a_{n})$ is **bounded above** if $\exists M \in \mathbb{R}: a_{n} \le M \quad \forall n \in \mathbb{N}$

A sequence $(a_n)$ is **bounded below** if $\exists m \in \mathbb{R}: a_{n} \ge m \quad \forall n \in \mathbb{N}$

If a sequence is bounded above and below we just say that it is **bounded**.

# Asymptotic Behavior

Some sequences converge or diverge for very large $n$.
If a sequence converges or diverges, it is called **regular**.

## Converging Sequences

If a sequence $(a_{n})$ approaches a finite number $a$ for very large $n$ it is called convergent.
$$
\displaystyle{\lim_{n \to \infty}} a_{n} = a
$$

Example: $(a_{n}) = \frac{1}{n}$ -> $\displaystyle{\lim_{n \to \infty}} a_{n} = 0$

### Rules

- If $\sum\limits_{k=1}^{\infty} a_{k} \in \mathbb{R}$ then $\lim a_{k} = 0$.
- -> [[D'Alembert Criterion]] for increasing sequences
- -> [[Leibniz Test]] for decreasing sequences

## Diverging Sequences

If a sequence $(a_{n})$ approaches plus or minus infinity it is called divergent.
$$
\displaystyle{\lim_{n \to \infty}} a_{n} = \pm \infty
$$
Example: $(a_{n}) = n$ -> $\displaystyle{\lim_{n \to \infty}} a_{n} = \infty$

## Non-Regular Sequences

Example: $(a_{n}) = (-1)^{n}$

# Monotonicity

All monotone sequences are [[Sequence of Numbers#Asymptotic Behavior|regular]].

## Monotone Increasing Sequences

A sequence $(a_{n})$ is called **monotone increasing** if all subsequent values of the sequence are larger or equal to the ones before.
$$
a_{n+1} \ge a_{n} \quad \forall n \in \mathbb{N}
$$

## Monotone Decreasing Sequences

A sequence $(a_{n})$ is called **monotone decreasing** if all subsequent values of the sequence are smaller or equal to the ones before.
$$
a_{n+1} \le a_{n} \quad \forall n \in \mathbb{N}
$$

# Supremum

The supremum of a sequence $\sup (a_{n})$ is the smallest possible [[Sequence of Numbers#Bounds|upper bound]].

If it is part of the sequence, it is called the maximum $\max (a_{n})$.

# Infimum

The infimum of a sequence $\inf (a_{n})$ is the largest possible [[Sequence of Numbers#Bounds|lower bound]].

If it is part of the sequence, it is called the minimum $\min (a_{n})$.

# Cauchy Sequence

A Cauchy sequence is a sequence whose terms become very close to each other as the sequence progresses.
$$
\forall \varepsilon > 0 \quad \exists n,m > 0: |a_{n} - a_{m}| < \varepsilon
$$

# Special Sequences

$\sum\limits_{k=1}^{\infty} \frac{1}{k}$ -> harmonic series

$\sum\limits_{k=1}^{\infty} \frac{1}{k^{\alpha}}$ -> generalized harmonic series

$\sum\limits_{k=1}^{\infty} \frac{(-1)^{k}}{k}$ -> alternating harmonic series

$\sum\limits_{k=1}^{\infty} \frac{1}{k}$ -> harmonic series
