from scipy.stats import norm
from scipy.optimize import root_scalar
import numpy as np
from pypwr2.cohen_es import cohen_es

def pwr_2p2n_test(h=None, n1=None, n2=None, sig_level=None, power=None, alternative="two_sided"):
    alternatives = {"two_sided", "less", "greater"}
    
    if alternative not in alternatives:
         raise ValueError(f"alternative not in: {alternatives}")
  
    args = [h, n1, n2, sig_level, power]

    if sum(x is None for x in args) != 1:
        raise ValueError(f"Exactly one of h, n1, n2, sig-Level, and power must be None")

    if h is not None and isinstance(h, str):
        h = abs(cohen_es("p",h)[2])

    if n1 is not None and np.any(n1 < 1):
        raise ValueError(f"Number of observations in the first group must be at least 2")

    if n2 is not None and np.any(n2 < 1):
        raise ValueError(f"Number of observations in the second group must be at least 2")

    if (sig_level is not None) and (not isinstance(sig_level, (int,float)) or np.any((sig_level < 0) | (sig_level > 1))):
        raise ValueError(f"'sig_level' must be a numeric in [0,1]")

    if (power is not None) and (not isinstance(power, (int,float)) or np.any((power < 0) | (power > 1))):
            raise ValueError(f"'power' must be a numeric in [0,1]")

    def power_fun(hv, n1v, n2v, sigv):
        match alternative:
            case "greater":
                return norm.sf(
                    norm.isf(sigv) - hv * np.sqrt((n1v*n2v)/(n1v+n2v))
                )

            case "two_sided":
                return (
                    norm.sf(
                        norm.isf(sigv / 2) - hv * np.sqrt((n1v*n2v)/(n1v+n2v))
                    )
                    +
                    norm.cdf(
                        norm.ppf(sigv / 2) - hv * np.sqrt((n1v*n2v)/(n1v+n2v))
                    )
                )

            case "less":
                return norm.cdf(
                    norm.ppf(sigv) - hv * np.sqrt((n1v*n2v)/(n1v+n2v))
                )

    if h is None:
        def fun(h):
            return power_fun(h, n1, n2, sig_level) - power
        match alternative:
            case "two_sided":
                h = root_scalar(fun, bracket=[1e-10, 10], method='brentq').root
            case "less":
                h = root_scalar(fun, bracket=[-10, 5], method='brentq').root
            case "greater":
                h = root_scalar(fun, bracket=[-5, 10], method='brentq').root
    
    else:
        match (n1, n2, sig_level, power):
            case (None, n2, sig_level, power):
                def fun2(n1):
                    return power_fun(h, n1, n2, sig_level) - power
                n1 = root_scalar(fun2, bracket=[2 + 1e-10, 1e9], method='brentq').root
            case (n1, None, sig_level, power):
                def fun2(n2):
                    return power_fun(h, n1, n2, sig_level) - power
                n2 = root_scalar(fun2, bracket=[2 + 1e-10, 1e9], method='brentq').root
            case(n1, n2, None, power):
                def fun3(sig_level):
                    return power_fun(h, n1, n2, sig_level) - power
                sig_level = root_scalar(fun3, bracket=[1e-10, 1- 1e-10], method='brentq').root
            case(n1, n2, sig_level, power):
                power = power_fun(h, n1, n2, sig_level)

    note="Different sample sizes"
    method = "Difference of proportion power calculation for binomial distribution (arcsine transformation)"

    return {
        "h": h,
        "n1": n1,
        "n2": n2,
        "sig_level": sig_level,
        "power": power,
        "alternative": alternative,
        "method": method,
        "note": note
    }
