# dados do produto:
#em metros , peso em kg


#------------------------------------------------------------**
#valores fixos
#------------------------------------------------------------**
altp = 0.18
largp = 0.20
profunp = 0.35
pesop = 1.3
#------------------------------------------------------------**




altca = input ("Qual a altura da cacamba ?    ")     
print (" ")
largca = input ("Qual a largura da cacamba ?    ")    
print (" ")
profunca = input ("Qual a profundidade da cacamba ?    ")
print (" ")
cargmaxno = input ("Qual a carga maxima Nominal suportada ?   ")
print (" ")


#Calcular quantidade de caixas enfileiradas horizontalmente**
quant1 = largca / largp


#Calcular quantidade de caixas empilhadas **
quant2 = altca / altp 


#Calcular quantidade de caixas enfileiradas na profundidade **
quant3 = profunca / profunp


#Quantidade maxima e caixas **
quant4 = cargmaxno / pesop 


#Mostrando os resultados **
print ("**-------------------------------------------------------------------**")
print ("quantidade de caixas enfileiradas na largura:"),  (quant1)
print ("**")
print ("quantidade de caixas empilhadas (altura):"), (quant2)
print ("**")
print ("quantidade de caixas enfileiradas na profundidade:"), (quant3)
print ("**")
print ("Quantidade maxima e caixas permitidas:") , (quant4)
print ("**-------------------------------------------------------------------**")





















