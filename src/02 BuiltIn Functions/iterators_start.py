# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter to create an iterator over a collection
    days_i = iter(days)
    print(days_i)
    print(next(days_i))
    print(next(days_i))

    # iterate using a function and a sentinel
    with open("testfile.txt", "r") as f:
        for line in iter(f.readline, ""):
            print(line)

    # use regular interation over the days
    for index, day in enumerate(days, start=1):
        print(f"index: {index}, day: {day}")

    # use zip to combine sequences
    for index, item in enumerate(zip(days, daysFr), start=1):
        print(f"{index} day of the Week: {item[0]} ({item[1]} in French)")


if __name__ == "__main__":
    main()
