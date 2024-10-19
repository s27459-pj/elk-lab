# %% Dane
E1 = 10
E2 = 20
Iz = 5
R1 = R2 = 2
R3 = 1

# %% Układ 1
R23 = R2 * R3 / (R2 + R3)
print(f"{R23 = } Ohm")

I11 = E1 / (R1 + R23)
print(f"{I11 = } A")

U31 = R23 * I11
print(f"{U31 = } V")

I31 = U31 / R2
print(f"{I31 = } A")

# %% Układ 2
R12 = R1 * R2 / (R1 + R2)
print(f"{R12 = } Ohm")

I22 = E2 / (R12 + R3)
print(f"{I22 = } A")

U32 = R3 * I22
print(f"{U32 = } V")

U12 = E2 - U32
print(f"{U12 = } V")

I32 = -U12 / R2
print(f"{I32 = } A")

# %% Układ 3
R123 = R12 * R3 / (R12 + R3)
print(f"{R123 = } Ohm")

U33 = R123 * Iz
print(f"{U33 = } V")

I33 = U33 / R2
print(f"{I33 = } A")

# %% Podsumowanie
U3 = U31 + U32 + U33
print(f"{U3 = } V")

I3 = I31 + I32 + I33
print(f"{I3 = } A")
