# %% Dane
from math import pi

R = 20
C = 900 * 10 ** (-9)
print(f"{R = } Ohm")
print(f"{C = } F")

# %% Obliczenia
fg = 1 / (2 * pi * R * C)
print(f"{fg = } Hz")

# %% Wyznaczenie częstotliwości z analizy aplitudowej
print(f"fg = {10**3.94} Hz")
