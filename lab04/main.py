from pathlib import Path

FIGURES = Path(__file__).resolve().parent / "figures4"
FIGURES.mkdir(exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt
import math
import time
from scipy.io import wavfile

#Exercitiul 1

def DFT(x):
    N = len(x)
    omega = range(N)
    X = np.zeros(len(omega), dtype=complex)
    i = 0
    for w in omega:
        for n in range(N):
            X[i] += x[n] * math.e**(-2*math.pi*1j*n*w/N)
        i += 1
    return X


def FFT(x):
    N = len(x)
    if N == 1:
        return np.array(x, dtype=complex)
    if N == 0 or N % 2 != 0:
        raise ValueError("Lungimea vectorului trebuie să fie o putere a lui 2.")

    Xpar = FFT(x[::2])
    Ximpar = FFT(x[1::2])
    X = np.empty(N, dtype=complex)
    for w in range(N // 2):
        z = math.e**(-2*math.pi*1j*w/N)*Ximpar[w]
        X[w] = Xpar[w] + z
        X[w + N // 2] = Xpar[w] - z
    return X
dimensiuni = [128, 256, 512, 1024, 2048, 4096, 8192]
timpi_DFT = []
timpi_FFT = []
timpi_numpy = []
"""
for N in dimensiuni:
    x = np.random.randn(N)

    start = time.perf_counter()
    DFT(x)
    timpi_DFT.append(time.perf_counter() - start)

    start = time.perf_counter()
    FFT(x)
    timpi_FFT.append(time.perf_counter() - start)

    start = time.perf_counter()
    np.fft.fft(x)
    timpi_numpy.append(time.perf_counter() - start)
plt.figure()
plt.semilogy(dimensiuni, timpi_DFT, "o-", label="DFT")
plt.semilogy(dimensiuni, timpi_FFT, "o-", label="FFT")
plt.semilogy(dimensiuni, timpi_numpy, "o-", label="NumPy FFT")
plt.xlabel("Dimensiunea vectorului N")
plt.ylabel("Timp de execuție (s)")
plt.legend()
plt.savefig(FIGURES/"ex1fig1.pdf")
plt.show()
"""
#Exercitiul 2
fs = 5
f1 = 7
f2 = f1 - fs
f3 = f1 + fs
#f=f1+k*fs

t = np.linspace(0, 1, 1000)
ts = np.arange(fs + 1) / fs
xs = np.sin(2 * np.pi * f1 * ts)

plt.figure()
for f in [f1, f2, f3]:
    plt.plot(t, np.sin(2 * np.pi * f * t), label=f"{f} Hz")

plt.scatter(ts, xs, label="Eșantioane comune")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.legend()
plt.savefig(FIGURES / "ex2fig1.pdf")
plt.show()

#Exercitiul 3

fs = 15
f1 = 7
f2 = 2
f3 = 12
#f=f1+k*fs

t = np.linspace(0, 1, 1000)
ts = np.arange(fs+1) / fs
xs = np.sin(2 * np.pi * f1 * ts)

plt.figure()
for f in [f1, f2, f3]:
    plt.plot(t, np.sin(2 * np.pi * f * t), label=f"{f} Hz")

plt.scatter(ts, xs, label="Eșantioane la 15hz")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.legend()
plt.savefig(FIGURES / "ex2fig1.pdf")
plt.show()

#Exercitiul 4
#[40,200], [-200,-40] incluse in [-200,200]=[-B,B], trebuie sa esantionez la 2B=400hz.

#Exericitul 6
folder = Path(__file__).resolve().parent
FIGURES = folder / "figures4"
#a
fs, x = wavfile.read(Path(__file__).resolve().parent / "vocale.wav")
#b
N = len(x)
M = N // 100
M -= M % 2  # M par
pas = M // 2
#c
S = []
for start in range(0, N - M + 1, pas):
    grup = x[start:start + M]
    S.append(np.abs(np.fft.rfft(grup)))
#d
S = np.array(S).T
#e
plt.figure()
plt.imshow(S, origin="lower", aspect="auto")
plt.xlabel("Fereastră de timp")
plt.ylabel("Bin FFT")
plt.colorbar(label="Magnitudine")
plt.savefig(FIGURES / "ex6fig1.pdf")
plt.show()

#Exercitiul 7
P_semnal_dB = 90
SNR_dB = 80

P_semnal_rel = 10**(P_semnal_dB / 10)  # P_semnal / P0
SNR = 10**(SNR_dB / 10)
P_zgomot_rel = P_semnal_rel / SNR
P_zgomot_dB = 10 * math.log10(P_zgomot_rel)

print(f"P_zgomot = {P_zgomot_rel:g} * P0")
print(f"P_zgomot_dB = {P_zgomot_dB:g} dB")

