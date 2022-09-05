

def make_multiplier(multiplier: float) -> callable:
    def multiplier(multiplier):
        return multiplier * multiplier
    return multiplier
