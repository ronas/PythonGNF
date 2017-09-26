altura = float(input("Qual a altura da parede:"))

largura = float(input("Qual a largura da parede:"))

area = altura * largura

tintaprecisa = area / 165

resto = tintaprecisa - int(tintaprecisa)

if resto != 0:
    tintaprecisa = tintaprecisa + 1

print ("Os galões precisos serão:",int(tintaprecisa))





