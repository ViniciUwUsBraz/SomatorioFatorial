import math

n=int(input("Digite um numero: "))
inputsalvo=n
contador=0
subtracao=0
operacao=0

while(n>0):  
    if(math.factorial(contador)>n):
        subtracao=math.factorial(contador-1)
        n = n-subtracao
        operacao+=1
        contador=1   
    contador+=1

    print("Total:",n,"Fatorial do contador",math.factorial(contador), "Contador",contador )
print("Numero escolhido",inputsalvo,"Operações minimas",operacao)