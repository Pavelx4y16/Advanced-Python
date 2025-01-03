# customize string representations of objects


class Person:
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f"<Person: " \
               f"fname = '{self.fname}', " \
               f"lname = '{self.lname}', " \
               f"age = '{self.age}'>"

    # use str for a more human-readable string
    def __str__(self):
        return f"{self.fname} is of age {self.age}"

    def __bytes__(self):
        return f"{self.fname}, {self.lname}, {self.age}".encode()

def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))
    print(bytes(cls1))


if __name__ == "__main__":
    main()
