from random import randint
n=int(input('Numarul de elemente:'))
k=[]
sp=[]
sn=[]
k.extend([randint(-50,50) for x in range(n)])
sp.extend([k[i] for i in range(len(k)) if k[i]>=0])
sn.extend([k[i] for i in range(len(k)) if k[i]<0])
print('Valorile date:',k)
print("Suma valorilor pozitive=", sum(sp))
print('Suma valorilor negative=', sum(sn))