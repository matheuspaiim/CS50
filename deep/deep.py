# :) deep.py exists
# :) input of 42 yields output of Yes
# :) input of forty-two yields output of Yes
# :) input of forty two yields output of Yes
# :) input of FoRty TwO yields output of Yes
# :) input of 42, with spaces on either side, yields output of Yes
# :) input of 50 yields output of No
# :) input of fifty yields output of No

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if answer == ("50"):
    print("No")
elif answer == ("fifty"):
    print("No")
else:
    print("Yes")