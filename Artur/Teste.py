x = input("Digite o primeiro número:")
y = input("Digite o segundo número:")
operacao = input("Digite a operaçao[*,/,+,-]:")



x = x.replace (",",".")
y = y.replace (",",".")

x = float(x)
y = float(y)


if operacao == '+':
    resultado = x + y
    
if operacao == '/    ':
    resultado = x / y

if operacao == '-':
    resultado = x - y
    
if operacao == '*':
    resultado = x * y    