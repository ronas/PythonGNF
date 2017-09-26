# Média

media1 = input("Digite a media1: ")
media2 = input("Digite a media2: ")
media3 = input("Digite a media3: ")
media4 = input("Digite a media4: ")


media1 = media1.replace(",", ".")
media2 = media2.replace(",", ".")
media3 = media3.replace(",", ".")
media4 = media4.replace(",", ".")


media1 = float(media1)
media2 = float(media2)
media3 = float(media3)
media4 = float(media4)

mediafinal =  (media1 + media2 + media3 + media4) / 4

print("A media final é: ", mediafinal)
print("A media final é: %6.1f" % mediafinal)

if mediafinal < 7.0 :
    print ("Você esta com nota vermelha!")

if mediafinal >= 7.0 :
    print ("Você passou!")
    


