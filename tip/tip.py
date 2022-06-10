# :) tip.py exists
# :) input of $50.00 and 15% yields $7.50
# :) input of $100.00 and 18% yields $18.00
# :) input of $15.00 and 25% yields $3.75


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    doll = d.strip('$')
    return float(doll)

def percent_to_float(p):
    perc = p.strip('%')
    perc_divide = float(perc) / 100
    return perc_divide

main()