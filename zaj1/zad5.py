# %% Dane
U5 = 125
R1 = R4 = 2
R2 = R3 = R6 = 4
R5 = 12

# %% Obliczenia
I5 = U5 / R5
print(f"{I5 = } A")

U6 = U5
I6 = U6 / R6
print(f"{I6 = } A")

I = I5 + I6
print(f"{I  = } A")

R13 = R1 + R3
print(f"{R13 = } Ohm")

R123 = R2 * R13 / (R2 + R13)
print(f"{R123 = } Ohm")

U2 = I * R123
print(f"{U2 = } V")

U4 = R4 * I
print(f"{U4 = } V")

E = U2 + U4 + U5
print(f"{E = } V")
