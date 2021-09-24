#!/home/heidi/Computadores/Metodos Numericos/Tarea1

N=int(raw_input('Ingrese un numero natural N='))
calculo=0

primos=[]
primos.append(2)

for i in range(2,N):
        contador=0
        for j in range(len(primos)):
                calculo+=1
                p=i%primos[j]
                if (p==0):
              		contador=1
			break
        if(contador==0):
                primos.append(i)
print primos
print 'El numero de calculos es calculos=%d'%calculo
