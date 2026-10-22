from pathlib import Path

from scipy.io import wavfile

FIGURES = Path(__file__).resolve().parent / "figures2"
FIGURES.mkdir(exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal
import sounddevice as sd
#fs=44100
#Exercitiul 1

fs=2000
A=2
f=50
phi=np.pi/2
t=np.arange(0,0.3,1/fs)
sin= lambda t: A*np.sin(2*np.pi*f*t+phi)
cos= lambda t: A*np.cos(2*np.pi*f*t+phi-np.pi/2)
fig, axs=plt.subplots(2)
axs[0].plot(t,sin(t))
axs[1].plot(t,cos(t))
plt.savefig(FIGURES/"ex1fig1.pdf")
plt.show()


#Exercitiul 2

fs=2000
f=50
phi1=np.pi/2
phi2=np.pi/4
phi3=np.pi/8
phi4=np.pi/16
sin1=lambda t:np.sin(2*np.pi*f*t+phi1)
sin2=lambda t:np.sin(2*np.pi*f*t+phi2)
sin3=lambda t:np.sin(2*np.pi*f*t+phi3)
sin4=lambda t:np.sin(2*np.pi*f*t+phi4)
t=np.arange(0,0.3,1/fs)
plt.figure()
plt.plot(t, sin1(t), label="phi = pi/2")
plt.plot(t, sin2(t), label="phi = pi/4")
plt.plot(t, sin3(t), label="phi = pi/8")
plt.plot(t, sin4(t), label="phi = pi/16")
plt.legend()
plt.savefig(FIGURES / "ex2fig1.pdf")
plt.show()

x=sin1(t)
z = np.random.normal(0,1,len(x))
SNR=[0.1,1,10,100]
fig1,axs1=plt.subplots(4)
for ax,snr in zip(axs1,SNR):
    gamma=np.linalg.norm(x)/(np.sqrt(snr)*np.linalg.norm(z))
    x_zgomot=x+gamma*z
    ax.plot(t,x_zgomot, label="Semnal cu zgomot")
    ax.plot(t, x, label="Semnal original")
    ax.set_title(f"SNR = {snr}")
    ax.legend()
plt.savefig(FIGURES / "ex2fig2.pdf")
plt.show()

#Exercitiul 3
#semnalele din lab01
#a
f=400
fs=1600
t2=np.arange(0,3,1/fs)
sin=lambda t: np.sin(2*f*np.pi*t)
x_a=sin(t2)
#b
fs=8000
f=800
t3=np.arange(0,3,1/fs)
sin2=lambda t: np.sin(2*f*np.pi*t)
x_b=sin2(t3)
#c
f=240
fs=10000
t4=np.arange(0,3,1/fs)
st = lambda t: 2 * (f*t - np.floor(f*t + 1/2))
x_c=st(t4)
#d
f=300
fs=10000
t5=np.arange(0,3,1/fs)
sq=lambda t: np.sign(np.sin(2*f*np.pi*t))
x_d=sq(t5)

for nume, x, fs_redare in [
    ("Sinus 400 Hz", x_a, 1600),
    ("Sinus 800 Hz", x_b, 8000),
    ("Sawtooth 240 Hz", x_c, 10000),
    ("Square 300 Hz", x_d, 10000),
]:
    print(f"Redare: {nume}")
    sd.play(0.2*x, fs_redare)
    sd.wait()
cale_wav = Path(__file__).resolve().parent / "sinus_800Hz.wav"
x_salvat = (0.2 * x_b).astype(np.float32)
wavfile.write(cale_wav, 8000, x_salvat)

fs_citit, x_citit = wavfile.read(cale_wav)

#Exercitiul 4

fs=3000
t=np.arange(0,0.3,1/fs)

sin=np.sin(2*np.pi*50*t)
st=2 * (100*t - np.floor(100*t + 1/2))
suma=sin+st
fig2,axs2=plt.subplots(3)
axs2[0].plot(t,sin)
axs2[1].plot(t,st)
axs2[2].plot(t,suma)
plt.savefig(FIGURES/"ex4fig1.pdf")
plt.show()

#Exercitiul 5

fs=44100
t=np.arange(0,3,1/fs)
f1=500
f2=1000
sin1=np.sin(2*np.pi*f1*t)
sin2=np.sin(2*np.pi*f2*t)
x=np.concatenate((sin1,sin2))
print("Redare:")
sd.play(0.2*x,fs)
sd.wait()

#Exercitiul 6

fs=1000
n = np.arange(20)
frecvente = [fs / 2, fs / 4, 0]
titluri = ["f = fs/2", "f = fs/4", "f = 0 Hz"]
fig, axs = plt.subplots(3)
for ax, f, titlu in zip(axs, frecvente, titluri):
    x = np.sin(2 * np.pi * f * n / fs)
    ax.stem(n, x)
    ax.set_title(titlu)

fig.savefig(FIGURES / "ex6fig1.pdf")
plt.show()

#Exercitiul 7

fs=1000
f = 400

t = np.arange(100) / fs
x = np.sin(2 * np.pi * f * t)
#a
t_a = t[::4]
x_a = x[::4]
#b
t_b = t[1::4]
x_b = x[1::4]

fig, axs = plt.subplots(3)

axs[0].stem(t, x)
axs[0].set_title("Original: fs = 1000 Hz")

axs[1].plot(t, x)
axs[1].stem(t_a, x_a)
axs[1].set_title("Decimare x[::4]: fs = 250 Hz")

axs[2].plot(t, x)
axs[2].stem(t_b, x_b)
axs[2].set_title("Decimare x[1::4]: fs = 250 Hz")

fig.savefig(FIGURES / "ex7fig1.pdf")
plt.show()

#Exercitiul 8
alfa = np.linspace(-np.pi / 2, np.pi / 2, 1000)
sin = np.sin(alfa)
taylor = alfa
pade = (alfa - 7 * alfa ** 3 / 60) / (1 + alfa ** 2 / 20)

eroare_taylor = np.abs(sin - taylor)
eroare_pade = np.abs(sin - pade)

fig, axs = plt.subplots(3)

axs[0].plot(alfa, sin, label="sin(alfa)")
axs[0].plot(alfa, taylor, label="Taylor: alfa")
axs[0].plot(alfa, pade, ":", label="Pade")
axs[0].set_title("Aproximari")

axs[1].plot(alfa, eroare_taylor, label="Eroare Taylor")
axs[1].plot(alfa, eroare_pade, label="Eroare Pade")
axs[1].set_title("Erori absolute")

axs[2].plot(alfa, eroare_taylor, label="Eroare Taylor")
axs[2].plot(alfa, eroare_pade, label="Eroare Pade")
axs[2].set_yscale("log")
axs[2].set_title("Erori absolute — Oy scara logaritmica")

for ax in axs:
    ax.legend()

plt.savefig(FIGURES/"ex8fig1.pdf")
plt.show()
