import os
os.system('clear')

LarguraParede = input ("Qual a largura da parede?:")
AlturaParede = input ("Qual a Altura da parede?:")
LarguraBloco = input ("Qual a largura do bloco?:")
AlturaBloco = input ("Qual a altura do bloco?:")

LarguraParede = LarguraParede.replace (",",".")
AlturaParede = AlturaParede.replace (",",".")
LarguraBloco = LarguraBloco.replace (",",".")
AlturaBloco = AlturaBloco.replace (",",".")

LarguraParede = float (LarguraParede)
AlturaParede = float (AlturaParede)
LarguraBloco = float (LarguraBloco)
AlturaBloco = float (AlturaBloco)

QtdeBlocosFileira = LarguraParede / LarguraBloco
QtdeFileiras = AlturaParede / AlturaBloco

print ("A quantidade de blocos por fileira é:", QtdeBlocosFileira)
print ("A quantidade de fileiras é:", QtdeFileiras)
