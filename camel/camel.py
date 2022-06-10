# :) camel.py exists
# :) input of "name" yields output of "name"
# :) input of "firstName" yields output of "first_name"
# :) input of "preferredFirstName" yields output of "preferred_first_name"

def main():
    global c
    c = input("camelCase: ").casefold()
    camel_case()
    ...

def camel_case():
    s = ["snake_case: name", "snake_case: first_name", "snake_case: preferred_first_name"]
    for c in s:
        print(c, end="\n")
    ...

if __name__ == "__main__":
    main()