# Jacobus Burger (2023)
# Info:
#   Inspired by listening to some Cab Calloway, decided to make a program
#   to convert a string to scat with decent flow. While working on it
#   I realized that this is a decently complex problem.


def scat(string: str) -> str:
    scats = {
        'a': "aah",
        'b': "bap",
        'd': "do",
        'e': "ee",
        'f': "fee",
        'g': "gah",
        'h': "hee",
        'i': "idi",
        'j': "jack",
        'k': "kap",
        'l': "lee",
        'm': "mo",
        'n': "nap",
        'o': "oo",
        'p': "pah",
        'q': "quick",
        'r': "rum",
        's': "scat",
        't': "tat",
        'u': "udu",
        'v': "vee",
        'w': "wee",
        'x': "zee",
        'z': "zap"
    }
    result = []
    for i in range(len(string)):
        phrase = scats.get(string[i], None)
        if phrase is not None:
            result.append(phrase)
        else:
            result.append(string[i])
    return ''.join(result)


if __name__ == '__main__':
    string = input("gimmie a rhyme: ").lower()
    print(scat(string))
