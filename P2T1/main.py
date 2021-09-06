from inputs import recebeParams, criaVetor, icod, tolM
from metodos import met_newton, met_broyden
from sup import finaliza

#Inputs do programa
var_teta1, var_teta2 = recebeParams()
vetorX = criaVetor()
var_icod = icod()
var_tolM = tolM()

if var_icod == 1:
    met_newton(vetorX, var_teta1, var_teta2, var_tolM)

elif var_icod == 2:
    met_broyden(vetorX, var_teta1, var_teta2, var_tolM)

finaliza()