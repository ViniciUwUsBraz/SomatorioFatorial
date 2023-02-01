tamanho=int(input("Digite o tamanho do array: "))
frase = [0] * tamanho

while(tamanho<1 or tamanho>100):
    tamanho=int(input("Tamanho invalido digite novamente: "))

for i in range(tamanho):
    x = int(input(),base=16)
    while(x<97 or x>122):
        x= int(input("Valor invalido digite novamente: "),base=16)
    y = chr(x)
    frase[i] = y

print(''.join(frase))
