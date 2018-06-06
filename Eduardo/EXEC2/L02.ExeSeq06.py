
#L02.ExeSeq06.py: *Faça um Programa que leia três números* e **mostre o maior deles**.



num1 = float (input("Digite o primeiro numero\n"))
num2 = float (input("Digite o segundo numero\n"))
num3 = float (input("Digite o terca numero\n"))




if (num1 > num2) and (num1 > num3):
	amaior = num1

if (num2 > num1) and (num2 > num3):
	amaior = num2

if (num3 > num2) and (num3 > num1):
	amaior = num3


if (num1 > num3 ) and (num1 < num2):
	bmeio = num1

if (num2 > num3) and (num2 <num1):
	bmeio = num2

if (num3 > num2) and (num3 < num1 ):
	bmeio = num3

if (num3 > num1) and (num3 < num2):
	bmeio = num3


if (num1 < num2) and (num1 < num3):
	cmenor = num1

if (num2 < num1) and (num2 < num3):
	cmenor = num2

if (num3 < num2) and (num3 < num1):
	cmenor = num3

if (num1 == num2) and (num2 == num3):
    amaior = num1
    bmeio = num2
    cmenor = num3
    print ("Todos sao iguais " , (amaior))

print ("maior numero é " , (amaior))

print ("Numero intermediario é " , (bmeio))

print ("O menor numero é " , (cmenor))

















