import os
os.system('clear')

Nota1 = input ("Digite a nota1:")
Nota2 = input ("Digite a nota2:")
Nota3 = input ("Digite a nota3:")
Nota4 = input ("Digite a nota4:")

Nota1 = Nota1.replace(",",".")
Nota2 = Nota2.replace(",",".")
Nota3 = Nota3.replace(",",".")
Nota4 = Nota4.replace(",",".")

Nota1 = float (Nota1)
Nota2 = float (Nota2)
Nota3 = float (Nota3)
Nota4 = float (Nota4)

Media = (Nota1 + Nota2 + Nota3 + Nota4 ) / 4

print ("Nota final", Media) 

if Media >= 7:
    print ("Aprovado")
else:
    print ("Reprovado")




