import numpy as np
import math

def finaliza():
    # Impede que o terminal feche automaticamente assim que o programa finaliza.
    input('Pressione qualquer tecla para finalizar...')

def ft(t, y, dy, a1, a2, a3, w1, w2, w3):
    return a1 * math.sin(w1 * t) + a2 * math.sin(w2 * t) + a3 * math.sin(w3 * t)

def ddy(t, y, dy, m, c, k, a1, a2, a3, w1, w2, w3):
    return (a1 * math.sin(w1 * t) + a2 * math.sin(w2 * t) + a3 * math.sin(w3 * t) - c * dy - k * y) / m