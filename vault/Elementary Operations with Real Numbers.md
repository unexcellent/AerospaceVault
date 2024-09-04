#uni/courses/math0 

Mathematical operations can be understood as [[Function|functions]].
-> $+$: $\mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}, (x,y) \mapsto x+y$

# Sums and Products

Given numbers $a_i \in \mathbb{R}, i=1, ..., n, n\in \mathbb{N}$

- $\sum\limits_{i=m}^{n} a_i = a_m + a_{m+1} + a_{m+1} + ... + a_n \hspace{10pt} m,n \in \mathbb{N}, m<n$
- $\prod\limits_{i=m}^{n} a_i = a_{m} \cdot a_{m+1} \cdot a_{m+2} \cdot ... \cdot a_n \hspace{10pt} m,n \in \mathbb{N}, m<n$ 

If $m > n$, then equals 1.

# Powers and Roots

$a^n = \prod\limits_{i=1}^n a \hspace{10pt} \forall a \in \mathbb{R}, \forall n \in \mathbb{N}_0$
-> $a^0 = \prod\limits_{i=1}^0 a = 1$

For fixed but arbitrary $n \in \mathbb{N}$ introduce $f_n: \mathbb{R}_{\ge 0} \rightarrow \mathbb{R}_{\ge 0}, x \mapsto x^n$, which is bijective.

Inverse function: $(\cdot)^{\frac{1}{n}}, \mathbb{R}_{\ge 0} \rightarrow \mathbb{R}_{\ge 0} \Rightarrow a^{\frac{1}{n}} = \sqrt[n]{a}$ 

We define: $a^{\frac{m}{n}} = (a^{\frac{1}{n}})^m = \sqrt[n]{a}^m \hspace{10pt} \forall a \in \mathbb{R}_{\ge 0}, \forall m \in \mathbb{N}_{0}, \forall n \in \mathbb{N}$

## Properties

- $a^r > 0$
- $a^r \cdot a^s = a^{r+s}$
- $a^r \cdot b^r = (ab)^{r}$
- $(a^r)^s = a^{rs}$

# Exponential Function

The functions $\overline{g}_a: \mathbb{R} \rightarrow \mathbb{R}, x \mapsto a^x$ for $a \in \mathbb{R}_{>0}$ are examples of exponential functions.

A function $f: \mathbb{R} \rightarrow \mathbb{R}, x \mapsto b \cdot a^x$ with $a \in \mathbb{R}_{>0}, b \in \mathbb{R}$.

In the special case $b=1, a = e = 2.71828...$ $f: \mathbb{R} \rightarrow \mathbb{R}, x \mapsto e^x$ is called natural/the exponential function.
The base $e$ is chosen such that the graph of $f$ has slope $1$ at $x=0$. It can be written as $f(x) = exp(x)$

# Logarithmic Function

For every $1 \neq a \in \mathbb{R}_{\gt 0}$, the function $f: \mathbb{R} \rightarrow \mathbb{R}_{\ge 0}, x \mapsto a^x$ is bijective.

This allows us to define the inverse of the map $x \mapsto a^x$ for $1 \neq a \in \mathbb{R}_{\gt 0}$. This inverse is called the logarithm with respect to base $a$.

## Definition

Suppose $1 \neq a \in \mathbb{R}_{\gt 0}$ and $b \in \mathbb{R}_{\gt 0}$ are given. the unique number $x \in \mathbb{R}$ satisfying $a^x = b$ is called the logarithm of $b$ with base $a$.

Notation: $\log_a(b)$

## Special Logarithms

- The logarithm with base $a = e$ is called the natural logarithm with the notation $\ln$ 
- The logarithm with base $a = 10$ is often denoted by $\lg$
- If no base is mentioned, the value of $a$ has to be deduced from the context

## Properties

For $a,b,c \in \mathbb{R}_{\gt 0}, a \neq 1$ 
- $\log_a 1 = 0$
- $\log_a a = 1$
- $a^{\log_a b} = \log_a (a^b) = b$
- $\log_a (a^b) = b$
- $\log_a(bc) = \log_a(b) + \log_a(c)$
- $\log_a(\frac{b}{c}) = \log_a(b) - \log_a(c)$
- $\log_a(b^c) = c \cdot \log_a(b)$

With this we can relate logarithms that have different bases to each other.

Suppose $a_1,a_2,c \in \mathbb{R}_{\gt 0}$ satisfying $a_1,a_2 \neq 1$ are given, then:
- $\log_{a_1}(b) = \log_{a_1}(a_2^{\log_{a_2}(b)}) = \log_{a_2}(b) \cdot \log_{a_1}(a_2)$
- $\log_{a_2}(b) = \frac{\log_{a_1}(b)}{\log_{a_1}(a_2)}$