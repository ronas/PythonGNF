print ("Compre agora na frutaria do Silvão!")

print ("PROXIMO!")

listaitens = []

listapreco = []

listaitens = ["7121100001","7897254171159","7891342010757","7896322700789","7897147500219"]

listapreco = [100.0,120.0,60.5,20.0,180.0]

item = input("Qual item o senhor deseja: ")

for indice in range(0,10):

    if item == listaitens[indice]:
        break

print("Você tera que pagar:", listapreco[indice])