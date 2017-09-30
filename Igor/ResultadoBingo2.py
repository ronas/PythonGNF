# Resultado Bingo 2
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador : Ronaldo
#
# Exercicio Bingo 2

#Comentários maiores '''

# Usando a biblioteca Random.Randint.
# Nos comandos usar minusculas.
import random

Sorteados = []
while(len(Sorteados)<20):
# numero in range(1,20):
   
    Bola = random.randint(1,99)
#    
    if Bola not in Sorteados:      
        Sorteados.append(Bola)
   
    print ("Bola :", Bola )
    
print(Sorteados)