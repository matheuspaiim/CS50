# :) plates.py exists
# :( input of CS50 yields output of Valid
    # expected "Valid", not "Invalid\n"
# :( input of ECTO88 yields output of Valid
    # expected "Valid", not "Invalid\n"
# :( input of NRVOUS yields output of Valid
    # expected "Valid", not "Invalid\n"
# :) input of CS05 yields output of Invalid
# :) input of CS50P2 yields output of Invalid
# :) input of PI3.14 yields output of Invalid
# :) input of H yields output of Invalid
# :) input of OUTATIME yields output of Invalid

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


if __name__ == "__main__":
    main()

