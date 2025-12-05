import numpy as np
from skfuzzy import trapmf, trimf
from skfuzzy.control import Antecedent, Consequent

WilgotnoscGleby = Antecedent(np.arange(10, 46, 1), "WilgotnoscGleby")
WilgotnoscGleby["Sucha"] = trapmf(WilgotnoscGleby.universe, [10, 10, 12, 22])
WilgotnoscGleby["Umiarkowana"] = trapmf(WilgotnoscGleby.universe, [18, 24, 28, 32])
WilgotnoscGleby["Optymalna"] = trimf(WilgotnoscGleby.universe, [26, 31, 36])
WilgotnoscGleby["Wilgotna"] = trapmf(WilgotnoscGleby.universe, [34, 40, 45, 45])


WilgotnoscPowietrza = Antecedent(np.arange(30, 91, 1), "WilgotnoscPowietrza")
WilgotnoscPowietrza["Niska"] = trapmf(WilgotnoscPowietrza.universe, [30, 30, 45, 60])
WilgotnoscPowietrza["Optymalna"] = trapmf(WilgotnoscPowietrza.universe, [55, 60, 70, 75])
WilgotnoscPowietrza["Wysoka"] = trapmf(WilgotnoscPowietrza.universe, [70, 75, 90, 90])


TemperaturaPowietrza = Antecedent(np.arange(10, 41, 1), "TemperaturaPowietrza")
TemperaturaPowietrza["Niska"] = trapmf(TemperaturaPowietrza.universe, [10, 10, 14, 22])
TemperaturaPowietrza["Optymalna"] = trapmf(TemperaturaPowietrza.universe, [18, 22, 26, 30])
TemperaturaPowietrza["Wysoka"] = trapmf(TemperaturaPowietrza.universe, [26, 30, 40, 40])


def get_CzasPodlewania_var(method: str):
    var = Consequent(np.arange(0, 301, 1), "CzasPodlewania", defuzzify_method=method)
    var["Brak"] = trapmf(var.universe, [0, 0, 5, 20])
    var["Krótki"] = trimf(var.universe, [15, 45, 75])
    var["Średni"] = trimf(var.universe, [70, 130, 200])
    var["Długi"] = trapmf(var.universe, [180, 240, 300, 300])
    return var