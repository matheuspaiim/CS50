# :) interpreter.py exists
# :) input of "1 + 1" yields output of 2.0
# :) input of "2 - 3" yields output of -1.0
# :) input of "2 * 2" yields output of 4.0
# :) input of "50 / 5" yields output of 10.0
# :) input of "3 / 2" yields output of 1.5

expression = input(" ")

x, y, z = expression.split(" ")

sum = float(x) + float(z)
mult = float(x) * float(z)
sub = float(x) - float(z)
div = float(x) / float(z)

if y == "+":
    print(sum)
elif y == "-":
    print(sub)
elif y == "*":
    print(mult)
elif y == "/":
    print(div)