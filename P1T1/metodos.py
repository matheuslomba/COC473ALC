import numpy as np
from sup import sim_def_pos, not_diag_dom

def dec_LU(matrizA, vetorB, ordemN, idet):

    if ordemN == 2:
        m = matrizA[1][0]/matrizA[0][0]
        l = [[1, 0], [m, 1]]
        u = np.linalg.solve(l, matrizA)

        y = np.linalg.solve(l, vetorB)
        x = np.linalg.solve(u, y)

    elif ordemN == 3:
        m1 = [[1, 0, 0], [-1 * matrizA[2-1][1-1]/matrizA[1-1][1-1], 1, 0], [-1 * matrizA[3-1][1-1]/matrizA[1-1][1-1], 0, 1]]
        m2 = [[1, 0, 0], [0, 1, 0], [0, -1 * np.dot(m1, matrizA)[3-1][2-1]/np.dot(m1, matrizA)[2-1][2-1], 1]]

        u = np.dot(np.dot(m2, m1), matrizA)
        l = np.linalg.inv(np.dot(m2, m1))

        y = np.linalg.solve(l, vetorB)
        x = np.linalg.solve(u, y)

        print('=' * 30)
        print(f'M1: {m1}')
        print('=' * 30)
        print(f'M2: {m2}')
    print('=' * 30)
    print(f'U:\n{u}')
    print('=' * 30)
    print(f'L:\n{l}')
    print('=' * 30)
    print(f'Y: {y}')
    print('=' * 30)
    print(f'X: {x}')
    print('=' * 30)
    if idet:
        print(f'Determinante de A = {np.linalg.det(matrizA)}')
    print('=' * 30)
    return 0


def dec_Cholesky(matrizA, vetorB, ordemN, idet):

    if sim_def_pos(matrizA, ordemN):
        l = [[]]
        for i in range(0, ordemN):
            for j in range(0, ordemN):
                if i == j:
                    sub = 0
                    for n in range(0, i):
                        sub += (l[i][n])*(l[i][n])
                    l[i].append(np.sqrt(matrizA[i][j] - sub))
                elif i > j:
                    sub = 0
                    for n in range(0, j):
                        sub += l[j][0] * l[i][0]
                    l[i].append((matrizA[i][j] - sub)/l[j][j])
                else:
                    l[i].append(0)
            if i < ordemN - 1:
                l.append(list())

        u = np.transpose(l)

        y = np.linalg.solve(l, vetorB)
        x = np.linalg.solve(u, y)

        print('=' * 30)
        print(f'L:\n{l}')
        print('=' * 30)
        print(f'U:\n{u}')
        print('=' * 30)
        print(f'Y: {y}')
        print('=' * 30)
        print(f'X: {x}')
        print('=' * 30)
        if idet:
            print(f'Determinante de A = {np.linalg.det(matrizA)}')
        print('=' * 30)
        return 0

    else:
        print(f'A matriz {matrizA} não é simétrica definida positiva.')
        return 0


def proc_Jacobi(matrizA, vetorB, ordemN, idet, tolM):

    if not not_diag_dom(matrizA, ordemN): #Condição para convergência: matrizA diagonal dominante
        x = []
        xi = []
        print('=' * 30)
        for i in range(0, ordemN):
            x.append(float(input('Insira um valor para o vetor solução X: ')))

        r = 100
        n_it = 0
        while r > tolM:
            for i in range(0, ordemN):
                sub = 0
                for j in range(0, ordemN):
                    if i != j:
                        sub += matrizA[i][j] * x[j]
                xi.append( (vetorB[i] - sub)/matrizA[i][i] )

            v_aux = np.subtract(xi, x)
            r = np.linalg.norm(v_aux)/np.linalg.norm(xi)

            x = xi[:]
            xi = []
            n_it += 1
            print(f'R da iteração {n_it}: {r}')
            print('=' * 30)

        print('=' * 30)
        print(f'X:\n{x}')
        print('=' * 30)
        if idet:
            print(f'Determinante de A = {np.linalg.det(matrizA)}')
        print('=' * 30)
        return 0


def proc_Gauss_Seidel(matrizA, vetorB, ordemN, idet, tolM):

    if not not_diag_dom(matrizA, ordemN) or sim_def_pos(matrizA, ordemN): #Condição para convergência
        x = []
        print('=' * 30)
        for i in range(0, ordemN):
            x.append(float(input('Insira um valor para o vetor solução X: ')))
        xi = x[:]

        r = 100
        n_it = 0
        while r > tolM:
            for i in range(0, ordemN):
                sub = 0
                for j in range(0, ordemN):
                    if i != j:
                        sub += matrizA[i][j] * xi[j]
                xi[i] = (vetorB[i] - sub) / matrizA[i][i]

            v_aux = np.subtract(xi, x)
            r = np.linalg.norm(v_aux) / np.linalg.norm(xi)

            x = xi[:]
            n_it += 1
            print('=' * 30)
            print(f'R da iteração {n_it}: {r}')

        print('=' * 30)
        print(f'X:\n{x}')
        print('=' * 30)
        if idet:
            print(f'Determinante de A = {np.linalg.det(matrizA)}')
        print('=' * 30)
    return 0

