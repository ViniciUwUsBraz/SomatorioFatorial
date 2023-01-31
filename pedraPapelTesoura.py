n=int(input())
v=[]

for i in range(n):
    s,r=input().split()
    if(s==r):
        v.append('e')
    if(s=='pedra'and (r=='tesoura' or r=='lagarto')):
        v.append('s')
    if(s=='papel' and (r=='pedra' or r=='spock')):
        v.append('s')
    if(s=='tesoura' and (r=='papel' or r=='lagarto')):
        v.append('s')
    if(s=='spock' and (r=='tesoura' or r=='pedra')):
        v.append('s')
    if(s=='lagarto' and(r=='spock' or r=='papel')):
        v.append('s')
    if(r=='pedra'and (s=='tesoura' or s=='lagarto')):
        v.append('r')
    if(r=='papel' and (s=='pedra' or s=='spock')):
        v.append('r')
    if(r=='tesoura' and (s=='papel' or s=='lagarto')):
        v.append('r')
    if(r=='spock' and (s=='tesoura' or s=='pedra')):
        v.append('r')
    if(r=='lagarto' and(s=='spock' or s=='papel')):
        v.append('r')

for i in range(n):
    if(v[i] =='e'):
        print("empate")
    if(v[i]=='s'):
        print("sheldon")
    if(v[i]=='r'):
        print("rajesh")
