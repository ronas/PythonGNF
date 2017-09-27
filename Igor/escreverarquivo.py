# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
# Data : 13/12/2016
# Exercicio: Escrever um Arquivo.

nomeArquivo = input("Qual seu Arquivo ?")
# Entrar com o nome do arquivo

ponteiro = open(nomeArquivo,'w')
# Ponteiro = Função logico de salvar no disco "open", 
#todas as opreções realizadas com arquivo são realizadas com o ponteiro 
# O W-write = Escrever um Texto
# O R-read = Somente leitura
# O A-append = Para incluir novos arquivo 
qualtexto = input("Digite seu Texto.")
# Digitar um Texto

ponteiro.write(qualtexto)
# O comando write, e para escrever.

ponteiro.close()
# Finaliza e Salva
print("Processo Finalizado")
#Texto de Finalização