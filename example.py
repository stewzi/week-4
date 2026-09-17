import numpy as np


def testing(n=5):
    print(f"Testing with {n} random numbers.")
    return np.random.randint(1, 11, n)