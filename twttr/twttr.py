# :) twttr.py exists
# :) input of Twitter yields output of Twttr
# :) input of "What's your name?" yields output of "Wht's yr nm?"
# :) input of CS50 yields output of CS50
# :) input of PYTHON yields output of PYTHN

def main():
    tweet = input("Input: ")
    twitter(tweet)
    print("")
    ...


def twitter(tweet):
    for cons in tweet:
        print(cons.strip("aeiouAEIOU"), end="")
    ...

if __name__ == "__main__":
    main()