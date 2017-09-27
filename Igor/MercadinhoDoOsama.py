# Mercadinho Do Osama
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Mercadinho Do Osama
# Data: Não estive presente nesta aula, fazendo atraves dos exercicios dos colegas.

# Programa Mercadinho Do Osama

Total = 0

for Contador in range (1,99999) :
    Preco = float(input("Preco = Digite o Preco :"))
    
    if Preco == 0 :
        break
    Total = Total + Preco
print ("O Valor Total é :", Total)
ValorEmDinheiro = float(input("O Valor Em Dinheiro é : "))
print ("O Seu Troco é :", ValorEmDinheiro - Total)
#
if Total > ValorEmDinheiro : 
    print ("Valor Insuficiente...")