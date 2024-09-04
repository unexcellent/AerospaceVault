#uni/courses/math2 

A series is the operation of adding a [[Sequence of Functions]] $f_{k}$ infinitely many times.
$$
\sum^{\infty}_{k=1} f_{k}
$$

# Convergence

Just like [[Sequence of Functions|sequences]], a function series can converge [[Sequence of Functions#Pointwise Convergence|pointwise]], [[Sequence of Functions#Uniform Convergence|uniformely]] and [[Series Convergence#Absolute Convergence|absolutely]].

## Total Convergence

A series of functions $f_{k}(x)$ is called totally convergent if
- $f_{k}(x)$ is [[Sequence of Functions#Uniform Convergence|uniformely convergent]]
- there exists a [[Sequence of Numbers|sequence of non-negative numbers]] $M_{k}$ with $\sum_{k} M_{k} < \infty$
- $|f_{k}| \le M_{k} \quad \forall k$ independently of $x$

## Normal Convergence

If $M_{k}$ is chosen as $M_{k} := \sup \{ |f_{k}| \}$, the series is called normally convergent.