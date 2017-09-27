# 
# Autor: Igor Nunes
# Materia: Programa Python
#Orientador : Ronaldo
# Aula de if

Resultado = 0

Numero1 = float(input ("Digite o primeiro numero: "))

Operacao = input("Digite a operacao[+ - * /]:")

Numero2 = float(input ("Digite a segundo numero: "))

if Operacao == '+' :
    Resultado = Numero1 + Numero2
    
if Operacao == '-' :
    Resultado = Numero1 - Numero2
    
if Operacao == '*' :
    Resultado = Numero1 * Numero2
    
if Operacao == '/' :
    Resultado = Numero1 / Numero2
    
print ("Resultado do calculo: ", Resultado)    
