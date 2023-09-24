# Jacobus Burger (2023)
# A program that converts a normal sentence into pig latin

def pig(sentence: str) -> str:
    return ' '.join(word[1:]+word[0]+"ay" for word in sentence.split())


if __name__ == '__main__':
    print(pig(input()))
