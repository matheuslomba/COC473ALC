import numpy as np

def finaliza():
    # Impede que o terminal feche automaticamente assim que o programa finaliza.
    input('Pressione qualquer tecla para finalizar...')

def sim_def_pos(matriz, ordemN):
    return def_pos(matriz) and simetrica(matriz, ordemN)

def def_pos(matriz):
    return np.all(np.linalg.eigvals(matriz) > 0)

def simetrica(matriz, ordemN):
    matrizt = np.transpose(matriz)
    for i in range(0, ordemN-1):
        for j in range(0, ordemN - 1):
            if matrizt[i][j] == matriz[i][j]:
                return True
            else:
                return False

def not_diag_dom(matriz, ordemN):
    for i in range(0, ordemN):
        a = 0
        b = 0
        for j in range(0, ordemN):
            if i == j:
                a = matriz[i][j]
            else:
                b += matriz[i][j]
        if a < b:
            print("A matriz A inputada não é diagonal dominante e, portanto, a condição para convergência da solução não é atendida.\nFavor inputar novamente uma matriz válida.")
            return False
    for j in range(0, ordemN):
        a = 0
        b = 0
        for i in range(0, ordemN):
            if i == j:
                a = matriz[i][j]
            else:
                b += matriz[i][j]
        if a < b:
            print("A matriz A inputada não é diagonal dominante e, portanto, a condição para convergência da solução não é atendida.\nFavor inputar novamente uma matriz válida.")
            return False

def singular (matrizA):
    if np.linalg.det(matrizA) == 0:
        return True
    else:
        return False

