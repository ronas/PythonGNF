#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês*. 
#Calcule e mostre o total do seu salário no referido mês**. *
#Sabendo-se que são descontados:
# *Imposto de Renda (11%), 
# *INSS (4%) e Contribuição Sindical (1%)**, *
# Faça um programa que nos dê*:     
# 
# 1] Salário bruto: Qtde de Horas * Valor Horas.     
# 2] Imposto de Renda (11%).     
# 3] INSS (4%).     
# 4] Contribuição Sindical (1%).     
# 5] Salário Líquido: Bruto - IR - INSS - CS**

valor_hora = float(input('Quanto vc ganha por hora em R$ ? '))
hora_mes = float(input('Quantas horas vc trabalha no mês? '))

total_horas = valor_hora * hora_mes #Calculando salário bruto
imp = (total_horas / 100) * 11 #Calculando imposto de renda com 11%.
inss = (total_horas / 100) * 4 #Calculando o inss de 4%.
cont_sind = (total_horas /100 ) * 1 #Calculando Contribuição Sindical de 1%.

#Calculando Salário Líquido: Bruto - IR - INSS - CS


print ('\n1) O total do Salário no mês bruto é R$: ' , total_horas)
print ('2) O valor do Imposto de Renda é: R$' , imp)
print ('3) O valor do INSS é: R$' , inss)
print ('4) O valor da Contrib.Sindical é: R$' , cont_sind)
print ('\n5) Seu salário líquido é: R$' , total_horas - imp - inss - cont_sind)