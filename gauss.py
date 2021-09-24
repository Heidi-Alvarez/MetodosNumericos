import math
import pylab as p
from sys import exit

def Gauss(A):

	NE=len(A)

	for k in xrange(NE):
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
    		for i in xrange(NE):
        		if i!=k:
            			mik=A[i][k]/A[k][k]
            			for j in xrange(NE+1):
                			A[i][j]=A[i][j]-mik*A[k][j]
#        		for i in xrange(NE): print A[i]
 #       		print

	if A[NE-1][NE-1]==0.0:
    		print 'No hay solucion unica'
    		exit(0)

#	print

#	for i in xrange(NE): print A[i]
#	print
	x=[]
	for i in xrange(NE):
    		xi=A[i][NE]/A[i][i]
		x.append(xi)
 #		print 'x%d = %.2f' % (i+1,xi)
	return x
