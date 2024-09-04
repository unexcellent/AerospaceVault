#uni/courses/math0 #uni/courses/math1 

A collection of well-defined, distinct object is called a set. The objects contained in the set are called elements.

# Basic Numerical Sets

- $\mathbb{P}$: prime numbers
- $\mathbb{N}$: natural numbers (defined by [[Peano Axioms]])
- $\mathbb{N}_0$: natural numbers and zero
- $\mathbb{Z}$: integers
- $\mathbb{Q}$: rational numbers -> $\mathbb{Q} := \{\frac{p}{q}, p \in \mathbb{Z}, q \in \mathbb{N}\}$
- $\mathbb{R}$: real numbers (defined by [[Dedekind Completeness Axiom]])
- $\mathbb{C}$: complex numbers

# Describing a Set

- Explicit definition (writing all elements out)
	- Example: $A := \{a, b, c, d\}$
- Characterization by properties
	- Example: $\mathbb{Q} := \{x \in \mathbb{R} | \exists q \in \mathbb{N}: q \cdot x \in \mathbb{Z}\}$

# Intervals

Let $a,b \in \mathbb{R}$, we define
- $[a, b] := \{s\in \mathbb{R}|a\leq s \leq b\}$
- $(a, b] := \{s\in \mathbb{R}|a\lt s \leq b\}$
- $[a, b) := \{s\in \mathbb{R}|a\leq s \lt b\}$
- $(a, b) := \{s\in \mathbb{R}|a\lt s \lt b\}$

# Basic Operations and Notations

- $a \in B$: $a$ is an element of $B$
- $a \notin B$: $a$ is not an element of $B$
- $A \subseteq B$: $A$ is a subset of $B$ -> $a \in A \Rightarrow a \in B$
- $A \not\subset B$: $A$ is not a subset of $B$ -> $\exists a \in A: a \notin B$
- $A \subset B$: $A$ is a proper subset of $B$ -> $(A \subset B) \wedge (A \neq B)$
- $A = B$: $A$ is equal to $B$ -> $(A \subset B) \wedge (B \subset A)$
- $A \cup B$: Union of $A$ and $B$ -> $A \cup B := \{x|x\in A \vee x \in B\}$
- $A \cap B$: Intersection of $A$ and $B$ -> $A \cap B := \{x|x\in A \wedge x \in B\}$
- $A \backslash B$: $A$ without $B$ -> $A\backslash B:= \{x\in A | x \notin B\}$
- $C_A(B)$: Context of $A$ and $B$ -> $A\backslash B$ in the situation $B \subset A$
- $|A|$: Cardinality of $A$ (number of elements)
- $A \times B$: Cartesian Product of ordered tuples -> $A \times B := \{(a, b)|a\in A, b \in B\}$
- $\emptyset$: Empty set
- Disjoint: Two sets $A$ and $B$ are disjoint if $A \cap B = \emptyset$
- $\mathcal{P}(A)$: Powerset of $A$ (set of all subsets of A)
	- Example: $A = \{a, b, c\}$
		- $\mathcal{P}(A) = \{ \{\}, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, \{a, b, c\}  \}$

## Iterative Operations

- $\bigcup\limits_{i=1}^{n} A_i := A_1 \cup A_2 \cup A_3 \cup \dots \cup A_n$ 
- $\bigcap\limits_{i=1}^{n} A_i := A_1 \cap A_2 \cap A_3 \cap \dots \cap A_n$ 

## Calculus Rules

- Commutativity:
	- $A \cup B = B \cup A$
	- $A \cap B = B \cap A$

- Associativity:
	- $A \cup (B \cup C) = (A \cup B) \cup C$
	- $A \cap (B \cap C) = (A \cap B) \cap C$

- Distributivity:
	- $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
	- $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$

- Demorgan:
	- $C \backslash (A \cup B) = (C \backslash A) \cap (C \backslash B)$
	- $C \backslash (A \cap B) = (C \backslash A) \cup (C \backslash B)$

- Cardinality:
	- $|A \times B | = |A| \cdot |B|$
	- $|A \cup B | = |A| + |B| - |A \cap B|$
	- $|A \backslash B | = |A| - |A \cap B|$