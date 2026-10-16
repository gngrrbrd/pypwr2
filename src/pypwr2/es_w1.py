import math
import numpy as np

def es_w1(P0,P1):
    es = math.sqrt(np.sum((P1-P0)**2/P0))
    return es