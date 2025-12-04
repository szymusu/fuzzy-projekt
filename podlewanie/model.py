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

# WilgotnoscGleby.view()
# WilgotnoscPowietrza.view()
# TemperaturaPowietrza.view()
# CzasPodlewania.view()
systems = {}
for method in ("centroid", "lom", "bisector"):
    var = Consequent(np.arange(0, 301, 1), "CzasPodlewania", defuzzify_method=method)
    var["Brak"] = trapmf(var.universe, [0, 0, 5, 20])
    var["Krótki"] = trimf(var.universe, [15, 45, 75])
    var["Średni"] = trimf(var.universe, [70, 130, 200])
    var["Długi"] = trapmf(var.universe, [180, 240, 300, 300])
    systems[method] = ControlSystem([
        Rule(WilgotnoscGleby["Sucha"], var["Długi"]),
        Rule(WilgotnoscGleby["Wilgotna"], var["Brak"]),

        Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Niska"], var["Krótki"]),
        Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Optymalna"] & WilgotnoscPowietrza["Niska"], var["Średni"]),
        Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Optymalna"] & WilgotnoscPowietrza["Optymalna"], var["Średni"]),
        Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Optymalna"] & WilgotnoscPowietrza["Wysoka"], var["Krótki"]),
        Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Niska"], var["Długi"]),
        Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Optymalna"], var["Długi"]),
        Rule(WilgotnoscGleby["Umiarkowana"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Wysoka"], var["Średni"]),

        Rule(WilgotnoscGleby["Optymalna"] & TemperaturaPowietrza["Niska"], var["Brak"]),
        Rule(WilgotnoscGleby["Optymalna"] & TemperaturaPowietrza["Optymalna"], var["Brak"]),
        Rule(WilgotnoscGleby["Optymalna"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Niska"], var["Krótki"]),
        Rule(WilgotnoscGleby["Optymalna"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Optymalna"], var["Krótki"]),
        Rule(WilgotnoscGleby["Optymalna"] & TemperaturaPowietrza["Wysoka"] & WilgotnoscPowietrza["Wysoka"], var["Brak"]),
    ])


def compute(in_WilgotnoscGleby, in_TemperaturaPowietrza, in_WilgotnoscPowietrza):
    answers = {}
    for method in ("centroid", "lom", "bisector"):
        simulation = ControlSystemSimulation(systems[method])
        simulation.input["WilgotnoscGleby"] = in_WilgotnoscGleby
        simulation.input["WilgotnoscPowietrza"] = in_WilgotnoscPowietrza
        simulation.input["TemperaturaPowietrza"] = in_TemperaturaPowietrza
        simulation.compute()
        answers[method] = float(simulation.output["CzasPodlewania"])

    return answers