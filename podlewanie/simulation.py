from skfuzzy.control import ControlSystem, ControlSystemSimulation

from podlewanie.rules import get_rules
from podlewanie.vars import WilgotnoscGleby, TemperaturaPowietrza, WilgotnoscPowietrza, get_CzasPodlewania_var

class Simulation:
    def __init__(self, method: str):
        self.WilgotnoscGleby = WilgotnoscGleby
        self.TemperaturaPowietrza = TemperaturaPowietrza
        self.WilgotnoscPowietrza = WilgotnoscPowietrza
        self.CzasPodlewania = get_CzasPodlewania_var(method)

        self.system = ControlSystem(get_rules(
            WilgotnoscGleby, TemperaturaPowietrza, WilgotnoscPowietrza, self.CzasPodlewania
        ))
        self.simulation = ControlSystemSimulation(self.system)

    def set_input_values(self, input_values: dict[str, float]):
        for k in input_values:
            assert k in ("WilgotnoscGleby", "TemperaturaPowietrza", "WilgotnoscPowietrza")
            self.simulation.input[k] = input_values[k]

    def compute(self):
        self.simulation.compute()
        return self.simulation.output["CzasPodlewania"]