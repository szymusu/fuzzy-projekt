from skfuzzy.control import Rule


def get_rules(wg, tp, wp, cp):
    return [
        Rule(wg["Sucha"], cp["Dlugi"]),
        Rule(wg["Umiarkowana"] & tp["Niska"], cp["Krotki"]),

        Rule(wg["Umiarkowana"] & tp["Optymalna"] & wp["Niska"], cp["Sredni"]),
        Rule(wg["Umiarkowana"] & tp["Optymalna"] & wp["Optymalna"], cp["Sredni"]),
        Rule(wg["Umiarkowana"] & tp["Optymalna"] & wp["Wysoka"], cp["Krotki"]),
        Rule(wg["Umiarkowana"] & tp["Wysoka"] & wp["Niska"], cp["Dlugi"]),
        Rule(wg["Umiarkowana"] & tp["Wysoka"] & wp["Optymalna"], cp["Dlugi"]),
        Rule(wg["Umiarkowana"] & tp["Wysoka"] & wp["Wysoka"], cp["Sredni"]),

        Rule(wg["Optymalna"] & tp["Niska"], cp["Brak"]),
        Rule(wg["Optymalna"] & tp["Optymalna"], cp["Brak"]),

        Rule(wg["Optymalna"] & tp["Wysoka"] & wp["Niska"], cp["Krotki"]),
        Rule(wg["Optymalna"] & tp["Wysoka"] & wp["Optymalna"], cp["Krotki"]),
        Rule(wg["Optymalna"] & tp["Wysoka"] & wp["Wysoka"], cp["Brak"]),

        Rule(wg["Wilgotna"], cp["Brak"]),
    ]