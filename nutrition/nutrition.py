# :) nutrition.py exists
# :) input of apple yields output of 130
# :) input of Avocado yields output of 50
# :) input of Kiwifruit yields output of 90
# :) input of pear yields output of 100
# :) input of Sweet Cherries yields output of 100
# :) nutrition.py ignores invalid input

def main():
    item = input("Item: ").lower()
    check_calories(item)
    ...


def check_calories(item):

    raw_fruits = {
       "apple": 130,
       "avocado": 50,
       "banana": 110,
       "vantaloupe": 50,
       "grapefruit": 60,
       "grapes": 90,
       "honeydew melon": 50,
       "kiwifruit": 90,
       "lemon": 15,
       "lime": 20,
       "nectarine": 60,
       "orange": 80,
       "peach": 60,
       "pear": 100,
       "pineapple": 50,
       "plums": 70,
       "strawberries": 50,
       "sweet cherries": 100,
       "tangerine": 50,
       "watermelon": 80
       }

    for fruit in raw_fruits:
        if fruit in item:
            print("Calories:", raw_fruits[fruit])
            ...


if __name__ == "__main__":
    main()