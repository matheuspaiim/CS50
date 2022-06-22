# :) plates.py exists
# :) input of CS50 yields output of Valid
# :) input of ECTO88 yields output of Valid
# :) input of NRVOUS yields output of Valid
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
        ...


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    for c in s:
        if c in [".", " ", "!", "?"]:
            return False

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    return True


if __name__ == "__main__":
    main()



