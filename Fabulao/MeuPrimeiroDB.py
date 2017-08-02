#Agente nunca esquece

varfim = "n"

nomearquivo = input("Qual será o nome do arquivo?")

ponteiro = open(nomearquivo,'a')

while varfim == "n":
    
    codigo = input("Qual é o código de barras?")

    nome = input("Qual o nome do produto?")
    
    preco = input("Qual é o preço do produto?")
    
    varlinha = codigo + "|" + nome + "|" + preco + "\n"
    
    ponteiro.write(varlinha)
    
    varfim = input("Você quer terminar?")
    
ponteiro.close()