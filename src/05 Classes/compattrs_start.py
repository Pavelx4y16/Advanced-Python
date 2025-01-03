# customize string representations of objects


class MyColor:
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgb":
            return self.red, self.green, self.blue
        else:
            raise AttributeError

    # use setattr to dynamically set a value
    def __setattr__(self, attr, val):
        if attr == "rgb":
            self.red, self.green, self.blue = val
        else:
            super().__setattr__(attr, val)

    # use dir to list the available properties
    def __dir__(self):
        return ["red", "green", "blue", "rgb"]


def main():
    # create an instance of myColor
    color = MyColor()
    # print the value of a computed attribute
    print(color.rgb)

    # set the value of a computed attribute
    color.rgb = (1, 2, 3)
    print(color.rgb)

    # access a regular attribute
    print(color.green)

    # list the available attributes
    print(dir(color))


if __name__ == "__main__":
    main()
