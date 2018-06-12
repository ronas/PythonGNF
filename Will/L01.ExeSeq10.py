
sexo = input('qual seu sexo:')
peso = float(input("qual e o seu peso"))
altura = float(input("qual e a sua altura"))
#PI = IMC desejado x (Altura x Altura)
#PI = 21 x (1,76 x 1,76)
#PI = 21 x 3,09
#PI = 64,9 kg
IMC = peso/(altura*altura)
IMC = float(IMC)

if sexo == "homem":
    print "seu IMC e: ", IMC
if sexo == "mulher":
    print "nada"

