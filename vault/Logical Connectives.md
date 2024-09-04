#uni/courses/math0 

Logical connectives combine/modify simple [[Mathematical Statements]] to create new ones.

# Negation

If $A$ is a statement, then $\neg A$ is the negation of $A$.

| $A$ | $\neg A$ |
| --- | -------- |
| 0   | 1        |
| 1   | 0        |

# And

If $A$ and $B$ are statements, then $A\wedge B$ means "$A$ and $B$".

| $A$ | $B$ | $A\wedge B$ |
| --- | --- | ----------- |
| 0   |  0   |       0      |
| 0   |   1  |       0      |
| 1   |  0   |        0     |
| 1    |  1   |     1        |

# Or

If $A$ and $B$ are statements, then $A\vee B$ means "$A$ or $B$".

| $A$ | $B$ | $A\vee B$ |
| --- | --- | ----------- |
| 0   |  0   |       0      |
| 0   |   1  |       1      |
| 1   |  0   |        1     |
| 1    |  1   |     1        |

# Exclusive Or

If $A$ and $B$ are statements, then $A\dot{\vee} B$ means "exclusively $A$ or $B$".

| $A$ | $B$ | $A\dot{\vee} B$ |
| --- | --- | ----------- |
| 0   |  0   |       0      |
| 0   |   1  |       1      |
| 1   |  0   |        1     |
| 1    |  1   |     0        |

# Implication

"$A\Rightarrow B$" means "if $A$ is true, then $B$ is true".

| $A$ | $B$ | $A\Rightarrow B$ |
| --- | --- | ----------- |
| 0   |  0   |       1      |
| 0   |   1  |       1      |
| 1   |  0   |        0     |
| 1    |  1   |     1        |

This operation is asymmetric -> $(A\Rightarrow B) \nRightarrow (B\Rightarrow A)$.

## Operations

- $(A \Rightarrow B) \Leftrightarrow (\neg B \Rightarrow \neg A)$

## Example

$(m, n \in \mathbb{N} \wedge m \text{ is even}) \Rightarrow m \cdot n \text{ is even}$

### Proof

Assume $m$, $n$ are natural numbers.
Then $m$ is even if $m = 2 \cdot x$ for some $x \in \mathbb{N}$. 
If you multiply by $n$, then $m \cdot n = 2 \cdot x \cdot n$ is also even.


# Equivalence

$A\Leftrightarrow B$ means "$A$ and $B$ have the same value".

| $A$ | $B$ | $A\Leftrightarrow B$ |
| --- | --- | ----------- |
| 0   |  0   |       1      |
| 0   |   1  |       0      |
| 1   |  0   |        0     |
| 1    |  1   |     1        |

## Operations

- $(A \Leftrightarrow B) \Leftrightarrow ((A \Leftrightarrow B) \wedge (B \Leftrightarrow A))$









