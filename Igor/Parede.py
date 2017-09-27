# Mercadinho Do Osama Promoção
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Mercadinho Do Osama Promoção
# Data: Não estive presente nesta aula, fazendo atraves dos exercicios dos colegas.

altura = float(input("Qual a altura de sua parede ?"))
#
largura = float(input("Qual a largura de sua parede ?"))
#
area = altura * largura
#
totaldegaloes = area / 165
#
resto = totaldegaloes - int(totaldegaloes)
#
if resto != 0:
    totaldegaloes = totaldegaloes + 1
#
print("Você ira precisar de :",int(totaldegaloes))    
