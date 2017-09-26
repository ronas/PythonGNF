
print("Se for votar no candidato A coloque 100")

print("Se for votar no candidato B coloque 101")

print("Se for votar no candidato C coloque 102")



CandidatoA = 0

CandidatoB = 0

CandidatoC = 0



for numero in range (0,99999):
    voto = int(input("Qual é o seu voto? "))
    if (voto == 100) :
        CandidatoA = CandidatoA + 1
        
    if (voto == 101) :
        CandidatoB = CandidatoB + 1
        
    if (voto == 102) :
        CandidatoC = CandidatoC + 1
     
    if (voto == 0) :
        break   


print ("O número de pessoas que votaram no candidato A foi: ", CandidatoA)

print ("O número de pessoas que votaram no candidato B foi: ", CandidatoB)

print ("O número de pessoas que votaram no candidato C foi: ", CandidatoC)
    
if (CandidatoA == CandidatoB and CandidatoA == CandidatoC and CandidatoB == CandidatoC) :
    print("Houve um empate entre o Candidato A, B e C")   

if (CandidatoA == CandidatoC) :
    print("Houve um empate entre o Candidato A e C")  
         
if (CandidatoA == CandidatoB) :
    print("Houve um empate entre o Candidato B e A")            

if (CandidatoB == CandidatoC) : 
    print("Houve um empate entre o Candidato B e C")       

if (CandidatoA > CandidatoB and CandidatoA > CandidatoC) :
    print("O Candidato A venceu")
    
if (CandidatoB > CandidatoA and CandidatoB > CandidatoC) :
    print("O Candidato B venceu")
    
if (CandidatoC > CandidatoB and CandidatoC > CandidatoA) :
    print("O Candidato C venceu")    
    