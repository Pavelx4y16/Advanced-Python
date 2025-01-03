# Demonstrate how to use list comprehensions


def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Perform a mapping and filter function on a list
    even_squared = list(map(lambda x: x**2, filter(lambda x: 4 < x < 16, evens)))
    print(even_squared)

    # Derive a new list of numbers frm a given list
    even_squared = [x ** 2 for x in evens if 4 < x < 16]
    print(even_squared)


if __name__ == "__main__":
    main()
