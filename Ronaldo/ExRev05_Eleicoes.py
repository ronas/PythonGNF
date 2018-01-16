# -*- coding: latin -*-
import sys, os

opcao = ''
votos_candidato_a = 0
votos_candidato_b = 0
votos_candidato_c = 0
votos_candidato_d = 0

while opcao != 's':
    
    os.system("clear")
  
    print("-----------------------\n"
          "    Candidato          \n"
          "-----------------------\n"
          " a) Toninho da Pamonha \n"
          " b) Juliao da Farmacia \n"
          " c) Cleverson Pai      \n"
          " d) Dodo Malucao       \n"
          "-----------------------\n"
          " s) Sair               \n")
  
    opcao = input('Opcao: ')
    
    if opcao =='a':
        votos_candidato_a = votos_candidato_a + 1

    if opcao =='b':
        votos_candidato_b = votos_candidato_b + 1

    if opcao =='c':
        votos_candidato_c = votos_candidato_c + 1

    if opcao =='d':
        votos_candidato_d = votos_candidato_d + 1

    if opcao == 's':
        print("Processo encerrado!")
        break

os.system("clear")

print("\n\nResultado da Votacao: ")
print("---------------------------------------")

print("Toninho da Pamonha: ", votos_candidato_a)
print("Juliao da Farmacia: ", votos_candidato_b)
print("Cleverson Pai     : ", votos_candidato_c)
print("Dodo Malucao      : ", votos_candidato_d)

print("\n\n")

sys.exit(0)