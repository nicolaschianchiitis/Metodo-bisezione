import turtle

from numpy import sign, abs


def f_bisection(f, a, b, tol):
    # approximates a root, R, of f bounded
    # by a and b to within tolerance
    # | f(m) | < tol with m the midpoint
    # between a and b Recursive implementation

    # check if a and b bound a root
    if sign(f(a)) == sign(f(b)):
        turtle.textinput("Avviso", "La funzione non si annulla nell'intervallo indicato.\n"
                                   "Premi su uno dei tasti qua sotto per continuare.")

    # get midpoint
    m = (a + b) / 2

    if abs(f(m)) < tol:
        # stopping condition, report m as root
        return m
    elif sign(f(a)) == sign(f(m)):
        # case where m is an improvement on "a".
        # Make recursive call with a = m
        return f_bisection(f, m, b, tol)
    elif sign(f(b)) == sign(f(m)):
        # case where m is an improvement on "b".
        # Make recursive call with b = m
        return f_bisection(f, a, m, tol)
