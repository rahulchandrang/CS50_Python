# Prints square of bricks using a function with nested loops


def main():
    print_square(3)


def print_square(size):
    # For each row in square
    for i in range(size):

            # For each brick in row

        for j in range(size):

            # print brick
            print("#", end="")
        print()


main()
