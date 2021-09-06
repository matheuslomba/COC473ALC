import numpy as np
import math
from inputs import ab, x_inicial, maxIter
from sup import finaliza, fx, derivada


# ===========================================

# Encontrar a raiz

def raiz(c, d, e, f, tolM):
    # Escolha de qual método será usado
    print('=' * 30)
    print('1 = Método da Bisseção\n2 = Método de Newton')
    while True:
        try:
            met = int(input('Qual método será utilizado? '))
            if met != 1 and met != 2:
                print('Favor inserir um valor válido para o método.')
            else:
                break
        except ValueError:
            print('Favor inserir um valor válido para o método (1 ou 2)')

    # Método da Bisseção
    if met == 1:
        met_bissecao(c, d, e, f, tolM)
    # Método de Newton
    elif met == 2:
        met_newton(c, d, e, f, tolM)


def met_bissecao(c, d, e, f, tolM):
    a, b = ab()
    fa = fx(a, c, d, e, f)
    fb = fx(b, c, d, e, f)

    if fa > 0 and fb < 0 or fa < 0 and fb > 0:

        n_it = 0
        while abs(b - a) > tolM:
            n_it += 1

            x = (a + b) / 2.0
            f = fx(x, c, d, e, f)

            print(n_it, "º iteração.")
            print("a = ", a)
            print("f(a) = ", fa)
            print("b = ", b)
            print("f(b) = ", fb)
            print("x = ", x)
            print("f(x) = ", f)
            print('-------------------------')

            if (f > 0):
                b = x
            else:
                a = x
    else:
        print(fa)
        print(fb)
        if fa < 0 and f(b) < 0:
            print("O intervalo selecionado não é válido pois f(a) e f(b) são ambos menores que zero.")
        else:
            print("O intervalo selecionado não é válido pois f(a) e f(b) são ambos maiores que zero.")
    return 0


def met_newton(c, d, e, f, tolM):
    max_it = maxIter()
    n_it = 1
    x = x_inicial()
    while n_it <= max_it:
        xi = x - (fx(x, c, d, e, f) / derivada(x, c, d, e, f))
        tolK = abs(xi - x)

        if tolK < tolM:
            print(n_it, "º iteração.")
            print("x(k-1) = ", x)
            print("f(x(k-1) = ", fx(x, c, d, e, f))
            print("f'(x(k-1) = ", derivada(x, c, d, e, f))
            print("x(k) = ", xi)
            print("|x(k) - x(k-1)| = ", tolK)
            return 0

        print(n_it, "º iteração.")
        print("x(k-1) = ", x)
        print("f(x(k-1) = ", fx(x, c, d, e, f))
        print("f'(x(k-1) = ", derivada(x, c, d, e, f))
        print("x(k) = ", xi)
        print("|x(k) - x(k-1)| = ", tolK)
        print('-------------------------')

        x = xi

        n_it += 1
    print("Não foi possível realizar a convergência antes de alcançar o número máximo de iterações.")

    return 0













