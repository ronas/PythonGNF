# Mercadinho Do Osama Promoção
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Mercadinho Do Osama Promoção
# Data: Não estive presente nesta aula, fazendo atraves dos exercicios dos colegas.

print ("Compre agora na frutaria do Pedrão!")

print("Proximo!")

ListaItens = []
#
ListaPreço = []
#
Listaitens = ["7121100001","7897254171159","7891342010757","7896322700789","7897147500219"]
#
Listapreço = [120.0,140.0,230.0,20.0,130.0]
#
item = input("Qual item o senhor deseja:")
#
for indice in range(0,10):
    if item == Listaitens[indice]:
        break
#
print("Você tera que pagar:", Listapreço[indice])            
    
    
    
    