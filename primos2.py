#!/home/heidi/Computadores/Metodos Numericos/Tarea1

N=int(raw_input('Ingrese un numero natural N='))
calculo=0

for i in range(2,N):
        contador=0
	mitad=int(i)
        for j in range(2,mitad):
                calculo+=1
                p=i%j
                if (p==0):
			break
                        contador=1
        if(contador==0):
                print i

print 'El numero de calculos es calculos=%d'%calculo

