from numpy import sign, abs
from sympy import Interval, lambdify, symbols
from sympy.calculus.util import continuous_domain


def f_bisection(f, a, b, tol):
    # approximates a root, R, of f bounded
    # by a and b to within tolerance
    # | f(m) | < tol with m the midpoint
    # between a and b Recursive implementation

    # check if a and b bound a root
    f_lambda = lambdify(symbols('x'), f)
    if sign(f_lambda(a)) == sign(f_lambda(b)) and continuous_domain(f, symbols('x'), Interval(a, b)) != Interval(a, b):
        return None

    # get midpoint
    m = (a + b) / 2
    m_abs = abs(m)

    if f_lambda(m_abs) < tol:
        # stopping condition, report m as root
        return m
    elif sign(f_lambda(a)) == sign(f_lambda(m)):
        # case where m is an improvement on "a".
        # Make recursive call with a = m
        return f_bisection(f, m, b, tol)
    elif sign(f_lambda(b)) == sign(f_lambda(m)):
        # case where m is an improvement on "b".
        # Make recursive call with b = m
        return f_bisection(f, a, m, tol)
