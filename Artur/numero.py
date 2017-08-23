numero1 = int(input("Digite o primeiro número:"))

numero2 = int(input("Digite o segundo número:"))

resultado = numero1 + numero2

print("O resultado é:",resultado)

resto = numero1 % numero2

if resto == 0:
    print("O número é par")
    
if resto != 0:
    print("O número é impar")