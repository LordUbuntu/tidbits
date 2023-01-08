#!/usr/bin/python3
# Info:
#   Momento mori.
from datetime import date


def age(birth_date):
    # determines important info based on given age (in form YYYY-MM-DD)
    today = date.today()
    expected_death = date(2080, 12, 14)
    years_alive = today.year - birth_date.year
    days_alive = (today - birth_date).days
    days_left = (expected_death - today).days
    years_left = (expected_death - today).years
    print(f"you were born {years_alive} years ago")
    print(f"you have been alive for {days_alive} days")
    print(f"you have approximately {days_left} days left to live")
    print(f"you have approximately {years_left} years left to live")


def parse_date(user_date):
    # converts string of form (YYYY-MM-DD) into a datetime representation
    L = []
    for part in user_date.split("-"):
        L.append(int(part))
    return date(L[0], L[1], L[2])


def main():
    age(parse_date(input("when were you born (YYYY-MM-DD)? ")))


if __name__ == "__main__":
    main()
