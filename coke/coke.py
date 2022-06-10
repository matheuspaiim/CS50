# :) coke.py exists
# :( coke accepts 25 cents
   # expected "25", not ""
# :( coke accepts 10 cents
   # expected "40", not ""
# :( coke accepts 5 cents
   # expected "45", not ""
# :( coke rejects invalid amount of cents
   # expected "50", not ""
# :( coke accepts continued input
   # expected prompt for input, found none
# :( coke terminates at 50 cents
   # expected prompt for input, found none
# :( coke provides correct change
   # expected prompt for input, found none

def main():
    global amount
    amount = 50
    print(f"Amount Due: {amount}")
    coke()
    ...

def coke():
    global coin
    buy = amount - coin

    while amount <= 50:
        coin = int(input("Insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            print(f"Amount Due: {buy}")
    ...

if __name__ == "__main__":
    main()