import numpy as np
import math
from inputs import pontox, deltax
from sup import finaliza, fx


# ===========================================

# Encontrar a raiz

def derivadaDF(c, d, e, f):
    # Escolha de qual método será usado
    print('=' * 30)
    print('1 = Diferenças Finitas - Passo a Frente\n2 = Diferenças Finitas - Passo Atrás\n3 = Diferença Central')
    while True:
        try:
            met = int(input('Qual método será utilizado? '))
            if met != 1 and met != 2 and met != 3:
                print('Favor inserir um valor válido para o método.')
            else:
                break
        except ValueError:
            print('Favor inserir um valor válido para o método (1, 2 ou 3)')

    x = pontox()
    dx = deltax(0)

    # Passo a Frente
    if met == 1:
        d = (fx(x + dx, c, d, e, f) - fx(x, c, d, e, f)) / dx - dx
        print("f'(x) = ", d)
        return 0

    # Passo Atrás
    elif met == 2:
        d = (fx(x, c, d, e, f) - fx(x - dx, c, d, e, f)) / dx + dx
        print("f'(x) = ", d)
        return 0

    # Diferença Central
    elif met == 3:
        d = (fx(x + dx, c, d, e, f) - fx(x - dx, c, d, e, f)) / (2 * dx)
        print("f'(x) = ", d)
        return 0
