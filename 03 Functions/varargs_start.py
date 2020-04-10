# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result



def main():
    # TODO: pass different arguments
    print(addition(2,4,10))
    print(addition(10,20,30,50))

    # TODO: pass an existing list
    nums = [1,2,3]
    print(addition(*nums))


if __name__ == "__main__":
    main()
