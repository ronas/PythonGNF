



print ("**--------------------------------------------------------**")
print ("**--------------------------------------------------------**")
hora1 = float (input ("Quanto voce ganha por hora ?  "))
horaT = float ( input ("Qual o numero de horas trabalhadas no mes ?  "))

print ("**--------------------------------------------------------**")
resul = hora1 * horaT

imp = (resul) * 0.11
inss = (resul) * 0.04
cs = (resul) * 0.01


print ("**--------------------------------------------------------**")
print ("Seu salario este mes foi  de : R$",resul)

print ("Salario Liquido (-imposto, -inss, -contr sind) : R$", ((resul - imp) -inss ) -cs)
print ("**--------------------------------------------------------**")
