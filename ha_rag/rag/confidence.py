def compute_confidence(distances):
    if not distances:
        return 0.0

    avg = sum(distances) / len(distances)
    return round(float(1 / (1 + avg)), 2)