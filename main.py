from matplotlib import pyplot as plt

from podlewanie.simulation import Simulation
from podlewanie.vars import WilgotnoscGleby, TemperaturaPowietrza, WilgotnoscPowietrza, get_CzasPodlewania_var

METHODS = ("centroid", "som", "bisector")

scenarios = [
    {
        "WilgotnoscGleby":      12,
        "TemperaturaPowietrza": 35,
        "WilgotnoscPowietrza":  30,
    },
    {
        "WilgotnoscGleby":      21,
        "TemperaturaPowietrza": 28,
        "WilgotnoscPowietrza":  75,
    },
    {
        "WilgotnoscGleby":      22,
        "TemperaturaPowietrza": 24,
        "WilgotnoscPowietrza":  65,
    },
    {
        "WilgotnoscGleby":      22,
        "TemperaturaPowietrza": 30,
        "WilgotnoscPowietrza":  50,
    },
]

if __name__ == "__main__":

    sim = Simulation("bisector")

    x = sim.WilgotnoscPowietrza.universe
    for scenario in scenarios:
        y = []
        sim.set_input_values(scenario)
        for _x in x:
            sim.set_input_values({"WilgotnoscPowietrza": _x})
            y.append(sim.compute())
        plt.plot(x, y)
        plt.show()

