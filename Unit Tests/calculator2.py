# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n + n #Purposefully failing the program


if __name__ == "__main__":
    main()
