from inputs import cria_matriz, cria_vetor, ordemN, icod, idet, tolM
from metodos import dec_LU, dec_Cholesky, proc_Jacobi, proc_Gauss_Seidel
from sup import finaliza

#Inputs do programa
var_ordemN = ordemN()
var_icod = icod()
var_idet = idet()
if var_icod == 3 or var_icod == 4:
    var_tolM = tolM()

A = cria_matriz(var_ordemN)
B = cria_vetor(var_ordemN)

if var_icod == 1:
    dec_LU(A, B, var_ordemN, var_idet)
elif var_icod == 2:
    dec_Cholesky(A, B, var_ordemN, var_idet)
elif var_icod == 3:                                                                                        
    proc_Jacobi(A, B, var_ordemN, var_idet, var_tolM)
elif var_icod == 4:
    proc_Gauss_Seidel(A, B, var_ordemN, var_idet, var_tolM)

finaliza()