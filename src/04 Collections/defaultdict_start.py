# Demonstrate the usage of defaultdict objects
import collections


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruit_counter = {}

    # Count the elements in the list
    for fruit in fruits:
        fruit_counter[fruit] = fruit_counter[fruit] + 1 if fruit in fruit_counter else 1

    # print the result
    # for (k, v) in fruit_counter.items():
    #     print(k + ": " + str(v))

    # do the same, but with DefaultDict
    fruit_counter = collections.defaultdict(int)
    # fruit_counter = collections.defaultdict(lambda: 0)
    for fruit in fruits:
        fruit_counter[fruit] += 1

    # print the result
    for (k, v) in fruit_counter.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
