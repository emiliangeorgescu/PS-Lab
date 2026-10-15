from pathlib import Path

FIGURES = Path(__file__).resolve().parent / "figures"
FIGURES.mkdir(exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt


#Exercitiul1
#a
t=np.linspace(0,0.03,61)

#b
x=lambda t: np.cos(520*np.pi*t+np.pi/3)
y=lambda t: np.cos(280*np.pi*t-np.pi/3)
z=lambda t: np.cos(120*np.pi*t+np.pi/3)

fig, axs=plt.subplots(3)
fig.suptitle("Exercitiul 1, b")
axs[0].plot(t,x(t))
axs[1].plot(t,y(t))
axs[2].plot(t,z(t))
plt.savefig(FIGURES/"ex1fig1.pdf")
plt.show()

#c

t1=np.linspace(0,0.03,7)

fig1, axs1=plt.subplots(3)
fig1.suptitle("Exercitiul1, c")
axs1[0].stem(t1,x(t1))
axs1[1].stem(t1,y(t1))
axs1[2].stem(t1,z(t1))
plt.savefig(FIGURES/ "ex1fig2.pdf")
plt.show()

#Exercitiul 2
#a

f=400
fs=1600
t2=np.arange(0,1,1/fs)
sin=lambda t: np.sin(2*f*np.pi*t)
plt.figure()
plt.plot(t2,sin(t2))
plt.suptitle("Exercitiul 2, a")
plt.savefig(FIGURES/"ex2fig1.pdf")
plt.show()

#b

fs=8000
f=800
t3=np.arange(0,3,1/fs)
sin2=lambda t: np.sin(2*f*np.pi*t)
plt.figure()
plt.plot(t3,sin2(t3))
plt.suptitle("Exercitiul 2, b")
plt.savefig(FIGURES/"ex2fig2.pdf")
plt.show()

#c

f=240
fs=10000
t4=np.arange(0,0.03,1/fs)
st = lambda t: 2 * (f*t - np.floor(f*t + 1/2))
plt.figure()
plt.plot(t4,st(t4))
plt.suptitle("Exercitiul 2, c")
plt.savefig(FIGURES/"ex2fig3.pdf")
plt.show()

#d

f=300
fs=10000
t5=np.arange(0,1,1/fs)
sq=lambda t: np.sign(np.sin(2*f*np.pi*t))
plt.figure()
plt.plot(t5,sq(t5))
plt.suptitle("Exercitiul 2, d")
plt.savefig(FIGURES/"ex2fig4.pdf")
plt.show()

#e

A=np.array(np.random.rand(128,128))
plt.figure()
plt.imshow(A)
plt.suptitle("Exercitiul 2, e")
plt.savefig(FIGURES/"ex2fig5.pdf")
plt.show()

#f

B=np.zeros((128,128))
B[64:128,64:128]=np.ones((64,64))
plt.figure()
plt.imshow(B)
plt.suptitle("Exercitiul 2, f")
plt.savefig(FIGURES/'ex2fig6.pdf')
plt.show()

#Exercitiul 3
#a
f=2000
t=1/f

print(t)

#b
nr_sec=3600
nr_esantioane=f*nr_sec
nr_biti=nr_esantioane*4
nr_bytes=nr_biti/8

print(nr_bytes)
