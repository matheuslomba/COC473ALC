import numpy as np
import math


def finaliza():
    # Impede que o terminal feche automaticamente assim que o programa finaliza.
    input('Pressione qualquer tecla para finalizar...')


def fx(x, c, d, e, f):
    return (c * (math.exp(d * x)) + (e * (x ** f)))


def derivada(x, c, d, e, f):
    h = 1e-5

    return (fx(x + h, c, d, e, f) - fx(x - h, c, d, e, f)) / (2 * h)


def pontos_quad_gauss():
    valores_pontos = [
        [[1.0, 1.0], [0.57735, -0.57735]],
        [[0.555556, 0.88889, 0.55556], [0.77459, 0, -0.77459]],
        [[0.34786, 0.65215, 0.65215, 0.34786], [0.86114, 0.33998, -0.33999, -0.86114]],
        [[0.23693, 0.47863, 0.56889, 0.47863, 0.23693], [0.90618, 0.53847, 0, -0.53847, -0.90618]],
        [[0.17133, 0.36076, 0.46791, 0.46791, 0.36076, 0.17133],
         [0.93247, 0.66121, 0.23862, -0.23862, -0.66121, -0.93247]],
        [[0.12949, 0.27971, 0.38183, 0.41796, 0.38183, 0.27971, 0.12949],
         [0.94911, 0.74153, 0.40585, 0, -0.40585, -0.74153, -0.94911]],
        [[0.10123, 0.22238, 0.31371, 0.36268, 0.36268, 0.31371, 0.22238, 0.10123],
         [0.96029, 0.79667, 0.53553, 0.18343, -0.18343, -0.53553, -0.79667, -0.96029]],
        [[0.08127, 0.18065, 0.26061, 0.31235, 0.33024, 0.31235, 0.26061, 0.18065, 0.08127],
         [0.96816, 0.83603, 0.61337, 0.32425, 0, -0.32425, -0.61337, -0.83603, -0.96816]],
        [[0.06667, 0.14945, 0.21909, 0.26927, 0.29552, 0.29552, 0.26927, 0.21909, 0.14945, 0.06667],
         [0.97391, 0.86506, 0.67941, 0.43339, 0.14887, -0.14887, -0.43339, -0.67941, -0.86506, -0.97391]]
    ]
    return valores_pontos


def pontos_quad_polinomial(a, b, L, n_pts):
    valores_pontos = [[], []]
    for i in range(0, (n_pts - 1)):
        if n_pts == 3 and i == 1:
            valores_pontos[0].append((a + b) / 2)
        else:
            valores_pontos[0].append(a + i * (b - a) / (n_pts - 1))
    valores_pontos[0].append(b)

    constantes = constantesL(n_pts)

    for j in range(0, n_pts):
        valores_pontos[1].append(L * constantes[j])

    print(valores_pontos)
    return valores_pontos


def constantesL(n_pts):
    delta = 1 / (n_pts - 1)

    x = []
    for i in range(0, n_pts):
        x.append(delta * (i))

    A = [[]]
    B = []

    for i in range(0, n_pts):
        for j in range(0, n_pts):
            A[i].append((x[j]) ** (i))
        B.append(1 / (i + 1))
        A.append([])

    A.pop()
    w = np.dot(np.linalg.inv(A), B)
    wt = np.transpose(w)
    return wt


