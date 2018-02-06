import os
os.system('clear')

ValorProduto = input ("Digite o valor do produto:")
QtdeProduto = input ("Digite a quantidade de produto")

ValorProduto = ValorProduto.replace (",",".")

ValorProduto * QtdeProduto

Pagamento = input ("Digite o valor do pagamento")

Troco = Pagamento - ValorProduto
