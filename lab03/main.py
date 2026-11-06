from pathlib import Path

FIGURES = Path(__file__).resolve().parent / "figures3"
FIGURES.mkdir(exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt
import math

#Exercitiul 1

F=np.zeros((8,8), dtype=complex)
for i in range(8):
    for k in range(8):
        F[i,k]=(1/math.sqrt(8))*math.e**(-2*math.pi*1j*k*i/8)
print(F)
I=np.identity(8,dtype=complex)
FhF=F.conjugate().T@F
print(np.linalg.norm(FhF-I)<=10**-14)
print(np.allclose(FhF,I))

#Exercitiul 2

fs=1000
A=1
f=15
phi=0
t=np.arange(0,1,1/fs)
x=A*np.sin(2*np.pi*t*f+phi)
plt.figure()
plt.ylabel("Amplitudine")
plt.xlabel("Timp (esantioane)")
plt.plot(np.arange(len(x)),x)
plt.savefig(FIGURES/"ex2fig1.pdf")
plt.show()
y=np.zeros_like(x,dtype=complex)
for n in range(len(x)):
    y[n]=x[n]*math.e**(-2*math.pi*1j*n/len(x))
plt.figure()
plt.ylabel("Imaginar")
plt.xlabel("Real")
plt.axis("equal")
plt.plot(y.real,y.imag)
plt.savefig(FIGURES/"ex2fig2.pdf")
plt.show()

omega=[5,10,15,20]
z=np.zeros_like(x,dtype=complex)
fig,axs=plt.subplots(2,2)
for ax,w in zip(axs.flat,omega):
    for n in range(len(x)):
        z[n]=x[n]*math.e**(-2*math.pi*1j*w*n/len(x))
    ax.plot(z.real,z.imag)
    plt.ylabel("Imaginar")
    plt.xlabel("Real")
    plt.axis("equal")
plt.savefig(FIGURES/"ex2fig3.pdf")
plt.show()

#Exercitiul 3
omega=[i for i in range(1,101)]
fs=1000
f1=10
f2=15
f3=60
t=np.arange(0,1,1/fs)
x=np.cos(2*math.pi*t*f1)+2*np.cos(2*math.pi*t*f2)+3*np.sin(2*math.pi*f3*t)
X=np.zeros(len(omega),dtype=complex)
i=0
N=len(x)
for w in omega:
    for n in range(N):
        X[i]+=x[n]*math.e**(-2*math.pi*1j*n*w/N)
    i+=1
fig,axs=plt.subplots(2)
axs[0].plot(t,x)
axs[1].plot(omega,np.abs(X))
plt.savefig(FIGURES/"ex3fig1.pdf")
plt.show()