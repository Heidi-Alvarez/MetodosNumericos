#!/home/heidi/Computadores/Metodos Numericos/Tarea5

import math

def Y(t):
	y=g*t
	return y 

t=[0,1,2,3,4]
g=-9.8
h=100.0
r=[0.9061798459,0.5384693101,0.0,-0.05384693101,-0.9061798459]
c=[0.2369268850,0.4786286705,0.5688888889,0.4786286705,0.2369268850]

n=int(len(t))

for i in range(n):
        tmin=t[0]
        tmax=t[i]
        inter=(tmax-tmin)/2.0
        suma=0.0
        for j in range(n):
		tt=(inter*2*r[j] +t[i]+t[0])/2.0
                suma+=c[j]*Y(tt)
        integral=inter*suma+h
        print 'h=%.3f m en t=%.1d s'%(integral,i)
