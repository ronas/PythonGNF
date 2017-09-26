import bancodadoslib

varfim = "n"

while varfim != "s":
    codigo = input("Digite o código de barras:")
    nome = input("Digite o nome do produto:")
    valor = input("Digite o valor do produto:")
    varfim = input("Quer terminar")
    bancodadoslib.GravarRegistro(codigo,nome,valor)

