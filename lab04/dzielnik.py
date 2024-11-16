# %% Dane
E = 24
Rg = Rd = 80

# %% Napięcie z dzielnikiem bez lodówki
Ud = E * Rd / (Rg + Rd)
print(f"{Ud = } V")

# %% Napięcie z dzielnikiem i lodówką
RL = 100
RdL = Rd * RL / (Rd + RL)
print(f"{RdL = } Ohm")
UdL = E * RdL / (Rg + RdL)
print(f"{UdL = } V")
# %% Dzielnik z kompensacją rezystancji lodówki (wydajniejszy sposób)
Rg = 80
Rd = 400
RL = 100
RdL = Rd * RL / (Rd + RL)
print(f"{RdL = } Ohm")
UdL = E * RdL / (Rg + RdL)
print(f"{UdL = } V")
Prl = UdL**2 / RL
print(f"{Prl = } W")
Prd = UdL**2 / Rd
print(f"{Prd = } W")

# %% Dzielnik z kompensacją rezystancji lodówki na inny sposób (mniej wydajny)
Rg = 44.44
Rd = 80
RL = 100
RdL = Rd * RL / (Rd + RL)
print(f"{RdL = } Ohm")
UdL = E * RdL / (Rg + RdL)
print(f"{UdL = } V")
Prl = UdL**2 / RL
print(f"{Prl = } W")
Prd = UdL**2 / Rd
print(f"{Prd = } W")
