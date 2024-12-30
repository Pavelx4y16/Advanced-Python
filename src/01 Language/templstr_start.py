# demonstrate template string functions
from string import Template


def main():
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # create a template with placeholders
    template = Template("You're watching ${title} by ${author}")

    # use the substitute method with keyword arguments
    str2 = template.substitute(title="Just some course", author="Pavel Savastseika")
    print(str2)
    # use the substitute method with a dictionary
    params = {
        "title": "Some Course",
        "author": "Some Author",
    }
    str3 = template.substitute(params)
    print(str3)

    
if __name__ == "__main__":
    main()
    