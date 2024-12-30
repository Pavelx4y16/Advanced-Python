# use transform functions like sorted, filter, map

def to_grade(x):
    if x >= 90:
        return "A"
    if x >= 80:
        return "B"
    if x >= 70:
        return "C"
    if x >= 65:
        return "D"

    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # use filter to remove items from a list
    odds = list(filter(lambda x: x % 2 == 1, nums))
    print(odds)

    # use filter on non-numeric sequence
    lowers = list(filter(lambda ch: ch.islower(), chars))
    print("".join(lowers))

    # use map to create a new sequence of values
    squares = list(map(lambda x: x**2, nums))
    print(squares)

    # use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(to_grade, grades))
    print(letters)


if __name__ == "__main__":
    main()
