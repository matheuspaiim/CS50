def main():
    dollars = dollars_to_float(input("How much was the meal? ").strip('$'))
    percent = percent_to_float(input("What percentage would you like to tip? ").strip('%'))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollars):
    dollars
    return float()

def percent_to_float(percent):
    return float(percent)

main()