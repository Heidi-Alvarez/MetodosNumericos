#!/home/heidi/Computadores/Metodos Numericos/Tercera

import math
import pylab as p
from sys import exit

E1=[1.0,1.0,0.0,3.0,4.0]
E2=[2.0,1.0,-1.0,1.0,1.0]
E3=[3.0,-1.0,-1.0,2.0,-3.0]
E4=[-1.0,2.0,3.0,-1.0,4.0]
E4=[1.0, 1.0, 0.0, 3.0, 4.0]
E1=[0.0, -1.0, -1.0, -5.0, -7.0]
E2=[0.0, 0.0, 3.0, 13.0, 13.0]
E3=[0.0, 0.0, 0.0, -13.0, -13.0]
A= [[1.0,-1.0,2.0,-1.0,-8.0],[2.0,-2.0,3.0,-3.0,-20.0],[1.0,1.0,1.0,0.0,-2.0],[1.0,-1.0,4.0,3.0,4.0]]

NE=len(A)

for k in xrange(NE):

##### compruebo si el elemento de la diagonal es cero

###  si lo es, lo intercambio con otra fila

    if A[k][k] ==0.0:

        for l in xrange(k+1,NE):

            if A[l][k] !=0:

                AUX=A[k]

                A[k]=A[l]

                A[l]=AUX

                print k, 'cambia por ', l

                break

            elif l == NE-1:

                print 'No hay solucion unica'

                exit(0)

################## Gauss-Jordan

    for i in xrange(NE):

        if i!=k:

            mik=A[i][k]/A[k][k]

            for j in xrange(NE+1):

                A[i][j]=A[i][j]-mik*A[k][j]

        for i in xrange(NE): print A[i]

        print

#########################################

if A[NE-1][NE-1]==0.0:

    print 'No hay solucion unica'

    exit(0)

######################################

#pinto la matriz diagonal

print

for i in xrange(NE): print A[i]

print

for i in xrange(NE):

    xi=A[i][NE]/A[i][i]

    print 'x%d = %.2f' % (i+1,xi)




