# Jacobus Burger (2023)
# A program that converts a normal sentence into pig latin

def pig(sentence: str) -> str:
    result = []
    for word in sentence.split():
        result.append(word[1:] + word[0] + "ay")
    return ' '.join(result)


if __name__ == '__main__':
    print(pig(input()))
