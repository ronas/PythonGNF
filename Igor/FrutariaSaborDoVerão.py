# Frutaria Sabor Do Verão
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Frutaria Sabor Do Verão
# Data: 08/11/2016
'''
Ordem do Exercicio

1º Declarar lista.
2º Ler a variável Item através do comando input.
3º Fazer FOR com variável para ler ListaItens e comparar.
com IF. Se FOR igual, parar com o BREAK.
4º O valor da variável INDICE,será utilizada na leitura da LISTAPREÇO.
5º Print do PREÇO.
'''
#Comentários maiores '''

ListaItens = ["Maça","Mamão","Melão","Banana","Uva"]
#
ListaPreço = [10.0,12.0,6.50,2.0,18.0]
#
Frutas = input("Que fruta você Gostaria ? ")
#
for indice in range(0,5):
    print(indice)
    if Frutas == ListaItens [indice]:
        break

print ("Valor da Fruta :",ListaPreço [indice])
        
    
