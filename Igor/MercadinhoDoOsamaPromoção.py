# Mercadinho Do Osama Promoção
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Mercadinho Do Osama Promoção
# Data: Não estive presente nesta aula, fazendo atraves dos exercicios dos colegas.

# Programa Mercadinho Do Osama Promoção

Total = 0
Preco = 1

while Preco != 0 :
    preco = float(input("Preco = Digite o seu Preco ?"))
    Total = Total + preco
print ("O Valor Total é : ", Total)
ValorEmDinheiro = float(input("O Valor Em Dinheiro é :"))
print("Seu Troco é :",ValorEmDinheiro - Total)

if Total > ValorEmDinheiro :
    print("Valor Insuficiente.")
