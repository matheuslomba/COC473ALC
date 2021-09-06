import numpy as np
import math
from inputs import pontox, deltax
from sup import finaliza, fx


# ===========================================

# Encontrar a raiz

def derivadaRE(c, d, e, f):
    x = pontox()
    dx1 = deltax(1)
    dx2 = deltax(2)
    p = 1
    q = dx1 / dx2

    d1 = (fx(x + dx1, c, d, e, f) - fx(x, c, d, e, f)) / dx1
    print("f'1(x) = ", d1)

    d2 = (fx(x + dx2, c, d, e, f) - fx(x, c, d, e, f)) / dx2
    print("f'2(x) = ", d2)

    dfinal = d1 + (d1 - d2) / (q ** (-p) - 1)

    print("f'final(x) = ", dfinal)

    return 0