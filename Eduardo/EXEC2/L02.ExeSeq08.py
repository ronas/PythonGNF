#08 - L02.ExeSeq08.py: *As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. 
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: 
#salários até R$ 280,00 (incluindo) : aumento de 20%; 
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%; 
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%; 
#salários de R$ 1500,00 em diante : aumento de 5% 

#Após o aumento ser realizado, informe na tela:    
#o salário antes do reajuste; 
#o percentual de aumento aplicado; 
#o valor do aumento; 
#o novo salário, após o aumento. *.

salatual = float (input("Digite seu salário atual:"))


if (salatual <= 280):
    salarioNovo = salatual + (salatual * 0.2)
    print ("Aumento Percentual de 20 %\n")
    salaumentado = (salatual * 0.2)
    print ("Salario antes do reajuste: R$ \n"  , (salatual))
    print ("Valor do salario aumentado :\n" ,(salaumentado))
    print ("Salario Novo :\n" ,(salarioNovo))




if (salatual >= 280.1) and (salatual == 700):
    salarioNovo = salatual + (salatual * 0.15)
    print ("Aumento Percentual de 15 %\n")
    salaumentado = (salatual * 0.15)
    print ("Salario antes do reajuste: R$ \n"  , (salatual))
    print ("Valor do salario aumentado :\n" ,(salaumentado))
    print ("Salario Novo :\n" ,(salarioNovo))



if (salatual >= 700.1) and (salatual == 1500):
    salarioNovo = salatual + (salatual * 0.1)
    print ("Aumento Percentual de 10 %\n")
    salaumentado = (salatual * 0.1)
    print ("Salario antes do reajuste: R$ \n"  , (salatual))
    print ("Valor do salario aumentado :\n" ,(salaumentado))
    print ("Salario Novo :\n" ,(salarioNovo))



if (salatual >= 1500.1) :
    salarioNovo = salatual + (salatual * 0.05)
    salaumentado = (salatual * 0.05)
    print ("Aumento Percentual de 5%\n")
    print ("Salario antes do reajuste: R$ \n"  , (salatual))
    print ("Valor do salario aumentado :\n" ,(salaumentado))
    print ("Salario Novo :\n" ,(salarioNovo))












































