import matplotlib.pyplot as plt
import numpy as np

from podlewanie.model import compute


if __name__ == "__main__":
    print("Scenariusz 1", compute(in_WilgotnoscGleby=10, in_TemperaturaPowietrza=35, in_WilgotnoscPowietrza=30))
    print("Scenariusz 2", compute(in_WilgotnoscGleby=10, in_TemperaturaPowietrza=35, in_WilgotnoscPowietrza=90))
    print("Scenariusz 3", compute(in_WilgotnoscGleby=20, in_TemperaturaPowietrza=12, in_WilgotnoscPowietrza=80))
    print("Scenariusz 4", compute(in_WilgotnoscGleby=32, in_TemperaturaPowietrza=24, in_WilgotnoscPowietrza=65))

    TP = 20
    WP = 65
    WG = 31
    x = np.arange(30, 91, 1)
    y = []
    for wp in x:
        y.append(compute(WG, TP, wp)["centroid"])

    plt.plot(x, y)
    plt.show()
