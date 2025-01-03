# define enumerations using the Enum base class
from enum import Enum, auto, unique


@unique
class Fruit(Enum):
    APPLE = 1
    BANNANA = auto()
    PEAR = auto()


def main():
    pass
    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print the auto-generated value
    print(Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    d = {Fruit.APPLE: "some very delicious apple"}
    print(d[Fruit.APPLE])


if __name__ == "__main__":
    main()
