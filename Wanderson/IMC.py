
altura = input ("Digite a sua altura:")
peso = input("Digite o seu peso:")

altura = altura.replace(",", ".")
peso   = peso.replace(",", ".")

altura = float(altura)
peso   = float(peso)


IMC = peso / (altura * altura)


print ("O indice de IMC é:", IMC)



