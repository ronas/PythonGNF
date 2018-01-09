# -*- coding: latin -*-
valorproduto = float(input("Digite o valor do produto:"))
quantidade = float(input("Digite o numero de produtos que serao comprados:"))
pagamento = float(input("Digite o valor do pagamento:"))
  
valorpagar = valorproduto * quantidade

if pagamento < valorpagar:
    falta = valorpagar - pagamento
    print("O valor que falta ser pago e:",falta)

if pagamento == valorpagar:
    print("Nao houve troco em sua compra.")

if pagamento > valorpagar:
    troco = pagamento - valorpagar
    print("O valor do troco e de:",troco)
