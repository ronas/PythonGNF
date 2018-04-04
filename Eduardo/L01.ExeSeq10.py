

print ("Entre com sua altura , ex.: 1.90")
print ("**----------------------------------**")
alt = float (input ("digite sua altura : "))
pes = float (input ("digite seu peso : "))


imc = pes / (alt * alt)
print ("seu IMC atual :  " , imc)

print ("Peso ideal : " , (72.7 * alt) - 58 )



