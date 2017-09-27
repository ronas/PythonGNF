# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
# Data : 20/12/2016
# Exercicio: O fumo .

'''
   Fazendo uma regra de três chegamos que 144 cigarros tiram 1 dia
   de vida da pessoa (1 dia = 1440 minutos = 144 cigarros)
'''
cigarros = int(input('Cigarros por dia: '))
anos = int(input('Anos fumados: '))
total_cigarros = anos * 365 * cigarros
dias_perdidos = total_cigarros / 144
print ('Você perdeu aproximadamente %.2f ' %dias_perdidos)
