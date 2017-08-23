

nomearquivo = input("Qual arquivo desejas ler?")

ponteiro = open(nomearquivo,'r')


codproduto = 13


while codproduto != "termino":
    ponteiro.seek(0)
    codproduto = input("Qual o código de barrras?")
    for varlinha in ponteiro:
        codbar,produto,valor = varlinha.split('|')
        if codbar == codproduto:
            print(codbar)
            print(produto)
            print(valor)
          
     
#    print(varlinha)

#varlinha = ponteiro.readline()
        
ponteiro.close()
#termino = "n"

#while termino == "n":
#    ponteiro.seek(0)
#    codproduto = input("Qual o código de barrras?")
#    for varlinha in ponteiro:
#        codbar,produto,valor = varlinha.split('|')
#        if codbar == codproduto:
#            print(codbar)
#            print(produto)
#            print(valor)
#            termino = input("Você quer terminar?")