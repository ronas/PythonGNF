def lernumero(msg):
    varleitura = float(input(msg))
    return varleitura;

def multip(n1,n2):
    vart = n1 * n2
    return vart;

def quadrado(n1):
    varx = n1 * n1
    return varx;

numero1 = lernumero("Qual é o primeiro número?")

print(quadrado(numero1))