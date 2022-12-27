# Jacobus Burger (2022)
# Implements recursive acronyms


# GNU => GNU is Not Unix
def GNU_is_Not_Unix(times: int, string="GNU is Not Unix"):
    if times == 0:
        return string + " is Not Unix"
    return GNU_is_Not_Unix(times - 1, string + " is Not Unix")


if __name__ == '__main__':
    print(GNU_is_Not_Unix(3))
