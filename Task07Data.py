# CONTROL: PY-07-A-80819

def build_data():
    scores = {"Алиса": 65, "Борис": 80, "Вика": 58, "Глеб": 95}
    fines = {"Алиса": 10, "Борис": 40, "Вика": 3, "Глеб": 60}
    result = {}

    for name in scores:
        points = scores[name] - fines[name]
        if points < 0:
            points = 0
        if points >= 50:
            points = points + 5
        result[name] = points

    return result
