import turtle as t
import matplotlib.pyplot
import sympy as sp
from sympy.calculus.util import continuous_domain, Interval
import re
from bisection import *


chart = matplotlib.pyplot
pgm_window = t.Turtle()
t.bgcolor("black")
t.title("Metodo di bisezione")
pgm_window.color("white")
pgm_window.hideturtle()
pgm_window.penup()

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
        for character in stringa:
            if character not in "0123456789.;-/()":
                stringa = stringa.replace(character, "")
        estremi = stringa.split(";")
        a = estremi[0]
        b = estremi[1]
        return float(a), float(b)
    else:
        return None


def draw_f_chart(function, soluzione_approssimata):
    chart.clf()  # Reset grafico
    chart.title(f"Grafico funzione\nSoluzione approssimata: {soluzione_approssimata}")
    chart.xlabel("x")
    chart.ylabel("y = f(x)")
    chart.grid(True)
    x_min = -50
    x_max = 50
    chart.ylim(-50, 50)
    # Disegno la funzione intera
    x_values = np.linspace(x_min, x_max, 400)
    y_values = function(x_values)
    chart.plot(x_values, y_values, linewidth=2.0, linestyle="-", color="b")
    # Soluzione approssimata
    x_appr = soluzione_approssimata
    y_appr = function(soluzione_approssimata)
    chart.plot(x_appr, y_appr, 'ro', linewidth=2.0)
    chart.show()


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
    for ch in tolleranza:
        if ch not in "01.":
            tolleranza = tolleranza.replace(ch, "")
    if intervallo[1] < intervallo[0]:
        soluzione = f_bisection(funzione, intervallo[1], intervallo[0], float(tolleranza))
        intervallo_ab = Interval(intervallo[1], intervallo[0])
    else:
        soluzione = f_bisection(funzione, intervallo[1], intervallo[0], float(tolleranza))
        intervallo_ab = Interval(intervallo[1], intervallo[0])
    pgm_window.clear()
    if soluzione is None or continuous_domain(funzione, x, intervallo_ab) != intervallo_ab:
        pgm_window.goto(-250, -250)
        pgm_window.write(f"La funzione non ammette radici nell'intervallo scelto!",
                         font=("HelveticaNeue", 22, "normal"))
        continue
    else:
        pgm_window.goto(-200, -290)
        pgm_window.write(f"Soluzione approssimata: {soluzione}",
                         font=("HelveticaNeue", 22, "normal"))
        draw_f_chart(sp.lambdify(x, funzione), soluzione)

t.mainloop()

