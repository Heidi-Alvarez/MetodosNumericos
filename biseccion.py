#!/home/heidi/Computadores/Metodos Numericos/Segunda

import math
import numpy as np

def fun(x):
	m=1.0
	h=100.0
        g=9.8
        k=0.1
        f=h-(m*g*x)/k +m*m*g*(1-math.exp(-k*x/m))/(k*k)
        return f

a=0.0
b=6.0
niter=0
Nmax=100
error=1e-7
while(niter<=Nmax):
	P=(a+b)/2.0
	funa=fun(a)
	funb=fun(b)
	funP=fun(P)
	if(funa*funP>0):
	    a=P
	elif(funa*funP<0):
	    b=P
	if(funP==0 or np.abs(funP-0)<=error):
	    print 'El tiempo en segundos que se demora en caer el objeto es %f'%P
	    break
	niter+=1


