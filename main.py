import matplotlib.pyplot as plt
import numpy as np

from podlewanie.simulation import Simulation

METHODS = ("centroid", "lom", "bisector")

scenarios = [
    {
        "WilgotnoscGleby":      10,
        "TemperaturaPowietrza": 35,
        "WilgotnoscPowietrza":  30,
    },
    {
        "WilgotnoscGleby":      10,
        "TemperaturaPowietrza": 35,
        "WilgotnoscPowietrza":  90,
    },
    {
        "WilgotnoscGleby":      20,
        "TemperaturaPowietrza": 12,
        "WilgotnoscPowietrza":  80,
    },
    {
        "WilgotnoscGleby":      32,
        "TemperaturaPowietrza": 24,
        "WilgotnoscPowietrza":  65,
    },
]

if __name__ == "__main__":

    sim = Simulation("bisector")
    sim.set_input_values(scenarios[3])
    sim.compute()
    sim.view_activation()
    exit()

    for i, scenario in enumerate(scenarios):
        sim = Simulation("centroid")
        sim.set_input_values(scenario)
        print(f"\nScenariusz {i+1}")
        print(scenario)
        print(sim.compute())
