import numpy as np
import math
from sup import finaliza, ft, ddy

# ===========================================

def rkn(h, t, m, c, k, a1, a2, a3, w1, w2, w3):
    y = 0
    dy = 0

    ti = 0
    while ti <= t:

        k1 = 1 / 2 * h * ddy(ti, y, dy, m, c, k, a1, a2, a3, w1, w2, w3)
        q = 1 / 2 * h * (dy + 1 / 2 * k1)

        k2 = 1 / 2 * h * ddy(ti + h / 2, y + q, dy + k1, m, c, k, a1, a2, a3, w1, w2, w3)

        k3 = 1 / 2 * h * ddy(ti + h / 2, y + q, dy + k2, m, c, k, a1, a2, a3, w1, w2, w3)
        L = h * (dy + k3)

        k4 = 1 / 2 * h * ddy(ti + h, y + L, dy + 2 * k3, m, c, k, a1, a2, a3, w1, w2, w3)

        y = y + h * (dy + 1 / 3 * (k1 + k2 + k3))
        dy = dy + 1 / 3 * (k1 + 2 * k2 + 2 * k3 + k4)

        print("=" * 30)
        print("Tempo = ", ti)
        print("K1 = ", k1)
        print("Q = ", q)
        print("K2 = ", k2)
        print("K3 = ", k3)
        print("L = ", L)
        print("K4 = ", k4)
        print("-" * 30)
        print("y = Deslocamento = ", y)
        print("dy = Velocidade = ", dy)
        print("ddy = Aceleração = ", ddy(ti, y, dy, m, c, k, a1, a2, a3, w1, w2, w3))

        ti += h

    return 0
