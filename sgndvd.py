
#!/home/heidi/Computadores/Metodos Numericos/Tarea5

import math
import pylab as p

m=1.0 #kg
t=[0.0,1.0,2.0,3.0,4.0] #segundos
y=[100.0,95.1,80.4,55.9,21.6] # metros
F=[] #Newtons

n=int(len(t))
h=(t[n-1]-t[0])/(n-1)

for i in range(1,n-1):
	a=1.0*(y[i-1]-2.0*y[i]+y[i+1])/h**2
	f=m*a
	F.append(f)

print F
