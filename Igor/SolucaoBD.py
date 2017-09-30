# Ler Arquivo
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Solução BD
# Data:07/02/2017

import BancoDadoslib # Quando for importar não usar py, n final
# Nunca colocar nada antes do import
varFim="n"

while varFim == "n":
    Codigo = input("Digite Codigo?")
    Nome = input("Digite Nome?")
    Valor = input("Qual Valor?")
    BancoDadoslib.GravarRegistro(Codigo,Nome,Valor)
    varFim = input("Terminar ? s/n")