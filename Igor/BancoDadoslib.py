# Ler Arquivo
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Banco de Dados Lib
# Data:07/02/2017

def GravarRegistro (prmCodigo,
                    prmNome,
                    prmValor):
    Ponteiro = open('BancoDados.db','a')
    Ponteiro.write(prmCodigo+'|'+prmNome+'|'+prmValor+'\n')
    Ponteiro.close()
    return