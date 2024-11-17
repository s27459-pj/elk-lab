# %%
import matplotlib.pyplot as plt
import numpy as np


class Dioda:
    def __init__(
        self,
        Urm=0.0,
        Ur=0.0,
        Ufp=0.0,
        rd=0.0,
        If=0.0,
        Ifm=0.0,
    ):
        self.Urm = Urm
        self.Ur = Ur
        self.Ufp = Ufp
        self.rd = rd
        self.If = If
        self.Ifm = Ifm

    def diodaId(self, Url, Ur, If, Ifm):
        self.Urm = Url
        self.Ur = Ur
        self.If = If
        self.Ifm = Ifm

    def diodaUfp(self, Url, Ur, Ufp, If, Ifm):
        self.Urm = Url
        self.Ur = Ur
        self.Ufp = Ufp
        self.If = If
        self.Ifm = Ifm

    def diodaUfpRd(self, Url, Ur, Ufp, rd, If, Ifm):
        self.Urm = Url
        self.Ur = Ur
        self.Ufp = Ufp
        self.rd = rd
        self.If = If
        self.Ifm = Ifm

    def diodaUd(self):
        if self.rd == 0.0 and self.Ufp == 0.0:
            return 0.0
        elif self.rd == 0 and self.Ufp > 0.0:
            return self.Ufp
        else:
            return self.Ufp + self.rd * self.If

    def diodaUI(self):
        if self.rd == 0.0 and self.Ufp == 0.0:
            uff = np.array([0.0, self.Ufp])
            iff = np.array([0.0, self.If])
        elif self.rd == 0.0 and self.Ufp > 0.0:
            uff = np.arange(0.0, self.Ufp, self.Ufp / 300)
            iff = np.zeros(len(uff))
            for i in range(len(uff)):
                if uff[i] < self.Ufp:
                    iff[i] = 0.0
                    iff[-1] = self.If
        else:
            uff = np.arange(
                0.0,
                self.Ufp + self.rd * self.If,
                (self.Ufp + self.rd * self.If) / 200,
            )
            iff = np.zeros(len(uff))
            for i in range(len(uff)):
                if uff[i] < self.Ufp:
                    iff[i] = 0.0
                else:
                    iff[i] = uff[i] / self.rd - self.Ufp / self.rd

        plt.plot(uff, iff)
        plt.xlabel("Uf [V]")
        plt.ylabel("If [A]")
        plt.title("Charakterystyka UI diody")
        plt.grid(True)
        plt.show()


# %%
dId = Dioda()
dId.diodaId(100, 50, 1.5, 5)
print(f"{dId.Urm = } [V]")
print(f"{dId.Ur = } [V]")
print(f"{dId.Ufp = } [V]")
print(f"{dId.rd = } [Ohm]")
print(f"{dId.If = } [A]")
print(f"{dId.Ifm = } [A]")
print(f"{dId.diodaUd() = } [V]")
dId.diodaUI()

# %%
dUfp = Dioda()
dUfp.diodaUfp(100, 50, 0.7, 1.5, 5)
print(f"{dUfp.Urm = } [V]")
print(f"{dUfp.Ur = } [V]")
print(f"{dUfp.Ufp = } [V]")
print(f"{dUfp.rd = } [Ohm]")
print(f"{dUfp.If = } [A]")
print(f"{dUfp.Ifm = } [A]")
print(f"{dUfp.diodaUd() = } [V]")
dUfp.diodaUI()

# %%
dUfpRd = Dioda()
dUfpRd.diodaUfpRd(100, 50, 0.7, 2.5, 1.5, 5)
print(f"{dUfpRd.Urm = } [V]")
print(f"{dUfpRd.Ur = } [V]")
print(f"{dUfpRd.Ufp = } [V]")
print(f"{dUfpRd.rd = } [Ohm]")
print(f"{dUfpRd.If = } [A]")
print(f"{dUfpRd.Ifm = } [A]")
print(f"{dUfpRd.diodaUd() = } [V]")
dUfpRd.diodaUI()


# %%
from enum import Enum


class Kolor(Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2
    BLUE = 3
    NONE = 4


class DiodaLED(Dioda):
    def blink(self):
        if self.Ufp > 0.7 and self.Ufp < 1.2:
            return Kolor(0)
        elif self.Ufp > 1.2 and self.Ufp < 2.2:
            return Kolor(1)
        elif self.Ufp > 2.2 and self.Ufp < 3.2:
            return Kolor(2)
        elif self.Ufp > 3.2 and self.Ufp < 4.0:
            return Kolor(3)
        else:
            return Kolor(4)


# %%
dLED = DiodaLED(Urm=100, Ur=50, Ufp=3.7, If=1.5, Ifm=5)
print(f"{dLED.Urm = } [V]")
print(f"{dLED.Ur = } [V]")
print(f"{dLED.Ufp = } [V]")
print(f"{dLED.rd = } [Ohm]")
print(f"{dLED.If = } [A]")
print(f"{dLED.Ifm = } [A]")
print(f"Kolor = {dLED.blink()}")
print(f"{dLED.diodaUd() = } [V]")
dLED.diodaUI()
