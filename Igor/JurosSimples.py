#
# Calculo de Juros Simples.
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador: Ronaldo
#
#Inicialização da variavel...
ValorTotal = float(input("Valor total: "))
#
QuantidadeDeParcelas = float(input("Quantidade de Parcelas: "))
#
PercentualDeJuros = float(input("Percentual de Juros: "))
#
JurosTotal = PercentualDeJuros * QuantidadeDeParcelas
#
TotalFinanciado = ValorTotal + ((ValorTotal / 100) * JurosTotal)
#
Numero = TotalFinanciado / QuantidadeDeParcelas
#
#Apresentação do resultado com casas decimais definidas...
#
print("Valor Total:%6.2f" % TotalFinanciado)
print("Valor da Parcelas: %6.2f" % Numero)
#