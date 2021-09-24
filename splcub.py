#!/home/heidi/Computadores/Metodos Numericos/Tercera

import math
import pylab as p

def GaussJordan(A):
        N=len(A)
        for i in range(N-1):
                for l in range(i+1,N):
                        m=A[l][i]/A[i][i]
                        for j in range(i,N):
                                A[l][j]=A[l][j]-m*A[i][j]

        for i in range(N-1):
                X=A[i][N-1]/A[i][i]
                x.append(X)
        return x

def fun(x):
    f=math.sin(x)*math.cos(x)
    return f

np=50; xmin=0.0; xmax=4.0*math.pi
deltax=(xmax-xmin)/(np-1.0)
xx=[]
funcion=[]
for i in range(np):
    x=xmin+deltax*float(i)
    f=fun(x)
    xx.append(x)
    funcion.append(f)

p.plot(xx,funcion, '.')

x=[]
h=[]
A=[[0.0]*(np) for i in range(np)]
A[0][0]=1.0
A[np-1][np-1]=1.0

for i in range(np-1):
    h.append(xx[i+1]-xx[i])

for i in range(1,np-1):
        A[i][i-1]=h[i-1]
        A[i][i]=2*(h[i]+h[i-1])
        A[i][i+1]=h[i]
        A[i][np-1]=3.0*(fun(xx[i+1])-fun(xx[i]))/h[i]-3.0*(fun(xx[i])-fun(xx[i-1]))/h[i-1]

c=GaussJordan(A)

b=[0.0]*(np)
for j in range(np-2):
        b[j]=(fun(xx[j+1])-fun(xx[j]))/h[j] -h[j]*(2.0*c[j]+c[j+1])/3.0
	print j
d=[0.0]*(np)
for j in range(np-2):
        d[j]=(c[j+1]-c[j])/(3.0*h[j])

print b

ngrid=10
deltax2=deltax/float(ngrid)
xxx=[]
splines=[]
xh=0.0
for i in range(np-1):
    for j in range(ngrid):
        x=xmin+xh+float(j)*deltax2
        xxx.append(x)
        S=fun(xx[i])+b[i]*(x-xx[i])+c[i]*(x-xx[i])**2.0+d[i]*(x-xx[i])**3.0
        splines.append(S)
    xh+=h[i]

p.plot(xxx,splines, 'b')

p.show()



