import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import trimf
from skfuzzy.control import Consequent, Antecedent

RPM = Antecedent(np.arange(0, 10200, 200), "RPM")
MAP = Antecedent(np.arange(0, 205, 5), "MAP (kPa)")

AFR = Consequent(np.arange(8, 16, .1), 'AFR', defuzzify_method='centroid')

RPM["idle"] = trimf(RPM.universe, [0, 0, 1000])
RPM["low"] = trimf(RPM.universe, [0, 1000, 2000])
RPM["cruise"] = trimf(RPM.universe, [1500, 2500, 3500])
RPM["high"] = trimf(RPM.universe, [3000, 5000, 7000])
RPM["very high"] = trimf(RPM.universe, [5000, 10000, 10000])

MAP["idle"] = trimf(MAP.universe, [0, 0, 30])
MAP["cruise"] = trimf(MAP.universe, [20, 40, 80])
MAP["mild"] = trimf(MAP.universe, [50, 70, 90])
MAP["atmospheric"] = trimf(MAP.universe, [80, 90, 100])
MAP["low boost"] = trimf(MAP.universe, [90, 150, 200])
MAP["high boost"] = trimf(MAP.universe, [150, 200, 200])

MAP.view()