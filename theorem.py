import numpy as np
from sympy import Interval, lambdify
from sympy.calculus.util import continuous_domain


def is_valid(f, a, b, symbol):
    f_lambda = lambdify(symbol, f)
    if is_continuous(f, symbol, a, b) and np.sign(f_lambda(a)) != np.sign(f_lambda(b)):
        return True
    else:
        return False


def is_continuous(f, a, b, symbol):
    dominio_intersezione_intervallo = continuous_domain(f, symbol, Interval(a, b))
    if dominio_intersezione_intervallo == Interval(a, b):
        return True
    else:
        return False
