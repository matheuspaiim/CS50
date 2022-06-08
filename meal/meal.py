# :) meal.py exists
# :( input of 7:00 yields output of "breakfast time"
    # expected "breakfast time...", not ""
# :( input of 7:30 yields output of "breakfast time"
    # expected "breakfast time...", not ""
# :( input of 13:00 yields output of "lunch time"
    # expected "lunch time", not ""
# :( input of 18:32 yields output of "dinner time"
    # expected "dinner time", not ""
# :) input of 11:11 yields no output

def main():
    time = input("")
    hours, minutes = time.split(":")



def convert(time):
    ...


if __name__ == "__main__":
    main()