import os
os.system('clear')
opcao = ""
candidatoA = 0
candidatoB = 0
candidatoC = 0
candidatoD = 0
while opcao != 'S':
    print("Digite o seu voto:")
    voto = input("Vote no seu candidato")
    if voto == "A":
        candidatoA = candidatoA + 1
    if voto == "B":
        candidatoB = candidatoB + 1
    if voto == "C":
        candidatoC = candidatoC + 1
    if voto == "D":
        candidatoD = candidatoD + 1
    opcao = input("Se quiser sair digite 'S', se nao quiser sair digite 'N'")
    os.system('clear')

print ("Votos do candidato A = ", candidatoA)
print ("Votos do candidato B = ", candidatoB)
print ("Votos do candidato C = ", candidatoC)
print ("Votos do candidato D = ", candidatoD)