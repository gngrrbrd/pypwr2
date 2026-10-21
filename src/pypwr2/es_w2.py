import numpy as np

def es_w2(P):
    pi = np.sum(P, axis=1)
    pj = np.sum(P, axis=0)
    P0 = pi @ pj
    es = np.sqrt(np.sum((P-P0)**2/P0))
    return es