import numpy as np
import math
from sup import finaliza, fun1, fun2, fun3, dParcial


# ------------------------------------------------------------

def met_newton(vetorX, teta1, teta2, tolM):
    x = vetorX[:]

    r = 100
    n_it = 0
    while r > tolM:
        a = x[0]
        b = x[1]
        c = x[2]
        fx = [[fun1(a, b, c, 1)], [fun2(a, b, c, teta1)], [fun3(a, b, c, teta2)]]

        jx = [
            [dParcial(1, 'a', a, b, c, 1), dParcial(1, 'b', a, b, c, 1), dParcial(1, 'c', a, b, c, 1)],
            [dParcial(2, 'a', a, b, c, teta1), dParcial(2, 'b', a, b, c, teta1), dParcial(2, 'c', a, b, c, teta1)],
            [dParcial(3, 'a', a, b, c, teta2), dParcial(3, 'b', a, b, c, teta2), dParcial(3, 'c', a, b, c, teta2)]
        ]

        inv_jx = np.linalg.inv(jx)

        dx = np.dot((inv_jx * -1), fx)

        for i in range(0, len(x)):
            x[i] = x[i] + dx[i][0]

        r = np.linalg.norm(dx) / np.linalg.norm(x)
        n_it += 1

        print('R da iteração ' + str(n_it) + ': ' + str(r))
        print('-' * 30)

        # print('f(x): ')
        # print(fx)
        # print('-' * 30)

        # print('Jacobiano(x): ')
        # print(jx)
        # print('-' * 30)

        # print('Inversa do Jacobiano(x): ')
        # print(inv_jx)
        # print('-' * 30)

        # print('DeltaX: ')
        # print(dx)
        # print('-' * 30)

        print('c2, c3 e c4: ' + str(x[0]) + ', ' + str(x[1]) + ', ' + str(x[2]))

        print('=' * 30)

        inv_jx = []
        dx = []

    return 0


def met_broyden(vetorX, teta1, teta2, tolM):
    x = vetorX[:]

    r = 100
    n_it = 0
    while r > tolM:
        a = x[0]
        b = x[1]
        c = x[2]
        fx = [[fun1(a, b, c, 1)], [fun2(a, b, c, teta1)], [fun3(a, b, c, teta2)]]

        jx = [
            [dParcial(1, 'a', a, b, c, 1), dParcial(1, 'b', a, b, c, 1), dParcial(1, 'c', a, b, c, 1)],
            [dParcial(2, 'a', a, b, c, teta1), dParcial(2, 'b', a, b, c, teta1), dParcial(2, 'c', a, b, c, teta1)],
            [dParcial(3, 'a', a, b, c, teta2), dParcial(3, 'b', a, b, c, teta2), dParcial(3, 'c', a, b, c, teta2)]
        ]

        inv_jx = np.linalg.inv(jx)

        dx = np.dot((inv_jx * -1), fx)

        for i in range(0, len(x)):
            x[i] = x[i] + dx[i][0]

        f1 = [[fun1(a, b, c, 1)], [fun2(a, b, c, teta1)], [fun3(a, b, c, teta2)]]

        y = [[], [], []]
        for i in range(0, len(y)):
            y[i].append(f1[i][0] - fx[i][0])

        r = np.linalg.norm(dx) / np.linalg.norm(x)
        n_it += 1

        print('=' * 30)
        print('R da iteração ' + str(n_it) + ': ' + str(r))
        print('-' * 30)

        # print('f(x): ')
        # print(fx)
        # print('-' * 30)

        # print('Jacobiano(x): ')
        # print(jx)
        # print('-' * 30)

        # print('Inversa do Jacobiano(x): ')
        # print(inv_jx)
        # print('-' * 30)

        # print('DeltaX: ')
        # print(dx)
        # print('-' * 30)

        print('c2, c3 e c4: ' + str(x[0]) + ', ' + str(x[1]) + ', ' + str(x[2]))

        print('=' * 30)

        inv_jx = []
        dx = []

    return 0