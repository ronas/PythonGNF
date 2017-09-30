# Eleições 2016 Vereador
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Eleições 2016
# Data: Não estive presente nesta aula, fazendo atraves dos exercicios dos colegas.

# Programa Eleitoral 2016 Vereador

Tiririca = 0
Marquito = 0
MulherMelão = 0

Eleitores = int(input("Quantidade de Eletores ?"))

for Contador in range (1,9999):
    Votos = input("Qual seu Voto ?")
    if Votos == "0" :
        break
    if Votos == '1' :
        Tiririca = Tiririca + 1 
    if Votos == '2' :
        Marquito = Marquito + 1 
    if Votos == '3' :
        MulherMelão = MulherMelão + 1
if Tiririca > Marquito and Tiririca > MulherMelão :
    print ("Candidato Tiririca Eleito")
if Marquito > MulherMelão and Marquito > Tiririca :
    print ("Candidato Marquito Eleito")
if MulherMelão > Tiririca and MulherMelão > Marquito :
    print ("Candidata Mulher Melão")
        
        
        
    
