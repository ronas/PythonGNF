LarguraParede = input ("Digite a largura da Parede: ")
AlturaParede = input ("Digite a altura da parede: ")
LarguraBloco = input ("Digite a largura do bloco: ")
AlturaBloco = input ("Digite a altura do bloco: ")
LarguraParede = float (LarguraParede)
AlturaParede = float (AlturaParede)
LarguraBloco = float (LarguraBloco)
AlturaBloco = float (AlturaBloco)
QtdeBlocosFileira = LarguraParede / LarguraBloco
QtdeFileira = AlturaParede / AlturaBloco
QtdeTotalBlocos = QtdeBlocosFileira * QtdeFileira
print ("Qtde de bloco por fileira é: ",QtdeBlocosFileira)
print ("Qtde de Fileira é: ",QtdeFileira)
print ("Total de blocos é: ",QtdeTotalBlocos)



