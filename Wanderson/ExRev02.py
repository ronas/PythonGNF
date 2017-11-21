
Altura = input ("Qual a altura?:")
Largura = input ("Qual a largura?:")
Profundidade = input ("Qual a profundidade?:")

Altura = Altura.replace (",",".")
Largura = Largura.replace (",",".")
Profundidade = Profundidade.replace (",",".")

Altura = float (Altura)
Largura = float (Largura)
Profundidade = float (Profundidade)

Volume = Altura*Largura*Profundidade

print ("Volume total:",Volume)

