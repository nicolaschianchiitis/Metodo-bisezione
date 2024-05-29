import turtle

import sympy as sp
from sympy.calculus.util import continuous_domain, Interval
import numpy as np
import re
import turtle as t
import math
import matplotlib.pyplot as plt
from bisection import *

t.bgcolor("black")
t.title("Metodo di bisezione")
t.color("white")
t.hideturtle()
t.penup()

TITOLO_INPUT_F = "Inserimento funzione"
PROMPT_INPUT_F = (f"Digita la funzione di cui vuoi trovare le radici approssimate attraverso il metodo di bisezione."
                  f"\nLegenda simboli principali:\n+, -, *, /, ^, =, !=\nVariabile dipendente: x\nVariabile "
                  f"indipendente: y, da NON indicare nell'input\nI numeri decimali vanno scritti con il punto (.)")
TITOLO_INPUT_INTERVALLO = "Inserimento intervallo"
PROMPT_INPUT_INTERVALLO = "Digita l'intervallo (limitato chiuso) nel formato a;b."
TITOLO_INPUT_TOLLERANZA = "Inserimento tolleranza"
PROMPT_INPUT_TOLLERANZA = "Digita la tolleranza (es. 0.001)"

pgm_in_esecuzione = True


def to_math_function(stringa):
    # f: Funzione
    f = stringa.lower().strip()
    f = re.sub(r"(\d+)([a-z])", r"\1*\2", f)
    f = re.sub(r"\((\d+)/(\d+)\)([a-z])", r"(\1/\2)*\3", f)
    funzione_matematica = sp.sympify(f, convert_xor=True)
    return funzione_matematica


def to_interval_bounds(stringa):
    stringa = stringa.strip()
    if re.search(r"-?\d+\.?(\d+)*;-?\d+\.?(\d+)*", stringa) is not None:
        estremi = stringa.split(";")
        a = estremi[0]
        b = estremi[1]
        return float(a), float(b)
    else:
        return None


def draw_f_chart(function, soluzione_approssimata):
    plt.title(f"Grafico funzione")
    plt.xlabel("x")
    plt.ylabel("y = f(x)")
    plt.grid(True)
    x_min = -50
    x_max = 50
    plt.ylim(-50, 50)
    # Disegno la funzione intera
    x_values = np.linspace(x_min, x_max, 400)
    y_values = function(x_values)
    plt.plot(x_values, y_values, linewidth=2.0, linestyle="-", color="b")
    # Soluzione approssimata
    x_appr = soluzione_approssimata
    y_appr = function(soluzione_approssimata)
    plt.plot(x_appr, y_appr, 'ro', linewidth=2.0)
    plt.show()


while pgm_in_esecuzione:
    x = sp.symbols('x')
    # Funzione SymPy
    funzione = to_math_function(t.textinput(TITOLO_INPUT_F, PROMPT_INPUT_F))
    # Tupla (a, b) ==> (float, float)
    intervallo = to_interval_bounds(t.textinput(TITOLO_INPUT_INTERVALLO, PROMPT_INPUT_INTERVALLO))
    while intervallo is None:
        intervallo = to_interval_bounds(t.textinput(TITOLO_INPUT_INTERVALLO, PROMPT_INPUT_INTERVALLO))
    tolleranza = t.textinput(TITOLO_INPUT_TOLLERANZA, PROMPT_INPUT_TOLLERANZA)
    while "0" not in tolleranza and "1" not in tolleranza and "." not in tolleranza:
        tolleranza = t.textinput(TITOLO_INPUT_TOLLERANZA, PROMPT_INPUT_TOLLERANZA)
    soluzione = f_bisection(funzione, intervallo[0], intervallo[1], float(tolleranza))
    intervallo_ab = Interval(intervallo[0], intervallo[1])
    turtle.clear()
    if soluzione is None or continuous_domain(funzione, x, intervallo_ab) != intervallo_ab:
        t.goto(-250, -250)
        t.write(f"La funzione non ammette radici nell'intervallo scelto!", font=("HelveticaNeue", 22, "normal"))
        continue
    else:
        t.goto(-200, -290)
        t.write(f"Soluzione: {soluzione}",
                font=("HelveticaNeue", 22, "normal"))
        draw_f_chart(sp.lambdify(x, funzione), soluzione)

t.mainloop()
