# %% Dane
E = 220
R1 = R3 = 5
R4 = R5 = 10
R2 = 20

# Analiza
# %%Rezystancja Thevenina
R14 = R1 * R4 / (R1 + R4)
print(f"{R14 = } Ohm")

R23 = R2 * R3 / (R2 + R3)
print(f"{R23 = } Ohm")

RT = R14 + R23
print(f"{RT = } Ohm")
# %% Napięcie Thevenina
U4 = E * R4 / (R1 + R4)
print(f"{U4 = } V")

U3 = E * R3 / (R2 + R3)
print(f"{U3 = } V")

UT = U4 - U3
print(f"{UT = } V")

# %% Szukany prąd
I5 = UT / (RT + R5)
print(f"{I5 = } A")
