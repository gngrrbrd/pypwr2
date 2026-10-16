import pandas as pd

def cohen_es(test, size):
    tests = {"p", "t", "r", "anov", "chisq", "f2"}
    sizes = {"small", "medium", "large"}

    if test not in tests:
        raise ValueError(f"Test must be: {test}")
    if size not in sizes:
        raise ValueError(f"Size must be: {size}")
    es = cohen(test, size)
    cohen = pd.DataFrame([
            {"test": test, 
             "size": size, 
             "effect_size": es, 
             "method": "Conventional effect size from Cohen (1982)"}
        ])
    return cohen

def cohen(test, size):
    es = {
        "p": {
            "small": 0.2,
            "medium": 0.5,
            "large": 0.8,
        },
        "t": {
            "small": 0.2,
            "medium": 0.5,
            "large": 0.8,
        },
        "r": {
            "small": 0.1,
            "medium": 0.3,
            "large": 0.5,
        },
        "anov": {
            "small": 0.1,
            "medium": 0.25,
            "large": 0.4,
        },
        "chisq": {
            "small": 0.1,
            "medium": 0.3,
            "large": 0.5,
        },
        "f2": {
            "small": 0.02,
            "medium": 0.15,
            "large": 0.35,
        },
    }

    return es[test][size]