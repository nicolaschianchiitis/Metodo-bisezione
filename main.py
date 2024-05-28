import sympy
import re

from bisection import *
from theorem import *
from chart import *
import turtle as t

TITOLO_INPUT_F = "Inserimento funzione"
PROMPT_INPUT_F = (f"Digita la funzione di cui vuoi trovare le radici approssimate attraverso il metodo di bisezione."
                  f"\nLegenda simboli principali:\n+, -, *, /, ^, =, !=\nVariabile dipendente: x\nVariabile "
                  f"indipendente: y, da NON indicare nell'input\nI numeri decimali vanno scritti con il punto (.)")
TITOLO_INPUT_INTERVALLO = "Inserimento intervallo"
PROMPT_INPUT_INTERVALLO = "Digita l'intervallo (limitato chiuso) nel formato a;b."

pgm_in_esecuzione = True


def to_math_function(stringa):
    funzione = stringa.lower().strip()
    funzione = re.sub(r"(\d+)([a-z])", r"\1*\2", funzione)
    funzione = re.sub(r"\((\d+)/(\d+)\)([a-z])", r"(\1/\2)*\3", funzione)
    funzione_matematica = sympy.sympify(funzione, convert_xor=True)
    return funzione_matematica


def to_interval_bounds(stringa):
    stringa = stringa.strip()
    if re.search(r"-?\d+\.?(\d+)*;-?\d+\.?(\d+)*", stringa) is not None:
        estremi = stringa.split(";")
        return float(estremi[0]), float(estremi[1])
    else:
        return None


while pgm_in_esecuzione:
    # Funzione SymPy
    input_funzione = to_math_function(t.textinput(TITOLO_INPUT_F, PROMPT_INPUT_F))
    print(input_funzione)
    # Tupla (a, b) ==> (float, float)
    input_intervallo = to_interval_bounds(t.textinput(TITOLO_INPUT_INTERVALLO, PROMPT_INPUT_INTERVALLO))
    while input_intervallo is None:
        input_intervallo = to_interval_bounds(t.textinput(TITOLO_INPUT_INTERVALLO, PROMPT_INPUT_INTERVALLO))
    print(f"Intervallo [{input_intervallo[0]}; {input_intervallo[1]}]")

    # Test
    print(is_continuous(input_funzione, input_intervallo[0], input_intervallo[1], sympy.symbols('x')))

t.mainloop()
