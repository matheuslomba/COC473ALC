from sup import finaliza

# ====================
# Inputs gerais

def parametros():
    print('=' * 30)
    while True:
        try:
            m = float(input('Qual será o valor de m? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            c = float(input('Qual será o valor de c? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            k = float(input('Qual será o valor de k? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            a1 = float(input('Qual será o valor de a1? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            a2 = float(input('Qual será o valor de a2? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            a3 = float(input('Qual será o valor de a3? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            w1 = float(input('Qual será o valor de w1? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            w2 = float(input('Qual será o valor de w2? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            w3 = float(input('Qual será o valor de w3? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    return m, c, k, a1, a2, a3, w1, w2, w3


def passo_integracao():
    print('=' * 30)
    while True:
        try:
            passo = float(input('Qual será o passo de integraçao (h) em segundos? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    return passo


def tempo_integracao():
    print('=' * 30)
    while True:
        try:
            tempo = float(input('Qual será o tempo total de integraçao (0.0 a 1.0) em segundos? '))
            if tempo < 0.0 or tempo > 1.0:
                print('Favor inserir um tempo válido.')
            else:
                break
        except ValueError:
            print('Favor inserir um número float.')
    return tempo