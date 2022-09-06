# Functions and parameters
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

# Returning function
def main2():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    
def square(n):
    return n * n

main2()