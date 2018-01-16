
# Cálculo IMC
# Autor: Artur Sanches
#
# Cálculo de IMC com entrada pelo usuário.
#
# Strings   - Substituição de caracteres
#           - Impressão formatada dos dados.
#
# Leitura dos dados do teclado ...
altura = input("Digite a sua altura: ")
peso   = input("Digite o seu peso: ")

# Tratamento da entrada do usuário ...
altura = altura.replace(",", ".")
peso   = peso.replace(",", ".")

# Conversão dos valores de texto para nomérico (ponto flutuante) ...
altura = float(altura)
peso   = float(peso)

# Cálculo de IMC ...
IMC = peso / (altura * altura)

# Apresentação do resultado ...
print ("O índice de IMC é: ", IMC)
print ("O índice de IMC é: %6.2f" % IMC)

# Apresenta a faixa de enquadradamento ...
if IMC < 17.00 :
    print ("Muito abaixo do peso!")
  
if IMC >= 17.00 and IMC <= 18.49 :
    print ("Abaixo do peso") 
    
if IMC >= 25 and IMC <= 29.99 :
    print ("Você esta gordo!")
    
if IMC >= 30 and IMC <= 34.99 :
    print ("Caraca obesidade!")

if IMC >= 35 and IMC <= 39.99 :
    print ("Ta tão obeso que parece um elefante")
    
if IMC >= 40 :
    print ("Meu Deus a obesidade é tanta que nem da pra ver a cabeça")         
    
    

