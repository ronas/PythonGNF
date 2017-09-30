#
# Calculo de Ler Idades.
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador: Ronaldo
#
#Inicialização da variavel...
Maiores = 0
#
#lupe de repetição...

for numero in range(10):
    Idade = int(input("Qual a sua idade ? "))
    if (Idade >= 18) :
        Maiores = Maiores + 1 
#        
print ("total : ", Maiores)
#