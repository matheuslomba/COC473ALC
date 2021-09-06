import numpy as np


def finaliza():
    # Impede que o terminal feche automaticamente assim que o programa finaliza.
    input('Pressione qualquer tecla para finalizar...')


def fun1(a, b, c, teta0):
    return (2 * (b ** 2)) + (a ** 2) + (6 * (c ** 2)) - teta0


def fun2(a, b, c, teta1):
    return (8 * (b ** 3)) + (6 * b * (a ** 2)) + (36 * a * b * c) + (108 * b * (c ** 2)) - teta1


def fun3(a, b, c, teta2):
    return (60 * (b ** 4)) + (60 * (b ** 2) * (a ** 2)) + (576 * a * c * (b ** 2)) + (2232 * (b ** 2) * (c ** 2)) + (
                252 * (c ** 2) * (a ** 2)) + (1296 * a * (c ** 3)) + (3348 * (c ** 4)) + (24 * c * (a ** 3)) + (
                       3 * b) - teta2


def dParcial(f, x, a, b, c, teta):
    h = 1e-5

    if f == 1:
        if x == 'a':
            return (fun1(a + h, b, c, teta) - fun1(a - h, b, c, teta)) / (2 * h)
        elif x == 'b':
            return (fun1(a, b + h, c, teta) - fun1(a, b - h, c, teta)) / (2 * h)
        elif x == 'c':
            return (fun1(a, b, c + h, teta) - fun1(a, b, c - h, teta)) / (2 * h)
    elif f == 2:
        if x == 'a':
            return (fun2(a + h, b, c, teta) - fun2(a - h, b, c, teta)) / (2 * h)
        elif x == 'b':
            return (fun2(a, b + h, c, teta) - fun2(a, b - h, c, teta)) / (2 * h)
        elif x == 'c':
            return (fun2(a, b, c + h, teta) - fun2(a, b, c - h, teta)) / (2 * h)
    elif f == 3:
        if x == 'a':
            return (fun3(a + h, b, c, teta) - fun3(a - h, b, c, teta)) / (2 * h)
        elif x == 'b':
            return (fun3(a, b + h, c, teta) - fun3(a, b - h, c, teta)) / (2 * h)
        elif x == 'c':
            return (fun3(a, b, c + h, teta) - fun3(a, b, c - h, teta)) / (2 * h)