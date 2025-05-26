def main():
    n1,n2 = get_numbers()
    add(n1,n2)

def get_numbers():
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    return a,b

def add(x,y):
    z = x + y
    print(z)

main()