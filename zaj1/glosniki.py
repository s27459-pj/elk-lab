# %% Dane
E = 24
R1 = 6
R2 = 8

# %% Połączenie równogległe
R12 = R1 * R2 / (R1 + R2)
print(f"{R12 = } Ohm")

I = E / R12
print(f"{I = } A")

Pcr = E * I
print(f"{Pcr = } W")

P1 = E**2 / R1
print(f"{P1 = } W")

P2 = E**2 / R2
print(f"{P2 = } W")

Por = P1 + P2
print(f"{Por = } W")

# %% Połączenie szeregowe
I = E / (R1 + R2)
print(f"{I = } A")

Pcs = E * I
print(f"{Pcs = } W")

P1 = I**2 * R1
print(f"{P1 = } W")

P2 = I**2 * R2
print(f"{P2 = } W")

Por = P1 + P2
print(f"{Por = } W")
