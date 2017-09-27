
# Eleições 2016
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Eleições 2016
# Data: Não estive presente nesta aula, fazendo atraves dos exercicios dos colegas.

# Programa Eleitoral

Dilma = 0
Bolsonaro = 0
trump = 0

Eleitores = int(input("Quantidade de Eletores ?"))

for Contador in range (1,Eleitores):
    Votos = input("Qual seu Numero ?")
    if Votos == '1':
        Dilma = Dilma + 1
    if Votos == '2' :
        Bolsonaro = Bolsonaro + 1
    if Votos == '3' :
        Trump = trump + 1
        
if Dilma > Bolsonaro and Dilma > Trump :
    print ("Candidato Dilma Eleita")
if Bolsonaro > Trump and Bolsonaro > Dilma :
    print ("Candidato Bolsonaro Eleito")   
if Trump > Dilma and trump > Bolsonaro :
    print ("CandidatoTrump Eleito")   
    