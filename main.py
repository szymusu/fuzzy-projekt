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
    # print("Scenariusz 1", compute(in_WilgotnoscGleby=10, in_TemperaturaPowietrza=35, in_WilgotnoscPowietrza=30))
    # print("Scenariusz 2", compute(in_WilgotnoscGleby=10, in_TemperaturaPowietrza=35, in_WilgotnoscPowietrza=90))
    # print("Scenariusz 3", compute(in_WilgotnoscGleby=20, in_TemperaturaPowietrza=12, in_WilgotnoscPowietrza=80))
    # print("Scenariusz 4", compute(in_WilgotnoscGleby=32, in_TemperaturaPowietrza=24, in_WilgotnoscPowietrza=65))

    for i, scenario in enumerate(scenarios):
        sim = Simulation("centroid")
        sim.set_input_values(scenario)
        print(f"\nScenariusz {i+1}")
        print(scenario)
        print(sim.compute())
