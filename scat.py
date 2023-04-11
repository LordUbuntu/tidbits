# Jacobus Burger (2023)
# Info:
#   Inspired by listening to some Cab Calloway, decided to make a program
#   to convert a string to scat with decent flow. While working on it
#   I realized that this is a decently complex problem.


def scat(string: str) -> str:
    scats = {
        'b': "bap",
        'd': "dee",
        'e': "ee",
        'f': "fee",
        'h': "hee",
        'j': "jack",
        'k': "kap",
        'l': "lee",
        'm': "mo",
        'n': "nap",
        'o': "oo",
        'p': "pah",
        'r': "rum",
        's': "scat",
        't': "tat",
        'v': "vee",
        'w': "wee",
        'z': "zap"
    }
    result = []
    i = 0
    while i < len(string):
        phrase = scats.get(string[i], None)
        if phrase is not None:
            result.append(phrase)
        else:
            result.append(string[i])
        i += 1
    return result