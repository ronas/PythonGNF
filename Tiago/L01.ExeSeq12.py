12 - L01.ExeSeq12.py: *Você foi contratado para desenvolver um programa que realizada cálculo 
de capacidade de carga máxima de caminhões. O seu programa deve ser capaz de informa quantas 
caixas do produto XPTO cabem no caminhão, sendo os dados do produto:

a) Altura: 18cm. 
b) Largura: 20cm. 
c) Profundidade: 35cm. 
d) Peso 1,3 Kg.

1] Perguntar dados da caçamba do caminhão.     a) Altura     b) Largura.     c) Profundidade.     d) Carga Máxima Nominal.     
2] Calcular quantidade de caixas enfileiradas horizontalmente:     Qtde1 = Largura Caçamba / Largura Produto.     
3] Calcular quantidade de caixas empilhadas:     Qtde2 = Altura Caçamba / Altura Produto.     
4] Calcular quantidade de caixas enfileiradas na profundidade:     Qtde3 = Profundidade Caçamba / Profundidade Produto.     
5] Quantidade máxima de caixas:     Qtde4 = Carga Máxima Nominal / Peso Produto.     
6] Mostrar todos os resultados.

print = float(input('Digite a altura da caçamba'))
Digite a largura da caçamba
Digite a profundidade da caçamba

'\n