import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import trimf, trapmf
from skfuzzy.control import Consequent, Antecedent, Rule, ControlSystem, ControlSystemSimulation

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


CzasPodlewania = Consequent(np.arange(0, 301, 1), "CzasPodlewania", defuzzify_method="centroid")
CzasPodlewania["Brak"] = trapmf(CzasPodlewania.universe, [0, 0, 5, 20])
CzasPodlewania["Krótki"] = trimf(CzasPodlewania.universe, [15, 45, 75])
CzasPodlewania["Średni"] = trimf(CzasPodlewania.universe, [70, 130, 200])
CzasPodlewania["Długi"] = trapmf(CzasPodlewania.universe, [180, 240, 300, 300])

# WilgotnoscGleby.view()
# WilgotnoscPowietrza.view()
# TemperaturaPowietrza.view()
# CzasPodlewania.view()

system = ControlSystem([
    Rule(WilgotnoscGleby["Sucha"], CzasPodlewania["Długi"]),
    Rule(WilgotnoscGleby["Wilgotna"], CzasPodlewania["Brak"]),

    Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Niska"], CzasPodlewania["Krótki"]),
    Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Optymalna"] & WilgotnoscPowietrza["Niska"], CzasPodlewania["Średni"]),
    Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Optymalna"] & WilgotnoscPowietrza["Optymalna"], CzasPodlewania["Średni"]),
    Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Optymalna"] & WilgotnoscPowietrza["Wysoka"], CzasPodlewania["Krótki"]),
    Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Niska"], CzasPodlewania["Długi"]),
    Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Optymalna"], CzasPodlewania["Długi"]),
    Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Wysoka"], CzasPodlewania["Średni"]),

    Rule(WilgotnoscGleby["Optymalna"] & TemperaturaPowietrza["Niska"], CzasPodlewania["Brak"]),
    Rule(WilgotnoscGleby["Optymalna"] & TemperaturaPowietrza["Optymalna"], CzasPodlewania["Brak"]),
    Rule(WilgotnoscGleby["Optymalna"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Niska"], CzasPodlewania["Krótki"]),
    Rule(WilgotnoscGleby["Optymalna"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Optymalna"], CzasPodlewania["Krótki"]),
    Rule(WilgotnoscGleby["Optymalna"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Wysoka"], CzasPodlewania["Brak"]),
])

simulation = ControlSystemSimulation(system)
simulation.input["WilgotnoscGleby"] = 20
simulation.input["WilgotnoscPowietrza"] = 40
simulation.input["TemperaturaPowietrza"] = 20
simulation.compute()

print(simulation.output["CzasPodlewania"])