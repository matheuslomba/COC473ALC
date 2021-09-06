import numpy as np
import math
from inputs import ab, num_pontos
from sup import finaliza, fx, pontos_quad_gauss, pontos_quad_polinomial, constantesL


# ===========================================

# Encontrar a raiz

def integral(c, d, e, f):
    # Escolha de qual método será usado
    print('=' * 30)
    print('1 = Quadratura de Gauss (Gauss-Legendre)\n2 = Quadratura Polinomial')
    while True:
        try:
            met = int(input('Qual método será utilizado? '))
            if met != 1 and met != 2:
                print('Favor inserir um valor válido para o método.')
            else:
                break
        except ValueError:
            print('Favor inserir um valor válido para o método (1 ou 2)')

    # Quadratura de Gauss
    if met == 1:
        quad_gauss(c, d, e, f)
    # Quadratura Polinomial
    elif met == 2:
        quad_polinomial(c, d, e, f)


def quad_gauss(c, d, e, f):
    a, b = ab()
    n_pts = num_pontos()
    valores_pontos = pontos_quad_gauss()

    L = b - a

    Aaux = 0

    for i in range(0, n_pts):
        wi = valores_pontos[n_pts - 2][0][i]
        zi = valores_pontos[n_pts - 2][1][i]
        fxi = fx((a + b + zi * L) / 2, c, d, e, f)
        Aaux += fxi * wi

        print("i = ", i + 1)
        print("wi = ", wi)
        print("zi = ", zi)
        print("fxi = ", fxi)
        print("Aaux = ", Aaux)
        print('-------------------------')

    A = Aaux * L / 2
    print("A = ", A)

    return 0


def quad_polinomial(c, d, e, f):
    a, b = ab()
    L = b - a
    n_pts = num_pontos()
    valores_pontos = pontos_quad_polinomial(a, b, L, n_pts)

    A = 0
    for i in range(0, n_pts):
        wi = valores_pontos[1][i]
        fxi = fx(valores_pontos[0][i], c, d, e, f)
        A += wi * fxi

        print("i = ", i + 1)
        print("wi = ", wi)
        print("fxi = ", fxi)
        print("A = ", A)
        print('-------------------------')

    return 0




