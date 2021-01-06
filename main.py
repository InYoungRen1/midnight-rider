# main.py
# Midnight Rider
# A text adventure game that is riveting
# IGN gives 4 stars out of 100

import random
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
    A. Eat a dumpling
    B. Move at a constant speed 
    C. Maximum Velocity
    D. Stop for fuel at a refueling station(no food available)
    E. Status check
    Q. QUIT
    ----
"""

WIN = """

you pressed the button to open the gate.
This isn't the first time you've done this,
so you know how to time it exactly.
Just as the door close, you slide right into the HQ
You know you did the right thing, the government 
would have just torn the car apart.
They don't know its secrets....
that is holds the key to different worlds.
As you step out of the vehicle, Fido runs up to you
"Thank you for saving me," he says.
it makes a strange sound.
It changed its form.
You've seen it before, but only on TV.
"...Bumblebee???"
"Ruin has come to our family...."


------ Game Over ------
"""



def type_text_output(text):
    for char in textwrap.dedent(text):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1.5)

def main():
    type_text_output(INTRODUCTION)

    # Constants
    MAX_FUEL_LEV = 50
    MAX_DUMPLING = 3
    MAX_DISTANCE_TRAVELLED = 100

    # Debuff from hunger
    # if hunger == 45:

# Variables
    done = False

    km_traveled = 0             # 100km traveled is the goal
    agents_distance = -20.0
    turns = 0                   # amount of turns taken
    dumplings = MAX_DUMPLING                # 3 is max dumping
    fuel = MAX_FUEL_LEV                   # 50 is a full tank
    hunger = 0                  # hunger increases with number

    while not done:

        # Fido
        if random.random() < 0.03:
            # Fido pops up says something and gives you one dumpling
            dumplings = MAX_DUMPLING
            print()
            print("********* You magically gained one dumpling!")
            print("******** \"You're welcome!\" a voice says.")
            print("********* It's Fido.")
            print("********* He's using his dumpling frying skills to cook you a dumpling.")
        if hunger > 35:
            print("********* Gnawing hunger sets in, turning the body against itself, weakening the mind…")
        elif hunger > 20:
            print("********* No force of will can overcome a failing body.")
        #  checked if reached END GAME
        if km_traveled > MAX_DISTANCE_TRAVELLED:
            # Win
            # print win scenario
            time.sleep(2)
            type_text_output(WIN)

            # Breaking the while loop
            break

        # give player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.?")

        if users_choice == "a":

            # Eat
            if dumplings > 0:
                dumplings -= 1
                hunger = 0
                print()
                print("--------- Mmmmmmm. Delicious.")
                print("--------- You ate a dumpling, your are starting feel better; but is it just a sense of illusion?")
                print()
            else:
                print()
                print("--------- You have no more dumplings left.")
                print()

            # Agents distance travelled
            agents_distance_now = (7, 15)
            agents_distance -= (player_distance_now - agents_distance_now)

        elif users_choice == "b":
            # Drive
            player_distance_now = random.randrange(5, 12)
            agents_distance_now = (7, 15)

            # use fuel
            fuel -= random.randrange(3, 10)

            # distance travelled
            agents_distance -= (player_distance_now - agents_distance_now)

            # feedback
            print()
            print(f"--------- You drove {player_distance_now} km. Agents are catching up")
            print()

        elif users_choice == "c":
            # Drive fast
            player_distance_now = random.randrange(9, 17)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(5, 15)

            # player distance traveled
            km_traveled += player_distance_now

            # agents distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)

            # feed back
            print()
            print(f"--------- You sped ahead {player_distance_now} km!")
            print()

        elif users_choice == "d":
            # refuel
            # Fill the fuel tank
            fuel = MAX_FUEL_LEV

            #Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give the user feed back
            print("--------- You filled the fuel tank.")
            print("--------- The agents are coming closer...")

        elif users_choice == "e":
            print(f"\t---Status check---")
            print(f"\tkm traveled: {km_traveled}")
            print(f"\tFuel left: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} km behind you")
            print(f"\tYou have: {dumplings} dumplings left")
            print("\t------\n")

        elif users_choice == "q":
            done = True

        # Increase hunger
        if users_choice not in ["a", "e"]:
            hunger += random.randrange(5, 13)

        # Pause
        time.sleep(1.5)


    # outroduction
    print("Thanks for playing! Please play it again!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
