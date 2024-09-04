#uni/courses/math0 
#uni/courses/math1 

A "statement" is an expression, that is either **true** or **false**.

# Examples

- "It is raining"
- "$x = 5$"
- "The Naview-Stokes-Equations have a unique solution in three dimensions."

# Main Purpose of Math

Formulation of Statements and assessing whether certain statements are **true** or **false**.

# Proof by Contradiction

We want to prove a statement $S$

- Assume (by contradiction), that $S$ is false
- If we obtain by logic deduction that some triviality is false (this is the contradiction)
- Then the problem of the false deduction is the starting point

## Example

There is no rational number, where the square is equal to 2.
-> $\nexists d \in \mathbb{Q}: d^{2}= 2$

Contradiction: assume $\exists d \in \mathbb{Q}: d^{2}= 2$

->  $d = \frac{p}{q}$ with $p \in \mathbb{Z}, q \in \mathbb{N}$

Assume without loss of generality that p and q are co-prime

-> $(\frac{p}{q})^{2} = 2 \Leftrightarrow p^{2} = 2 \cdot q^{2}$

-> $p^{2}$ is even -> $p$ is even -> $p = 2m$

-> $(2m)^{2} = 2 \cdot p^{2} = 2^{2}m^{2} \Leftrightarrow 2 m^{2} = q^{2}$

-> $q^{2}$ is even -> $q$ is even

-> $p$ and $q$ can not be co-primes because they have the common factor $2$

=> There can not be a rational number, that squares to $2$