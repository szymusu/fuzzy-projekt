import numpy as np
from skfuzzy import trapmf, trimf
from skfuzzy.control import Antecedent, Consequent

WilgotnoscGleby = Antecedent(np.arange(10, 46, 1), "WilgotnoscGleby")
WilgotnoscGleby["Sucha"] = trapmf(WilgotnoscGleby.universe, [10, 10, 16, 18])
WilgotnoscGleby["Umiarkowana"] = trapmf(WilgotnoscGleby.universe, [16, 18, 21, 22])
WilgotnoscGleby["Optymalna"] = trapmf(WilgotnoscGleby.universe, [18, 22, 27, 32])
WilgotnoscGleby["Wilgotna"] = trapmf(WilgotnoscGleby.universe, [27, 32, 45, 45])

TemperaturaPowietrza = Antecedent(np.arange(10, 41, 1), "TemperaturaPowietrza")
TemperaturaPowietrza["Niska"] = trapmf(TemperaturaPowietrza.universe, [10, 10, 16, 20])
TemperaturaPowietrza["Optymalna"] = trapmf(TemperaturaPowietrza.universe, [16, 22, 26, 30])
TemperaturaPowietrza["Wysoka"] = trapmf(TemperaturaPowietrza.universe, [26, 30, 40, 40])

WilgotnoscPowietrza = Antecedent(np.arange(30, 91, 1), "WilgotnoscPowietrza")
WilgotnoscPowietrza["Niska"] = trapmf(WilgotnoscPowietrza.universe, [30, 30, 45, 60])
WilgotnoscPowietrza["Optymalna"] = trapmf(WilgotnoscPowietrza.universe, [55, 60, 70, 75])
WilgotnoscPowietrza["Wysoka"] = trapmf(WilgotnoscPowietrza.universe, [70, 75, 90, 90])

def get_CzasPodlewania_var(method: str):
    var = Consequent(np.arange(0, 301, 1), "CzasPodlewania", defuzzify_method=method)
    var["Brak"] = trimf(var.universe, [0, 0, 0])
    var["Krotki"] = trapmf(var.universe, [0, 30, 60, 90])
    var["Sredni"] = trapmf(var.universe, [60, 90, 150, 180])
    var["Dlugi"] = trapmf(var.universe, [150, 180, 240, 300])
    return var
