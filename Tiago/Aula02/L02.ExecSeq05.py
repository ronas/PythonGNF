# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar*: 
# **A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
# **A mensagem "Reprovado", se a média for menor do que sete; 
# A mensagem "Aprovado com Distinção", se a média for igual a dez**.

nota1 = input('Digite a nota1: ')
nota2 = input('Digite a nota2: ')

#media >= 7 (Aprovado)
#menor > 6 (Reprovado)
#aprov_dist == 10 (Aprovado com Distinção)

if (nota1 >=7):
    print('Aprovado')
