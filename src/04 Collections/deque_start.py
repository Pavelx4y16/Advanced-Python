# deque objects are like double-ended queues

import collections
import string


def main():
    
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print(len(d))

    # deques can be iterated over
    for item in d:
        print(item, end=" ")
    print()

    # manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)

    # rotate the deque
    d.rotate(2)
    print(d)


if __name__ == "__main__":
    main()
