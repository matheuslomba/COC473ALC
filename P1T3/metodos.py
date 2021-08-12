import numpy as np
import math

#------------------------------------------------------------

def interpolacao(x, listapontos, paresN):

    phi = 1
    y = 0

    for i in range(0, paresN):
        for j in range(0, paresN):
           if j != i:
               phi *= (x - listapontos[j][0]) / (listapontos[i][0] - listapontos[j][0])
        y += phi * listapontos[i][1]
        phi = 1

    print(f'y = {y}')

    return 0

#------------------------------------------------------------

def regressao(x, listapontos, paresN):

    matrizP = [[]]
    matrizY = []

    for i in range(0, paresN):
        for j in range(0, 2):
            if j == 0:
                matrizP[i].append(1/math.pow(math.e, listapontos[i][0]))
            else:
                matrizP[i].append(math.log(listapontos[i][0], math.e))
        matrizY.append(listapontos[i][1])

        if i < paresN - 1:
            matrizP.append(list())

    matrizPt = np.transpose(matrizP)
    matrizA = np.dot(matrizPt, matrizP)
    matrizC = np.dot(matrizPt, matrizY)
    MatrizAinv = np.linalg.inv(matrizA)
    matrizB = np.dot(MatrizAinv, matrizC)

    y = (matrizB[0] / math.e ** x) + matrizB[1] * math.log(x, math.e)

    print(f'y = {y}')

    return 0