#!/usr/bin/python3
# Info:
#   Momento mori.
import datetime


def age(birthday, expected_lifespan=80):
    # determines important info based on given age (in form YYYY-MM-DD)
    today = datetime.date.today()
    expected_death = datetime.date(birthday.year + expected_lifespan, 12, 1)
    years_alive = today.year - birthday.year
    days_alive = (today - birthday).days
    weeks_alive = days_alive // 7
    days_left = (expected_death - today).days
    weeks_left = days_left // 7
    years_left = (expected_death - today).days // 365
    print(f"you were born {years_alive} years ago")
    print(f"you have been alive for {days_alive} days / {weeks_alive} weeks")
    print(f"you have approximately {days_left} days / {weeks_left} weeks / {years_left} years left to live assuming you live for {expected_lifespan} years")
    print(f"You've lived {(years_alive / expected_lifespan) * 100}% of your life. Remember that it's never too late to do anything until you're already dead! Make the most of the rest, and keep growing!!")


def parse_date(user_date):
    return datetime.date.fromisoformat(user_date)


def main():
    # assumes this is before the 10000's or year would be YYYYY
    birthday = parse_date(input("when were you born (YYYY-MM-DD)? "))
    age(birthday)


if __name__ == "__main__":
    main()
