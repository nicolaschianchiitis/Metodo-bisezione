import numpy as np
from sympy import lambdify, symbols


def f_bisection(f, a, b, tol):
    # approximates a root, R, of f bounded 
    # by a and b to within tolerance 
    # | f(m) | < tol with m the midpoint 
    # between a and b Recursive implementation

    # Make the function lambda
    f_lambda = lambdify(symbols('x'), f)

    # check if a and b bound a root
    if np.sign(f_lambda(a)) == np.sign(f_lambda(b)):
        return None

    # get midpoint
    m = (a + b) / 2

    if np.abs(f_lambda(m)) < tol:
        # stopping condition, report m as root
        return m
    elif np.sign(f_lambda(a)) == np.sign(f_lambda(m)):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return f_bisection(f, m, b, tol)
    elif np.sign(f_lambda(b)) == np.sign(f_lambda(m)):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return f_bisection(f, a, m, tol)