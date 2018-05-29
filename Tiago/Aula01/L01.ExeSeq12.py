#Você foi contratado para desenvolver um programa que realizada cálculo 
#de capacidade de carga máxima de caminhões. O seu programa deve ser capaz de informa quantas 
#caixas do produto XPTO cabem no caminhão, sendo os dados do produto:

#a) Altura: 18cm. 
#b) Largura: 20cm. 
#c) Profundidade: 35cm. 
#d) Peso: 1,3 Kg.
#e) Carga Max.Nominal


#1] Perguntar dados da caçamba do caminhão.     a) Altura     b) Largura.     c) Profundidade.     d) Carga Máxima Nominal.     
#2] Calcular quantidade de caixas enfileiradas horizontalmente:     Qtde1 = Largura Caçamba / Largura Produto.     
#3] Calcular quantidade de caixas empilhadas:     Qtde2 = Altura Caçamba / Altura Produto.     
#4] Calcular quantidade de caixas enfileiradas na profundidade:     Qtde3 = Profundidade Caçamba / Profundidade Produto.
#5] Quantidade máxima de caixas:     Qtde4 = Carga Máxima Nominal / Peso Produto.     
#6] Mostrar todos os resultados.

#Dados ddo produto
alt_prod = 18
larg_prod = 20
prof_prod = 35
peso_prod = 1.3
car_nominal = 100.000

#Dados da Caçamba
alt_cac = float(input('Digite a altura da caçamba: '))
larg_cac = float(input('Digite a largura da caçamba: '))
prof_cac = float(input('Digite a profundidade da caçamba: '))


qtda2 = larg_cac / larg_prod
qtda1 = alt_cac / alt_prod
qtda3 = prof_cac / prof_prod
qtda4 = car_nominal / peso_prod

print ('A quantidade de caixas enfileiradas horizontalmente é: ' , qtda2)
print ('A quantidade de caixas empilhadas é: ' , qtda1)
print ('A quantidade de caixas enfileiradas na profundidade é: ' , qtda3)
print ('A Quantidade máxima de caixas no caminhão é: ' , qtda4)