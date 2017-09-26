
ValorTotal = float(input("Valor total: "))

QuantidadeDeParcelas = float(input("Quantidade de Parcelas: "))

PercentualDeJuros = float(input("Percentual de Juros: "))

JurosTotal = PercentualDeJuros * QuantidadeDeParcelas

TotalFinanciado = ValorTotal + (( ValorTotal / 100) * JurosTotal)

Numero = TotalFinanciado / QuantidadeDeParcelas

print("Valor Total: ", TotalFinanciado)
print("Valor Total: %6.2f" % TotalFinanciado)
print("Valor da Parcela: ", Numero)
print("Valor da Parcela: %6.2f" % Numero)

