# Demonstrate the usage of Counter objects

from collections import Counter


def main():
    # list of students in class 1
    class_1 = [
        "Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah", "Kevin", "James", "James", "Melanie", "Penny", "Steve"
    ]

    # list of students in class 2
    class_2 = [
        "Bill", "Barry", "Cindy", "Debbie", "Frank", "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"
    ]

    # Create a Counter for class1 and class2
    c1 = Counter(class_1)
    c2 = Counter(class_2)

    # How many students in class 1 named James?
    print(c1["James"])
    print(c1["Undefined"])

    # How many students are in class 1?
    print(sum(c1.values()))

    # Combine the two classes
    c1 += c2
    print(sum(c1.values()))

    # What's the most common name in the two classes?
    print(c1.most_common(3))

    # Separate the classes again
    c1 -= c2
    print(c1.most_common(3))

    # What's common between the two classes?
    print(c1 & c2)


if __name__ == "__main__":
    main()
