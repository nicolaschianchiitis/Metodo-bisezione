import numpy as np
from sympy import Symbol, Interval
from sympy.calculus.util import continuous_domain


def is_valid(f, a, b):
    x = Symbol("x")
    if is_continuous(f, x, a, b) and np.sign(f(a)) != np.sign(f(b)):
        return True
    else:
        return False


def is_continuous(f, a, b, symbol):
    dominio_intersezione_intervallo = continuous_domain(f, symbol, Interval(a, b))
    if dominio_intersezione_intervallo == Interval(a, b):
        return True
    else:
        return False
    # dominio = continuous_domain(f, symbol, Interval(a, b))
    # print(dominio)
    # return True if dominio.contains(a) and dominio.contains(b) else False



