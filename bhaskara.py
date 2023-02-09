import math

a,b,c= map(float,input().split())
delta= round((b*b),2) - (4*a*c)
if delta>0 and a!=0:
    bhaskarap= (-b +math.sqrt(delta))/ (2*a)
    bhaskaran= (-b -math.sqrt(delta))/ (2*a)
    print("R1 = %.5f\nR2 = %.5f" %(bhaskarap,bhaskaran))
else:
    print("Impossivel calcular")