
import os
os.system('clear')
#inicialização da variável
Opcao = ''
CandidatoA = 0
CandidatoB = 0
CandidatoC = 0
CandidatoD = 0

while Opcao != 'S': 
    print ("Digite o seu voto: ")
    Voto = input ("Digite o seu candidato: ") 
    if Voto == 'A':
        CandidatoA = CandidatoA + 1
    if Voto == 'B': 
        CandidatoB = CandidatoB + 1
    if Voto == 'C':
        CandidatoC = CandidatoC + 1
    if Voto == 'D':
        CandidatoD = CandidatoD + 1
    Opcao = input ("Concluir S/N: ")
    os.system('clear')
print ("Votos do Candidato A: ", CandidatoA)
print ("Votos do Candidato B: ", CandidatoB)
print ("Votos do Candidato C: ", CandidatoC)
print ("Votos do Candidato D: ", CandidatoD)



