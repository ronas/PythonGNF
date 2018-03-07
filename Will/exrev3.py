larguraParede = input("diga a largura da parede")
alturaParede = input("diga a altura da parede")
larguraBloco = input("diga a largura do bloco")
alturaBloco = input("diga a largura do bloco")
larguraParede = float (larguraParede)
alturaParede = float (alturaParede)
larguraBloco = float (larguraBloco)
alturaBloco = float (alturaBloco)
qtdeBlocosFileira = larguraParede/larguraBloco
qtdeFileiras = alturaParede/alturaBloco

print ("A quantidade de blocos por fileira é ", qtdeBlocosFileira)
print ("A quantidade de fileiras é ", qtdeFileiras)
