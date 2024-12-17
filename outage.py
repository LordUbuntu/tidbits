# Jacobus Burger (2024-12-16)
# Power outage happened recently for a second before I assume the backup generator of the grid kicked in. This inspired a simple ascii game idea where you type out the letter of a station when it goes out to power it back on, can't leave a station off for too long or you lose! This may be a full project so for now here's a little placeholder:
import termcolor

def placeholder():
    print(termcolor.colored("POWER OUTAGE", "yellow", "on_red", attrs=["bold", "blink", "underline"]))

if __name__ == "__main__":
    placeholder()
