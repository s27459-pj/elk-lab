# %% Biblioteki
import matplotlib.pyplot as plt
import numpy as np

# %% Dane
# Częstotliwość sygnału
f = 1_000
# Częstotliwość próbkowania
fs = 480_000
print(f"{f = }, {fs = }")

n = np.arange(2048)
print(f"{n = }")

# %% Przebieg sygnału w funkcji próbek
sinus = (
    0.5 * np.sin(2 * np.pi * f * n / fs)
    + 0.3 * np.sin(2 * np.pi * 3 * f * n / fs)
    + 0.2 * np.sin(2 * np.pi * 5 * f * n / fs)
)

plt.plot(n, sinus)
plt.title("Przebieg sygnału w funkcji próbek")
plt.xlabel("n [-]")
# plt.ylabel("1 * np.sin(2 * np.pi * f * n / fs) [-]")
plt.grid(True)
plt.show()

# %% Przebieg sygnału w funkcji czasu
t = n / fs
print(f"{t = }")

plt.plot(t, sinus)
plt.title("Przebieg sygnału w funkcji czasu")
plt.xlabel("t [s]")
# plt.ylabel("1 * np.sin(2 * np.pi * f * n / fs) [-]")
plt.xlim(0, 0.003)
plt.grid(True)
plt.show()

# %% Widmo (real fft)
widmo = np.fft.rfft(sinus)
print(f"{widmo = }")
widmo_amp = np.abs(widmo)
print(f"{widmo_amp = }")
widmo_amp_norm = widmo_amp / 1024
print(f"{widmo_amp_norm = }")
f = np.fft.rfftfreq(len(sinus), 1 / fs)
print(f"{f = }")

plt.plot(f, widmo_amp)
plt.title("Widmo amplitudowe")
plt.xlabel("f [Hz]")
plt.ylabel("|sinus| [-]")
plt.xlim(0, 20_000)
plt.grid(True)
plt.show()

plt.plot(f, widmo_amp_norm)
plt.title("Widmo amplitudowe po normalizacji")
plt.xlabel("f [Hz]")
plt.ylabel("|sinus| [-]")
plt.xlim(0, 20_000)
plt.grid(True)
plt.show()

# %% Widmo w skali logarytmicznej
plt.plot(f, 20 * np.log10(widmo_amp_norm))
plt.title("Widmo amplitudowe po normalizacji w skali logarytmicznej")
plt.xlabel("f [Hz]")
plt.ylabel("|sinus| [dB]")
plt.xlim(0, 20_000)
plt.grid(True)
plt.show()

# %% Widmo fazowe
widmo_fazowe = np.angle(widmo)
print(f"{widmo_fazowe = }")
plt.plot(f, widmo_fazowe)
plt.title("Widmo fazowe")
plt.xlabel("f [Hz]")
plt.ylabel("angle(sinus) [rad]")
plt.xlim(0, 20_000)
plt.grid(True)
plt.show()


# %% Maksima widma
def maksima_widma(widmo, prog, rozmiar_okna, fs):
    ponad = (widmo >= prog).astype(int)
    pochodna = np.diff(ponad)
    poczatki = np.where(pochodna == 1)[0] + 1
    konce = np.where(pochodna == -1)[0] + 1
    maksima = []
    for poczatek, koniec in zip(poczatki, konce):
        p = np.argmax(widmo[poczatek:koniec]) + poczatek
        a, b, c = widmo[p - 1 : p + 2]
        k = 0.5 * (a - c) / (a - 2 * b + c)
        maksima.append((p + k) * fs / rozmiar_okna)
    return maksima


wwwwwww = 20 * np.log10(np.abs(widmo_amp_norm) / 1024)
print(wwwwwww)

maksima = maksima_widma(wwwwwww, -80, 2048, fs)

for m in maksima:
    print("f = {:8.3f}, współczynnik = {:5.2f}".format(m, m / maksima[0]))
