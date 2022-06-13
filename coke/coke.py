# :) coke.py exists
# :) coke accepts 25 cents
# :) coke accepts 10 cents
# :) coke accepts 5 cents
# :) coke rejects invalid amount of cents
# :) coke accepts continued input
# :) coke terminates at 50 cents
# :) coke provides correct change

def main():

    global amount
    amount = 50
    coke()
    ...

def coke():

    global amount
    print(f"Amount Due: {amount}")

    while amount <= 50 and amount >= 0:

        coin = int(input("Insert coin: "))
        buy = amount - coin
        change = abs(buy)

        if buy > 0 and coin in [25, 10, 5]:
            print(f"Amount Due: {buy}")
            amount -= coin

        elif buy == 0:
            print(f"Change Owed: {buy}")
            break

        elif buy < 0:
            print(f"Change Owed: {change}")
            break

        else:
            print(f"Amount Due: {amount}")

    ...

if __name__ == "__main__":
    main()