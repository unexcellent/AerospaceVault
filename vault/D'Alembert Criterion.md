#uni/courses/math1 

Method of determining [[Sequence of Numbers#Asymptotic Behavior|asymptotic behavior of increasing sequences]].

Given a sequence $a_{k}\ge 0 \quad \forall k$. If there exists a $q \in (0, 1)$ such that $\frac{a_{k+1}}{a_{k}} \le q < + \infty$ asymptotically, then $a_{k}$ is [[Sequence of Numbers#Converging Sequences|converging]].

# Example

Given the series $a_{k} = \frac{k}{10^k}$
$$
\frac{a_{k+1}}{a_{k}} = \frac{k+1}{10^{k+1}} \cdot \frac{10^{k}}{k} = \frac{k+1}{k} \cdot \frac{1}{10}
$$
with $\lim \frac{k+1}{k} = 1$.

Therefore, $\displaystyle\sum^{k=1}_{\infty} \frac{k}{10^{k}} < \infty$, which means that $a_{k}$ is converging.