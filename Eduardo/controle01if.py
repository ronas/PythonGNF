sal1 =  input( " Digite primeiro salario : ")
sal2 = input ("\n Digite o segundo salario: ")

sal1 = float(sal1)
sal2 = float(sal2)

if (sal1 == sal2):
    print ("\n os salarios sao iguais ")

if (sal1 > sal2):
    print ("\n salario 1 eh o maior, valor: R$  " , sal1)
    sat = sal1 - sal2 
    print ("\n Salario é maior ", sat)

if (sal1 < sal2):
    print ("\n salario 2 eh o maior, valor: R$  " , sal2)
    sat = sal2 - sal1 
    print ("\n Salario é maior ", sat)
print ("\n  FIM ----------  Parabens")

