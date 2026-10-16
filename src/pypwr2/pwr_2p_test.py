import scipy
import numpy as np
import math
import cohen_es as cohen

def pwr_2p_test(h, n, sig_level, power, alternative):
    alternatives = {"two_sided", "less", "greater"}
    
    if alternative not in alternatives:
         raise ValueError(f"alternative not in: {alternatives}")
    
    args = [h, n, sig_level, power]
    
    if math.sum(x is None for x in args) != 1:
        raise ValueError(f"Exactly one of h, n, sig-Level, and power must be None")
    
    if h is not None and isinstance(h, str):
        h = cohen.cohen_es("p",h)[2]
    
    if n is not None and np.any(n < 1):
        raise ValueError(f"Number of Observations in each foup must be at least 1")
    
    if (sig_level is not None and not isinstance(sig_level, (int,float))) or np.any((sig_level < 0) | (sig_level > 1)):
        raise ValueError(f"'sig_level' must be a numeric in [0,1]")
    
    if (power is not None and not isinstance(power, (int,float))) or np.any((power < 0) | (power > 1)):
            raise ValueError(f"'power' must be a numeric in [0,1]")

    # Unfinished
    match alternative:
        case "two_sided":
            if h is not None:
                h = abs(h)
            
            