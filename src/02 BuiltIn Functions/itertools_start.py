# advanced iteration functions in the itertools package
import itertools


def less_than_fifty(x):
    return x < 50


def main():
    # cycle iterator can be used to cycle over a collection
    seq = ["Joe", "John", "Mike"]
    cycle = itertools.cycle(seq)
    for name in range(5):
        print(next(cycle))

    # use count to create a simple counter
    counter = itertools.count(start=3, step=2)
    for i in range(3):
        print(next(counter))

    # accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals)
    print(list(acc))

    # use chain to connect sequences together
    chain = itertools.chain("first", "second")
    print(list(chain))
    
    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(less_than_fifty, vals)))
    print(list(itertools.takewhile(less_than_fifty, vals)))


if __name__ == "__main__":
    main()
    