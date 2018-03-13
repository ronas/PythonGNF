# -*- coding: latin -*-
# Autor: Igor Nunes
# Materia: Curso Programação "Python"
# Orientador : Ronaldo
#
# Exercicio: Eleições 2018
# Programa Eleitoral 2018 Vereador

import os
os.system('clear')

Opcao = ''
Tiririca = 0
Marquito = 0
MulherMelao = 0

Eleitores = int(input("Quantidade de Eletores ?"))

for Contador in range (1,9999):
    
    print("[1] Tiririca, [2] Marquito, [3] MulherMelao")
    
    Votos = input("Escolha seu canditado ? ")
      
    if Votos == "0" :
        break
    if Votos == '1' :
        Tiririca = Tiririca + 1 
    if Votos == '2' :
        Marquito = Marquito + 1 
    if Votos == '3' :
        MulherMelao = MulherMelao + 1

    opcao = input ("Concluir S/N: ")
    os.system ('clear')  

if Tiririca > Marquito and Tiririca > MulherMelao :
    print ("Candidato Tiririca Eleito")
if Marquito > MulherMelao and Marquito > Tiririca :
    print ("Candidato Marquito Eleito")
if MulherMelao > Tiririca and MulherMelao > Marquito :
    print ("Candidata Mulher Melao")




  

    


        
        
        
    
