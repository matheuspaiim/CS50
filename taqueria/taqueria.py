
try:
    while True:
        menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
        item = input("Item: ").capitalize()
        for key in menu:
            if key in item:
                print(f'Total: ${menu[key]:.2f}')
                menu[key] += menu[key]
        break
except EOFError:
    pass
except KeyError:
    pass
    ...
