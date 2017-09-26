respostas = []

gabarito = []

nota = 0

gabarito = ['c','d','b','d','a','c','d','b','d','d']

for indice in range(0,10):
    respostas.append(input("Qual é a resposta?"))
    
for indice in range(0,10):
    if gabarito[indice] == respostas[indice]:
        print("Você acerto a questão", indice)
        nota = nota + 1
        
print("Você tirou", nota)         
