# :) meal.py exists
# :) input of 7:00 yields output of "breakfast time"
# :) input of 7:30 yields output of "breakfast time"
# :) input of 13:00 yields output of "lunch time"
# :) input of 18:32 yields output of "dinner time"
# :) input of 11:11 yields no output

def main():
    global time
    time = input("What time is it? ")
    convert(time)
...

def convert(time):
    hours, minutes = time.split(":")
    h = int(hours)
    m = int(minutes)

    if (7 <= h <= 8) and (m <= 59):
        print("breakfast time")
    elif (12 <= h <= 13) and (m <= 59):
        print("lunch time")
    elif (18 <= h <= 19) and (m <= 59):
        print("dinner time")
        ...

if __name__ == "__main__":
    main()