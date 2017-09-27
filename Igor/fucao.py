# Ler Arquivo
# Autor: Igor Nunes
# Materia: Curso Programar em Python
# Orientador : Ronaldo
#
# Exercicio: Fução 1
# Data:24/01/2017

def multip(n1,n2):
    vart = n1 * n2
    return vart;

def lerNumero(MSG):
    varleitura = float(input(MSG))
    return varleitura;

def Quadrado(n1):
    varx = n1*n1
    return varx;

lernumero1 = lerNumero("Digite o primeiro numero:")
#lernumero2 = lerNumero ("Digite o segundo numero:")

#varm = lernumero1 * lernumero2 : usando o def
#varm = multip(lernumero1)

#print ("Seu resultado é : ", varm) 

print(Quadrado(lernumero1))