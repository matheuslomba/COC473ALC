from inputs import passo_integracao, tempo_integracao, parametros
from metodos import rkn
from sup import finaliza

#Inputs do programa
t = tempo_integracao()
h = passo_integracao()
m, c, k, a1, a2, a3, w1, w2, w3 = parametros()

rkn(h, t, m, c, k, a1, a2, a3, w1, w2, w3)

finaliza()