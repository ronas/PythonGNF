#Faça um Programa que verifique se uma letra digitada é "F" ou "M"*.
#Conforme a letra escrever: **F - Feminino, M - Masculino, Sexo Inválido**.

#print ("Identificação de F para 'Feminino' e M para 'Masculino'")

sexo = input('Digite M ou F: ')

if sexo == 'M':
    print ('Masculino')

elif sexo == 'F':
    print ('Feminino')

else:
    print ('Gênero Inválido')