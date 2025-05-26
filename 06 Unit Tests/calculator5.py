# Tests a function with one function via pytest
# Use pytest <yest_filename> to run this

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n + n


if __name__ == "__main__":
    main()
