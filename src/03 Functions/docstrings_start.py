# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """Doesn't really do anything, just prints.

    Args:
        arg1: the first argument
        arg2: second argument.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
