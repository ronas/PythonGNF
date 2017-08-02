
import random

sorteados = []


while(len(sorteados)<20):
    bola = random.randint(1,99)
    if bola not in sorteados :
        sorteados.append(bola)
                    
print(sorteados)    