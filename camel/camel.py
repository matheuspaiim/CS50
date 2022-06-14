# :) camel.py exists
# :) input of "name" yields output of "name"
# :) input of "firstName" yields output of "first_name"
# :) input of "preferredFirstName" yields output of "preferred_first_name"

def main():
    name = input("camelCase: ").replace('F', '_f')
    camel_case(name)
    ...

def camel_case(name):
    snake = [f"snake_case: {name}"]
    for name in snake:
        print(name.replace('N', '_n'), end="\n")
    ...


if __name__ == "__main__":
    main()