# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar*: 
# **A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
# **A mensagem "Reprovado", se a média for menor do que sete; 
# A mensagem "Aprovado com Distinção", se a média for igual a dez**.

#media >= 7 (Aprovado)
#menor > 6 (Reprovado)
#aprov_dist == 10 (Aprovado com Distinção)


nota1 = float (input ("Digite a nota1: "))
nota2 = float (input ("Digite a nota2: "))

nota_med = (nota1 + nota2)/2
print (nota_med)

if (nota_med >=7):
    print ("Aprovado")

if (nota_med <7):
    print ("Reprovado")

if (nota_med == 10):
    print ("Aprovado com distinção")