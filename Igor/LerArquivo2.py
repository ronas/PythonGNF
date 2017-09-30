# Ler Arquivo
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Ler Arquivo Ready
# Data: Não estive presente nesta aula, fazendo atraves dos exercicios dos colegas.

nomearquivo = input("Qual Arquivo?")

ponteiro = open(nomearquivo,'r')

termino = "n"

while termino == "n":
    ponteiro.seek(0)
#Sempre volta a ler a primeira linha do Banco de Dados.    
    codproduto = input("Qual o codigo do Produto ?")
    for varlinha in ponteiro:
        codbar,produto,valor = varlinha.split('|')
#('|'):Separa o itens por linha.
#split : Fala qual a sintaxe de separação.
        if codbar == codproduto:
            print(codbar)
            print(produto)
            print(valor)
            termino = input("Você deseja terminar?")
            
ponteiro.close()
        
