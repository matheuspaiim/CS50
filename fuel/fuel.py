# :) fuel.py exists
# :) input of 3/4 yields output of 75%
# :) input of 1/3 yields output of 33%
# :) input of 2/3 yields output of 67%
# :) input of 0/100 yields output of E
# :) input of 1/100 yields output of E
# :) input of 100/100 yields output of F
# :) input of 99/100 yields output of F
# :) input of 100/0 results in reprompt
# :) input of 10/3 results in reprompt
# :) input of three/four results in reprompt
# :) input of 1.5/4 results in reprompt
# :) input of 3/5.5 results in reprompt
# :) input of 5-10 results in reprompt

while True:
    fuel = input('Fraction: ')

    try:
        x, y = fuel.split("/")
        percent_fuel = int(x) / int(y)

        if percent_fuel <= 1:
            break

    except ValueError:
        pass
    except ZeroDivisionError:
        pass

percent = percent_fuel * 100

if percent >= 99:
    print('F')
elif percent <= 1:
    print('E')
else:
    print(f'{round(percent)}%')