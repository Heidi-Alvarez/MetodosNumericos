#!/home/heidi/Computadores/Metodos Numericos/Segunda

import math
import pylab as p

def fun(x):
    m=1.0
    h=100.0
    g=9.8
    k=0.1
    f=h-(m*g*x)/k +m*m*g*(1-math.exp(-k*x/m))/(k*k)
    return f

delta=1e-5
i=0
t=0
tt=[]
HH=[]
H=0
corte=[]
while(H>-20):
        i+=1
        t+=delta*i
        H=fun(t)
        tt.append(t)
        HH.append(H)
	corte.append(0)

p.plot(tt,HH, '.')
p.plot(tt,corte)

p.show()

