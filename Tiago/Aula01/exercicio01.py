#Exercicio 01
#Autor Tiago
#Aula de hoje - comando print e input.
import os
os.system("clear") # Aqui chama o comando para excluir informações que o usuário não precisa visualizar.
#print("hello world")
varNome=input ("Digite seu nome:") #Variavel criada para pedir informaçao.(usuario digita a informacao)
#print(varNome)            
varIdade=input ("Digite sua Idade:")
#print(varIdade)
varSexo=input ("Digite seu Sexo:")
#print(varSexo)

varPrecoUnitario=float (input("Preco")) # 20 - Converção de texto para numeros, chamando a biblioteca responsavel pela conversão.
varQtde=float (input("Quantidade"))     # 10 - Quantidade
varTotal=varPrecoUnitario*varQtde       # Calculo=Multiplica Unitario x Quantidade 
print (varTotal)           
varTotal_imp=varTotal+((varTotal/100)*36)    #porcentagem..imposto de 36%
print ("Valor Total com impostos 36%:" ,  varTotal_imp) #Tras o resultado da informação na tela do usuario.