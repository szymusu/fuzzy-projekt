from skfuzzy.control import Rule


def get_rules(wg, tp, wp, cp):
    return [
        Rule(wg["Sucha"], cp["Długi"]),
        Rule(wg["Wilgotna"], cp["Brak"]),

        Rule(wg["Umiarkowana"] & tp["Niska"], cp["Krótki"]),
        Rule(wg["Umiarkowana"] & tp["Optymalna"] & wp["Niska"], cp["Średni"]),
        Rule(wg["Umiarkowana"] & tp["Optymalna"] & wp["Optymalna"], cp["Średni"]),
        Rule(wg["Umiarkowana"] & tp["Optymalna"] & wp["Wysoka"], cp["Krótki"]),
        Rule(wg["Umiarkowana"] & tp["Wysoka"] & wp["Niska"], cp["Długi"]),
        Rule(wg["Umiarkowana"] & tp["Wysoka"] & wp["Optymalna"], cp["Długi"]),
        Rule(wg["Umiarkowana"] & tp["Wysoka"] & wp["Wysoka"], cp["Średni"]),

        Rule(wg["Optymalna"] & tp["Niska"], cp["Brak"]),
        Rule(wg["Optymalna"] & tp["Optymalna"], cp["Brak"]),
        Rule(wg["Optymalna"] & tp["Wysoka"] & wp["Niska"], cp["Krótki"]),
        Rule(wg["Optymalna"] & tp["Wysoka"] & wp["Optymalna"], cp["Krótki"]),
        Rule(wg["Optymalna"] & tp["Wysoka"] & wp["Wysoka"], cp["Brak"]),
    ]