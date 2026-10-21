# pypwr2 v0.2.1
A Python port of the [pwr](https://github.com/heliosdrm/pwr) package in R

## Scope and Approach

In scope, this package exists to bring the functionality and broad usability of the pwr package to python. Command and file structure was kept as identical as possible. Logic was kept functionally the same but uses some pythonic structuring to either bridge a langauge gap or, in some cases, improve the runtime complexity. Otherwise, all usage of the function is or will be kept identical to its R counter part. 

Functions successfully ported:
- es.h as **es_h**
- es.w1 as **es_w1**
- es.w2 as **es_w2**
- pwr.2p.test as **pwr_2p_test**
- pwr.2n2p.test as **pwr_2p2n_test**

Functions not ported yet:
- pwr.anova.test
- pwr.chisq.test
- pwr.norm.test
- pwr.p.test
- pwr.r.test
- pwr.t.test
- pwr.t2n.test

## Note: 

Where R uses the built in command uniroot to solve for whatever is null between h, n(s), sig.level, and power, this port uses root_scalar eith method brentq from scipy optimize. Even though both functions use Brent's Method as a root finding algorithm, there has been found a mathematical results discrepancy of approximately 0.001% in results. While this doesn't effect sample sizing in a practical sense, this must be noted for transparency.
