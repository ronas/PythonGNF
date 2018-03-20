#ler 1 numero
#ler 2 numero
#ler operacao
#usar if para escolher opeacao
#mostrar o resultado
import os
os.system("clear")

operacao = "inicio"
while operacao != "sair":
    numero1 = input("qual o primeiro numero ")
    numero2 = input("Qual o segundo numero ")
    numero1 = float (numero1)
    numero2 = float (numero2)
    operacao = input("Voce quer dividir, multiplicar, adicionar, subtrair, potencializar ou sair: ")
    total = 0
    if operacao == "dividir":
        if numero2 == 0:
            print("Não há divisão por zero")
        else:
            total = numero1/numero2
            print (total)
    elif operacao == "potencializar": 
        total = numero1 ** numero2
        print (total)
    elif operacao == "multiplicar":
        total = numero1 * numero2           
        print(total)
    elif operacao == "adicionar":
        total = numero1 + numero2
        print(total)
    elif operacao == "subtrair":
        total = numero1 - numero2
        print(total)
    elif operacao == "sair":
        break
    else:
        print("Operação inválida")
