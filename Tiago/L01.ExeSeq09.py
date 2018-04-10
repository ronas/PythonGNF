# Faça um programa que pergunte quanto você ganha por hora, 
# pergunte o número de horas trabalhadas no mês e apresente*: 
# 
# 1) O total do salário no mês [bruto]. 
# 2) O valor do Imposto de Renda [11%].

valor_hora = float(input('Quanto vc ganha por hora em R$ ? '))
hora_mes = float(input('Quantas horas vc trabalha no mês? '))

total_horas = valor_hora * hora_mes #Calculando salário bruto
imp = (total_horas / 100) * 11 #Calculando imposto de renda com 11%.

print ('1) O total do Salário no mês bruto é R$:', total_horas)

print ('2) O valor do Imposto de Renda é: R$' , imp)