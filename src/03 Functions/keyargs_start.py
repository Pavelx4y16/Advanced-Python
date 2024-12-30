# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def just(arg1, arg2, *, important_arg):
    print(arg1, arg2, important_arg)


def main():
    # try to call the function without the keyword
    # just(1, 2, True)
    just(1, 2, important_arg=True)


if __name__ == "__main__":
    main()
