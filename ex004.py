r = "S"
while r == "S":
    a = int(input("Digite a quantidade de votos do candidato A: "))
    b = int(input("Digite a quantidade de votos do candidato B: "))
    c = int(input("Digite a quantidade de votos do candidato C: "))
    r = str(input("Para sair Precione [S]. "))
    if a > b and a > c:
        print("O candidato \033[30;42mA\033[m Venceu com {} votos.".format(a))
    if b > a and b > c:
        print("O candidado \033[30;42mB\033[m venceu com {} votos.".format(b))
    if c > a and c > b:
        print("O candidato \033[30;42mC\033[m venceu com {} votos.".format(c))
print("Fim da eleição.")
