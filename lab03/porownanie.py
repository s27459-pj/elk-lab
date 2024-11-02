# %% Biblioteki
import matplotlib.pyplot as plt
import numpy as np

# %% Dane
# Częstotliwość sygnału
f = 1_000
# Częstotliwość próbkowania
fs = 480_000
print(f"{f = }, {fs = }")

n = np.arange(4096)
print(f"{n = }")

# %%
y = np.sin(2 * np.pi * f * n / fs)

for N in (64, 128, 256, 512, 1024, 2048, 4096):
    widmo = np.abs(np.fft.rfft(y[:N]))
    index_prazka = np.argmax(widmo)
    czestotliwosc_prazka = index_prazka * (fs / N)
    blad = 100 * np.abs(czestotliwosc_prazka - f) / f
    print(
        "N = {:4}, czestotliwosc = {:>8.3f}Hz, blad = {:5.2f}%".format(
            N, czestotliwosc_prazka, blad
        )
    )


# %%
def show(N: int):
    w = np.abs(np.fft.rfft(y[:N]))
    ft = np.fft.fftfreq(N, 1 / fs)
    plt.plot(ft[: N // 2 + 1], w)
    plt.title(f"Widmo amplitudowe ({N})")
    plt.xlabel("f [Hz]")
    plt.ylabel("|sinus| [-]")
    plt.xlim(0, 20_000)
    plt.grid(True)
    plt.show()


for i in (64, 128, 256, 512, 1024, 2048, 4096):
    show(i)
