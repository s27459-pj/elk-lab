# %% Dane
from math import pi

R = 20
fd = 80_000

# %%
C = 1 / (2 * pi * fd * R)
print(f"{C = } F")

# %%
C = 900 * 10 ** (-9)
R = 1 / (2 * pi * fd * C)
print(f"{R = } Ohm")
f = 1 / (2 * pi * R * C)
print(f"{f = } Hz")
