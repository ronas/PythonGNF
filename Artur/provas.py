respostas = []

correto = 0

gabarito = []

gabarito = ['e','b','b','c','d',"e","b",'a',"d","d"]

for indice in range(0,10):
    respostas.append(input("Qual a resposta?"))
    
for indice in range(0,10):
    if gabarito[indice] == respostas[indice]:
        print("Você acertou a questão", indice)
        correto = correto + 1



print("Você tirou", correto) 

if correto >=7:
    print("Passou")
if correto <7:
    print("Reprovou")            
    