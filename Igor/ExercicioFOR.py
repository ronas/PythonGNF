
# Calculo de IMC
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador : Ronaldo
#
# Aula de FOR

#Comentários maiores '''
'''
pets = ['cachorro','gato','coelho','mercol']

for meupet in pets:
    print(meupet)
  if meupet == "cachorro":
    print ("Favorito!")
'''
'''#Substituição de letra com acento
nome = "Rogério Olimpio da Sélva"
print (nome)
        
for letra in nome:
    if letra == "é":
        print("e")
    
    if letra != "é": 
        print(letra)
 Repetição de Numeração
for numero in range(10):
    print (numero)
'''
total = 0

for numero in range(1,1001):
    total = total + numero
    print (numero)
    
print ("total : ",total)

