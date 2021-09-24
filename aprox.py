#!/home/heidi/Computadores/Metodos Numericos/Tarea5

import math
import pylab as p
from gauss import Gauss


x=[4.0,4.2,4.5,4.7,5.1,5.5,5.9,6.3,6.8,7.1]
y=[102.56,113.18,130.11,142.05,167.53,195.14,224.87,256.73,299.50,326.72]


orden1=[]
orden2=[]
orden3=[]

########Lineal############
n=int(len(x))
sumxy=0.0; sumx=0.0; sumy=0.0; sumxx=0.0

for i in range(n):
	sumxy+=x[i]*y[i]
	sumx+=x[i]
	sumy+=y[i]
	sumxx+=(x[i])**2

m=(n*sumxy -sumx*sumy)/(n*sumxx -sumx**2)
b=(sumy*sumxx -sumx*sumxy)/(n*sumxx -sumx**2)

error1=0.0

for i in range(n):
	Y=m*x[i]+b
	error1+=(y[i]-Y)**2
	orden1.append(Y)


#######Lineal#################################

#############Segundo Orden####################
n=3;
A=[[0.0]*(n+1) for i in range(n)]
m=int(len(x))
for j in range(n):
	b=0.0
	for k in range(n):
		a=0.0
		for i in range(m):
			a+=x[i]**(j+k)
			A[k][j]=a
	for i in range(m):
		b+=y[i]*x[i]**j
	A[j][n]=b

C=Gauss(A)
error2=0.0

for i in range(m):
	Y=C[0]+C[1]*x[i]+C[2]*x[i]**2
	error2+=(y[i]-Y)**2
        orden2.append(Y)

##############Segundo Orden#################

##############Tercer Orden##################
n=4;
A=[[0.0]*(n+1) for i in range(n)]
m=int(len(x))
for j in range(n):
        b=0.0
        for k in range(n):
                a=0.0
                for i in range(m):
                        a+=x[i]**(j+k)
                        A[k][j]=a
        for i in range(m):
                b+=y[i]*x[i]**j
        A[j][n]=b

C=Gauss(A)
error3=0.0
for i in range(m):
        Y=C[0]+C[1]*x[i]+C[2]*x[i]**2+C[3]*x[i]**3
	error3+=(y[i]-Y)**2
        orden3.append(Y)
	
################Tercer Orden####################

################Errores#########################
print error1, error2, error3

################Errores#########################

################Grafica########################

p.plot(x,y,'b.', ms=10)
p.plot(x,orden1)
p.plot(x,orden2)
p.plot(x,orden3)

p.show()

















