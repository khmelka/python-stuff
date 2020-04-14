# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    ftemp1=[(t*9/5)+32 for t in ctemps]
    ftemp2={(t*9/5)+32 for t in ctemps}
    print(ftemp1)
    print(ftemp2)


    # TODO: build a set of unique Fahrenheit temperatures

    # TODO: build a set from an input source
    sTemp="The weather is great"
    chars={c.upper() for c in sTemp if not c.isspace()}
    print(chars)


if __name__ == "__main__":
    main()
