# %%
import numpy as np
from scipy.special import lambertw


def lambert_w(
    isc: float,
    voc: float,
    imp: float,
    vmp: float,
    alpha: float,
    beta: float,
    n_ser: int,
    c=25,
    g=1000,
):
    # dane odniesienia
    t_ref = 273.15 + 25
    g_ref = 1000

    # stałe fizyczne
    k = 1.38064852e-23  # stała Boltzmann [J/(m^2*K)]
    q = 1.60217657e-19  # Ładunek elektronu w [C]
    eg_ref = 1.121  # napięcie przerwy pasmowej [eV]
    eg = eg_ref * q  # energia przerwy energetycznej
    vt_ref = k * t_ref / q  # reference thermal voltage

    # proąd gnerowany w wyniku fotoemisji jest aproksymowany prądem zwarciowym
    iph = isc

    # współczynnik idealności diody
    a = (beta - voc / t_ref) / (
        (n_ser * vt_ref) * ((alpha / iph) - (3 / t_ref) - (eg / (k * (t_ref**2))))
    )

    # prad ciemny
    io = iph * np.exp(-voc / (a * n_ser * vt_ref))

    # 𝑥 parametry obliczay z funkcji Lambert-W
    x = (
        lambertw(
            (vmp / (a * io * n_ser * vt_ref))
            * (2 * imp - iph - io)
            * np.exp(
                vmp
                * (vmp - 2 * a * n_ser * vt_ref)
                / (np.power(a, 2) * np.power(n_ser, 2) * np.power(vt_ref, 2))
            )
        )
        + (2 * vmp) / (n_ser * a * vt_ref)
        - np.power(vmp, 2) / (np.power(a, 2) * np.power(n_ser, 2) * np.power(vt_ref, 2))
    )

    # rezystancje szeregowe i bocznikowe
    rs = np.real((x * a * n_ser * vt_ref - vmp) / imp)
    rsh = np.real((x * a * n_ser * vt_ref) / (iph - imp - io * (np.exp(x) - 1)))

    # account for G and T
    # uses equations from Sera 2007
    t = 273.15 + c
    g_ratio = g / g_ref

    vt = a * vt_ref
    alpha = alpha / isc * 100  # Convert alpha to %/C
    isc_t = isc * (1 + (alpha / 100) * (t - t_ref))
    voc_t = voc + beta * (t - t_ref)

    io_t = (isc_t - (voc_t - rs * isc_t) / rsh) * np.exp(
        -voc_t / (n_ser * vt * (t / t_ref))
    )
    iph_t = io_t * np.exp(voc_t / (n_ser * vt * (t / t_ref))) + voc_t / rsh
    iph_gt = iph_t * g_ratio

    return iph_gt, io_t, rs, rsh, a


# %%
# wartości liczbowe dla modułu PV "kyocera kc200gt"
isc = 8.21
voc = 32.9
imp = 7.61
vmp = 26.3
alpha = 3.18e-3
beta = -0.123
n_ser = 54

# temperatura i natężenie promieniowania
c = 25
g = 600

iph, io, rs, rsh, a = lambert_w(isc, voc, imp, vmp, alpha, beta, n_ser, c, g)

print(f"iph: {iph}")
print(f"io: {io}")
print(f"rs: {rs}")
print(f"rsh: {rsh}")
print(f"a: {a}")
