import numpy as np

def es_h(p1,p2):
    es = 2*np.arcsin(np.sqrt(p1))-2*np.arcsin(np.sqrt(p2))
    return es