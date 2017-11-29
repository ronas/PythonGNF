nota1 = input ("Digite a nota 1: ")
nota2 = input ("Digite a nota 2: ")
nota3 = input ("Digite a nota 3: ")
nota4 = input ("Digite a nota 4: ")
nota1 = float (nota1)
nota2 = float (nota2)
nota3 = float (nota3)
nota4 = float (nota4)
MediaGeral = ((nota1 + nota2 + nota3 + nota4) / 4)
if MediaGeral >= 7: 
    print("Você foi aprovado! Média ",MediaGeral)
else:
        print ("Você foi reprovado! Média: ",MediaGeral)
#print ("A média Geral é: ",MediaGeral)
