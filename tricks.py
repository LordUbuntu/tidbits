# a collection of tricks I've made in Python


def finish(generator) -> list:
    """Instantiate all values in a generator into a list"""
    return [*generator]

def flatten(L: list) -> list:
    """Flattens a nested list down one dimension"""
    return [*l for l in L]
