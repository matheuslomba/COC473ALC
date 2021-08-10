from inputs import cria_matriz, ordemN, icod, idet, tolM
from metodos import met_potencia, met_jacobi
from sup import finaliza

#Inputs do programa
var_ordemN = ordemN()
var_icod = icod()
var_idet = idet()
var_tolM = tolM()
A = cria_matriz(var_ordemN)

if var_icod == 1:
    met_potencia(A, var_ordemN, var_idet, var_tolM)
elif var_icod == 2:
    met_jacobi(A, var_ordemN, var_idet, var_tolM)

finaliza()