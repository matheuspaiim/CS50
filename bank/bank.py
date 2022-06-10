# :) bank.py exists
# :) input of "Hello" yields output of $0
# :) input of " Hello " yields output of $0
# :) input of "Hello, Newman" yields output of $0
# :) input of "How you doing?" yields output of $20
# :) input of "What's happening?" yields output of $100
# :) input of "What's up?" yields output of $100

answer = input(" ")

if answer == "How you doing?":
    print("$20")
elif answer == "What's happening?":
    print("$100")
elif answer == "What's up?":
    print("$100")
else:
    print("$0")