horas = input("Digite as horas trabalhadas: ")
ganho = input("Digite o ganho por hora: ")

ganho = ganho.replace(",", ".")

horas = float(horas)
ganho = float(ganho)

ganhodiario = (horas * ganho) /100

ganhou = (ganhodiario * 86 )

print("Você ganhou:", ganhou)
print("Você ganhou: %6.2f" % ganhou,"R$")




