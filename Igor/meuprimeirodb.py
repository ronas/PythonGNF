# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
# Data : 20/12/2016
# Exercicio: Meu Primeiro DB.
#
#Agente Nunca Esquece!!!!!!
#
varFim="n"
#
nomeArquivo = input("Qual seu Arquivo ?")
#
ponteiro = open(nomeArquivo,'a')
#
while varFim == "n":
#
    codProduto = input("Codigo Produto :")
#
    nome = input("nome :")
#
    preco = input("Preço Produto : ")
#
#varLinha =" ".join((codProduto,"#",nome,"#",preco,"\n"))
#
    varLinha = codProduto+"|"+nome+"|"+preco+"\n"
#
    ponteiro.write(varLinha)
#
    varFim = input("Terminar ? s/n")
#

ponteiro.close()
