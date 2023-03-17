import os
import time


a=int(input("Digite quanto tempo quer ficar parado: "))
aux=0
segundos=0
minutos=0
horas=0
while(aux<=a):
    if(segundos==60):
        minutos+=1
    if(minutos==60):
        minutos=-0
        horas+=1
    if(segundos%60==0 and segundos!=0):
        segundos=0
    os.system('clear')
    print("Cronometro: %02i:%02i:%02i "%(horas,minutos,segundos))
    time.sleep(1)
    segundos+=1
    aux+=1
