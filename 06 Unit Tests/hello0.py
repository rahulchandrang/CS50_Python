# Function to be tested


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to) #Here print dont return any values. So we cant use assert in test


if __name__ == "__main__":
    main()
