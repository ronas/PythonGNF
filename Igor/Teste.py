#Teste
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador : Ronaldo

#Exercicio: Teste de Prova

#Comentários maiores '''

#

Respostas = []

Correto = 0 

Gabarito = ["a","d","e","f","n","b","L","r","z","n","q"]

for indice in range(0,10):
          
        Respostas.append(input("Qual a Respostas?"))
   
print ("Respostas :", Respostas )

#Decisão de Gabarito e Resposta

for indice in range(0,9):
    if Gabarito[indice]==Respostas[indice]:      
        Correto=Correto+1
   
print ("Correto :", Correto )

# print de Aprovado e Reprovado.

if Correto >=7:
    print("Aprovado:")

if Correto <=7:
    print("Reprovado:")

    
