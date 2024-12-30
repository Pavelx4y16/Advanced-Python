# demonstrate built-in utility functions


def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]
    print(f"List: {list1}")
    
    # any will return true if any of the sequence values are true
    print(f"Any: {any(list1)}")
    # all will return true only if all values are true
    print(f"All: {all(list1)}")
    # min and max will return minimum and maximum values in a sequence
    print(f"Min: {min(list1)}")
    print(f"Max: {max(list1)}")
    # Use sum() to sum up all of the values in a sequence
    print(f"Sum: {sum(list1)}")


if __name__ == "__main__":
    main()
    