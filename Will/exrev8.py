import os
os.system("clear")


peso = input("digite o seu peso: ")
if not peso.isdigit():
    print("Digite apenas numeros!")
altura = input("digite a sua altura: ")
if not altura.isdigit():
    print("Digite apenas numeros!")

peso = float(peso)
altura = float(altura)

IMC = peso / (altura * altura)
print("Seu IMC É: ", IMC)

if IMC >= 16 and IMC <= 16.9:
    print("muito abaixo do peso")
elif IMC >= 17 and IMC <= 18.4:
    print("abaixo do peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("peso normal")
elif IMC >= 25 and IMC <= 29.9:
    print("acima do peso")
elif IMC >= 30 and IMC <= 34.9:
    print("obesidade grau 1")
elif IMC >= 35 and IMC <= 40:
    print("obesidade grau 2")
elif IMC > 40:
    print("obesidade grau 3")