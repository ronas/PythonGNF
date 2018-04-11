# Autor: Igor Nunes
# Materia: Programa Python
# Orientador : Ronaldo
# Data : 10/04/2018
# Exercicio: L02.Exeseq04.py
# Atividade: Faça um programa que peça as 4 notas bimestrais e* **mostre a média**.
# Comentários maiores ""
# Estrutura de decisão
# caso 4 <= média < 6 -> Nota Recuperação
# caso 6 <= média < 8 -> Nota Aprovado
# caso 8 <= média < 10 -> Nota Aprovado
#
Nome = input("Nome do Aluno: ")
NomeProfessor = input("Nome do Professor: ")
#
Numero1 = float(input ("Digite o primeiro prova1: "))
Numero2 = float(input ("Digite o segunda prova2: "))
Numero3 = float(input ("Digite o terceira prova3: "))
Numero4 = float(input ("Digite o quarta prova4: "))
#
Resultado = (Numero1 + Numero2 + Numero3 + Numero4)/4
#
#Apresentação do resultado com casas decimais...
print ("O indice de Resultado é: %4.1f" % Resultado) 
#
if Resultado >= 4 and Resultado <= 6 :
    print("Reprovado")
    
if Resultado >= 6 and Resultado <= 8 :
    print("Recuperação")
    
if Resultado >= 8 and Resultado <= 10 :
    print ("Aprovado")