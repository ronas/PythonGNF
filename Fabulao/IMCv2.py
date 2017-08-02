# Calculo IMC
# Autor: Artur Sanches
#
# Calculo de IMC com entrada pelo usuario.
#
# Strings   - Substituicao de caracteres
#           - Impressao formatada dos dados.
#
# Leitura dos dados do teclado ...
altura = input("Digite a sua altura: ")
peso   = input("Digite o seu peso: ")

# Tratamento da entrada do usuario ...
altura = altura.replace(",", ".")
peso   = peso.replace(",", ".")

# Conversao dos valores de texto para nomerico (ponto flutuante) ...
altura = float(altura)
peso   = float(peso)

# Calculo de IMC ...
IMC = peso / (altura * altura)

# Apresentacao do resultado ...
print ("O indice de IMC e: ", IMC)
print ("O indice de IMC e: %6.2f" % IMC)

# Apresenta a faixa de enquadradamento ...
if IMC < 17.00 :
    print ("Muito abaixo do peso!")
  
if IMC >= 17.00 and IMC <= 18.49 :
    print ("Abaixo do peso") 
    
if IMC >= 25 and IMC <= 29.99 :
    print ("Voce esta gordo!")
    
if IMC >= 30 and IMC <= 34.99 :
    print ("Caraca obesidade!")

if IMC >= 35 and IMC <= 39.99 :
    print ("Ta tao obeso que parece um elefante")
    
if IMC >= 40 :
    print ("Meu Deus a obesidade e tanta que nem da pra ver a cabeca")         
    
    

