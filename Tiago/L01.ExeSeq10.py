# Tendo como dados de entrada a ALTURA e o PESO ATUAL de uma pessoa, construa um algoritmo que calcule:
# 1] IMC atual: Peso / (Altura * Altura)
# 2] Peso ideal: (72.7 * Altura) - 58
# 3] Imprimir os resultados.
print("\nEntre com os seguintes dados para calcular seu IMC atual:")

peso=float(input ('\nDigite seu Peso (Kg): '))
alt=float(input ('Digite sua altura (mt): '))

result_imc = (peso / alt * alt )
result_ideal = (72.7 * alt) - 58
print ('\nSeu IMC atual é:' , result_imc, 'Kg/m2' )
print ('Seu peso ideal é: ' , result_ideal , 'Kg' )