"""Roll a chosen number of six-sided dice."""

import random


def main():
    try:
        count = int(input("How many dice? "))
        if count < 1:
            raise ValueError
    except ValueError:
        print("Enter a positive whole number.")
        return
    rolls = [random.randint(1, 6) for _ in range(count)]
    print("Rolls:", ", ".join(map(str, rolls)))
    print("Total:", sum(rolls))


if __name__ == "__main__":
    main()
