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
    E. Status check
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
    # intro()


# Variables
    done = False
    km_traveled = 0             # 100km traveled is the goal
    agents_distance = -20.0
    turns = 0                   # amount of turns taken
    dumplings = 0                # 3 is max dumping
    fuel = 50                   # 50 is a full tank
    hunger = 0                  # hunger increases with number

    while not done:

        # TODO: checked if reached END GAME

        # give player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.?")

        if users_choice == "e":
            print(f"\t---Status check---")
            print(f"\tkm traveled: {km_traveled}")
            print(f"\tFuel left: {fuel} litre")
            print(f"\tAgents are {abs(agents_distance)} km behind you")
            print(f"\tYou have: {dumplings} dumplings left")
            print("\t------\n")
        elif users_choice == "q":
            done = True

        # Pause
        time.sleep(1)

        # TODO:change the environment based on the choice and random number generator


    # outroduction
    print("Thanks for playing! Please play it again!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
