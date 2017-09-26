total = 0

preco = 1

while preco != 0:
    
    preco = int(input("Qual é o preço? "))
    
    if (preco > 0 ) :
        total = total + preco

        

    
print("O preço total é:", total)
print("O preço total é: %6.2f" % total)

valorpago = int( input("Qual foi o valor pago: ") )

troco = valorpago - total

print("O troco é:", troco)
print("O troco é: %6.2f" % troco)

if troco > 0 :
    print ("Aqui esta o troco")
    
if total > valorpago :
    print ("Você não possui dinheiro suficiente")    