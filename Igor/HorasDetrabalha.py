   
#
# Calculo de Horas trabalhadas.
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador: Ronaldo
# Aula de total de horas trabalhadas
#
#Leitura dos dados do teclado...
horasTrabalhadas = input("Horas trabalhadas: ")
valorHoras = input("Valor da Horas: ")
imposto = input("imposto: ")
#
#Tratamento de entrada do usuário...
horasTrabalhadas = horasTrabalhadas.replace(  ","  ,  "."  )
valorHoras   = valorHoras.replace(",",".")
imposto   = imposto.replace(",",".")
#
#Conversão dos valores de texto para numérico (ponto flutuante)...
horasTrabalhadas = float(horasTrabalhadas)
valorHoras = float(valorHoras)
imposto = float(imposto)

totalBruto = ( horasTrabalhadas * valorHoras )

# Valor do imposto.
#imposto = 24

# Calculo de porcentagem de imposto.
impostoDevido = totalBruto * (imposto /100 ) 

#Calculo do valor liquido.
totalLiquido = (totalBruto - impostoDevido)
#
print ("totalBruto R$ ",totalBruto )
#
print ("impostoDevido",impostoDevido)
#
print("totalLiquido R$ ",totalLiquido)



