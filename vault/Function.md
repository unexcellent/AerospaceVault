#uni/courses/math0 
#uni/courses/math1 

# Definition

Let $X$, $Y$ be non-emtpy [[Set|sets]]. A function $f$ from $X$ to $Y$ is a rule, that assigns to each element of $X$ a unique element of set $Y$. -> $\forall x \in X \hspace{5pt} \exists_1 y \in Y: y = f(x)$

# Notation

$f: X \rightarrow Y, x \mapsto f(x)$

Let $f: X \rightarrow Y$ be a function between non-empty sets $X$ and $Y$ then:
- $X$ is called the domain
- $Y$ is called the codomain
- The element $f(x)$, that a given $x \in X$ is mapped to is called the image of $x$ under $f$
- For $C \subset X$, $f(C):= \{y \in Y | \exists x \in C: f(x)=y\}$ is called the image of $C$ under $f$
- For $D \subset Y$, $f^{-1}(D):= \{x \in X | f(x) \in D\}$ is called the pre-image of $D$ under $f$
- The set $\{(x,y) \in X \times Y | y = f(x)\}$ is called the graph of $f$

# Calculus Rules for Images and Pre-Images

Let $f: X \rightarrow Y$ be a map between non-empty sets $X$ and $Y$ then:
- $C_1 \subset C_2 \subset A \rightarrow f(C_1) \subset f(C_2)$
- $D_1 \subset D_2 \subset B \rightarrow f^{-1}(D_1) \subset f^{-1}(D_2)$
- $f(C_1 \cup C_2) = f(C_1) \cup f(C_2) \hspace{10pt} \forall C_1, C_2 \subset A$
- $f^{-1}(D_1 \cup D_2) = f^{-1}(D_1) \cup f^{-1}(D_2) \hspace{10pt} \forall D_1, D_2 \subset B$
- $f(C_1 \cap C_2) \subset f(C_1) \cap f(C_2) \hspace{10pt} \forall C_1, C_2 \subset A$
- $f^{-1}(D_1 \cap D_2) = f^{-1}(D_1) \cap f^{-1}(D_2) \hspace{10pt} \forall D_1, D_2 \subset B$
- $C \subset f^{-1}(f(C)) \hspace{10pt} \forall C \subset A$
	- Example:
		- $f: \mathbb{R} \rightarrow \mathbb{R}, x \mapsto 0$
		- -> $C = \{0\}$
		- -> $f(C) = \{0\}$
		- -> $f^{-1}(f(C)) = \mathbb{R}$
- $f(f^{-1}(D)) \subset D \hspace{10pt} \forall D \subset B$

# Mapping Properties

## Injectivity

Let $f: X \rightarrow Y$ be a function between non-empty sets $X$ and $Y$. Then $f$ is called **injective** if all unique elements of $X$ produce a unique result of $Y$.
-> $\forall x_1, x_2 \in X, x_1 \neq x_2: f(x_1) \neq f(x_2)$

## Surjectivity

Let $f: X \rightarrow Y$ be a function between non-empty sets $X$ and $Y$. Then $f$ is called **surjective** if all elements of $Y$ have a corresponding element in $X$.
-> $\forall y \in Y \hspace{5pt} \exists x \in X: f(x) = y$

## Bijectivity

Let $f: X \rightarrow Y$ be a function between non-empty sets $X$ and $Y$. Then $f$ is called **bijective** if f is injective and surjective.
-> $\forall y \in Y \hspace{5pt} \exists_1 x \in X: f(x) = y$

## Example

The function $g(x):= x^2$ is nether surjective nor injective as a map from $\mathbb{R} \rightarrow \mathbb{R}$.

However, $g$ is:
- injective as a map $g: [0, \infty) \rightarrow \mathbb{R}$
- surjective as a map $g: \mathbb{R} \rightarrow [0, \infty)$ 
-> choice of domain and co-domain is crucial

# Inverse Function

If $f: X \rightarrow Y$ is a **bijective** map between non-empty sets, then there exists a unique function $f^{-1}: Y \rightarrow X$ satisfying:
- $f^{-1}(f(x)) = x \hspace{10pt} \forall x \in X$
- $f(f^{-1}(y)) = y \hspace{10pt} \forall y \in Y$

This is called the inverse function.