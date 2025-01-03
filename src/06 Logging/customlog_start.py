# Demonstrate how to customize logging output

import logging


extra_data = {
    "user": "user@gmail.com",
}


# add another function to log from
def another_function():
    logging.debug("Some debug message", extra=extra_data)


def main():
    # set the output file and debug level, and
    # use a custom formatting specification
    fmtstr = "User: %(user)s, %(asctime)s, %(levelname)s, %(funcName)s, Line %(lineno)d: %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(
        filename="output.log",
        level=logging.DEBUG,
        filemode="w",
        format=fmtstr,
        datefmt=datestr,
    )

    logging.info("This is an info-level log message", extra=extra_data)
    logging.warning("This is a warning-level message", extra=extra_data)

    another_function()


if __name__ == "__main__":
    main()
