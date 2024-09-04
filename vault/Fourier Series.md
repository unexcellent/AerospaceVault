#uni/courses/math2 

The Fourier series provides a method for approximating periodic [[Function|functions]] into a sum of [[Trigonometric Functions|trigonometric functions]].

# Real Representation

$$
S_{N}(x) = \frac{1}{2} a_{0} + \sum_{n=1}^{N} a_{n} \cdot \cos(nx) + \sum_{n=1}^{N} b_{n} \cdot \sin(nx)
$$
with
$$
a_{0} = \frac{1}{\pi} \int^{p_{1}}_{p_{0}} f(x) \ dx
$$
$$
a_{n} = \frac{1}{\pi} \int^{p_{1}}_{p_{0}} f(x) \cdot  \cos(nx) \ dx
$$
$$
b_{n} = \frac{1}{\pi} \int^{p_{1}}_{p_{0}} f(x) \cdot  \sin(nx) \ dx
$$
-> $[p_{0}, p_{1}]$: periodic [[Interval]] of $f$

# Complex Representation

$$
S(x) = \sum_{k \in \mathbb{Z}} \hat{f}(k) \cdot e^{ikx}
$$
with
$$
\hat{f}(k) = \frac{1}{2\pi} \int_{p_{0}}^{p_{1}} f(x) \cdot e^{-ikx} \ dx
$$

# Convergence

For all points $x_{0}$ on which $f$ is continuous
$$
\lim_{x \to x_{0}} S_{N}(x) = f(x_{0})
$$
for all points on which $f$ is not continuous
$$
\lim_{x \to x_{0}} S_{N}(x) = \frac{1}{2} \left(  \lim_{x \to x_{0}-} f(x) + \lim_{x \to x_{0}+} f(x) \right)
$$