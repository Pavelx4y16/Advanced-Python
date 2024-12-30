# Demonstrate the use of variable argument lists


# define a function that takes variable arguments
def addition(*args):
    return sum(args)


def main():
    # pass different arguments
    print(addition(3, 4, 5))
    print(addition(3, -3, 5, -5))
    print(addition())
    print(addition(0))

    # pass an existing list
    print(addition(*[3, 2, 1]))


if __name__ == "__main__":
    main()
