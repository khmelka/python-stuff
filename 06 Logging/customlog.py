# Demonstrate how to customize logging output

import logging

extraData={
    'user': 'user@ex.com'
}

# TODO: add another function to log from
def anotherFun():
    logging.debug("This is a debug-level message", extra=extraData)

def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtstr="%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"

    datestr = "%m/%d/%Y %I:%M:%S %p" 

    logging.basicConfig(filename="output.log", 
                        level=logging.DEBUG,
                        format=fmtstr,
                        datefmt=datestr)

    logging.info("This is an info-level log message", extra=extraData)
    logging.warning("This is a warning-level message", extra=extraData)
    anotherFun()


if __name__ == "__main__":
    main()
 