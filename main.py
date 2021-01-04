# main.py
# Midnight Rider
# A text adventure game that is riveting
# IGN gives 4 stars out of 100

import sys
import textwrap
import time

INTRODUCTION = """
 
 WELCOME TO MIDNIGHT RIDER
 
 WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
 THE CAR IS SPECIAL.
 
 THE GOVERNMENT WANTS IT FOR THEIR GAIN.
 
 WE CAN'T LET THAT HAPPEN.
 
 ONE GOAL: SURVIVAL... and THE CAR.
 REACH THE END BEFORE THE MAN GON GETCHU
 
 
 """

CHOICES = """
    ----
    Q. QUIT
    ----
"""

def intro():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)

def main():
    intro()

    done = False

    while not done:
        pass
    # TODO: checked if reached END GAME

    # give player their choices
    print(CHOICES)

    # Handle user's input
    users_choice = input("What do you want to do? ").lower().strip("!,.?")
    if users_choice == "q":
        done = True

    # TODO:change the environment based on the choice and random number generator


# outroduction
print("Thanks for playing! Please play it again!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
