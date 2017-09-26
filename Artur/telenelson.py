
import random

sorteados = []

for numero in range (1,21):

    bola = random.randint(1,99)
    if bola not in sorteados :
        sorteados.append(bola)
                    
print(sorteados)    
    
    