import numpy as np
import math
from sup import simetrica, maiorTolM, maiorForaDiag

#------------------------------------------------------------

def met_potencia(matrizA, ordemN, idet, tolM):

    l0 = 1 #lambda0
    x = []
    print('=' * 30)
    for i in range(0, ordemN):
        x.append(float(input('Insira um valor para o vetor solução X: ')))

    r = 100
    n_it = 0
    while r > tolM:

        y = np.dot(matrizA, x)

        l = y[0]
        for i in range(0, len(x)):
            x[i] = y[i]/l

        r = abs(l-l0)/abs(l)
        l0 = l
        n_it += 1
        print('=' * 30)
        print(f'R da iteração {n_it}: {r}')

    print('=' * 30)
    autovalores = np.linalg.eigvals(matrizA)
    av = []
    for a in autovalores:
        av.append(a)
    print(f'Autovalores:\n{av}')
    print('=' * 30)
    print(f'Autovetor:\n{x}')
    print('=' * 30)
    if idet:
        print(f'Determinante de A = {np.linalg.det(matrizA)}')

    return 0

#------------------------------------------------------------

def met_jacobi(matrizA, ordemN, idet, tolM):

    #Condição: só matriz simétrica
    if simetrica(matrizA, ordemN):

        detA = np.linalg.det(matrizA)

        x = np.eye(ordemN)

        n_it = 0
        while maiorTolM(matrizA, ordemN, tolM):

            maior, maior_i, maior_j = maiorForaDiag(matrizA, ordemN)

            if matrizA[maior_i][maior_i] == matrizA[maior_j][maior_j]:
                phi = math.pi / 4
            else:
                phi = 0.5 * ( math.atan( (2 * matrizA[maior_i][maior_j]) / (matrizA[maior_i][maior_i] - matrizA[maior_j][maior_j]) ) )

            p = np.eye(ordemN)
            p[maior_i][maior_i] = math.cos(phi)
            p[maior_i][maior_j] = -1 * math.sin(phi)
            p[maior_j][maior_i] = math.sin(phi)
            p[maior_j][maior_j] = math.cos(phi)

            pt = np.transpose(p)
            matrizA = np.dot(np.dot(pt, matrizA), p)

            x = np.dot(x, p)

            n_it += 1

        av = []
        for i in range(0, ordemN):
            av.append(matrizA[i][i])

        print('=' * 30)
        print(f'Matriz P:\n{p}')
        print('=' * 30)
        print(f'Matriz A:\n{matrizA}')
        print('=' * 30)
        print(f'Autovalores: {av}')
        print('=' * 30)
        print(f'Matriz X:\n{x}')
        print('=' * 30)
        print(f'{n_it} iterações para convergência.')
        print('=' * 30)
        if idet:
            print(f'Determinante de A = {detA}')
            print('=' * 30)

    return 0