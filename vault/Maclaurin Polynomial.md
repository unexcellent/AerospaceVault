#uni/courses/math0 

As derivatives provide a **linearization** of a given function, they can be used to approximate a complicated function by a simpler functions.

Let $n \in \mathbb{N}_{0}$. Consider a function $f: \mathbb{R} \to \mathbb{R}$, that is n-times differentiable at $x=0$ with derivatives $f^{(k)}(0) \in \mathbb{R}, \quad k=0, \dots, n$. Then the Maclaurin [[Polynomial and Rational Functions|polynomial]] of order n (or Taylor polynomial of order n with expansion point 0) associated with f is defined to be.
$$
T_{n}(x) = \sum\limits_{k=0}^{n} \frac{f^{(k)}(0)}{k!} x^{k}= f(0) + f'(0) x + \frac{1}{2} f''(0) x^{2}+ \dots + \frac{1}{n!} f^{(n)}(0) x^n
$$
