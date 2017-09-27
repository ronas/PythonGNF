# Capacidade de Carga
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador : Ronaldo
#
#Comentários maiores '''

Peso = 1 
PesoTotal = 0

CapacidadeDeCarga = float(input("Capacidade de Carga Total ? "))

while Peso != 0 :
    Peso = float(input("Peso = Digite o Peso : "))
    
    if PesoTotal + Peso >CapacidadeDeCarga:
        break
    PesoTotal = PesoTotal + Peso
    

print ("O Peso Total é :", PesoTotal)