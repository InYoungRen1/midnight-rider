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
 
 WE'VE STOLEN A RELIC. WE NEED TO GET IT HOME.
 THE RELIC IS SPECIAL.
 
 THE CORP WANTS IT FOR THEIR GAIN.
 
 WE CAN'T LET THAT HAPPEN.
 
 ONE GOAL: SURVIVAL... and THE RELIC.
 REACH THE END BEFORE THE AGENTS GET YOU.
 
 
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
You know you did the right thing, the corp 
would have just torn the relic apart.
They don't know its secrets....
that is holds the key to different worlds.
As you step out of the vehicle, Johnny SilverHand runs up to you
"Thank you for saving me," he says.
it makes a strange sound.
It changed its form.
You've seen it before, but only on TV.
"...Geralt???"
"Ruin has come to our family...."


------ Game Over ------
"""

LOSE_HUNGER = """

YOUR STOMACH IS EMPTY 
WHO KNEW THAT WHAT THE DOCTOR SAID WAS TRUE,
THAT HUMAN/ROBOT HYBRIDS WOULD NEED 
DUMPLING TO SUSTAIN THEMSELVES. 
YOUR ROBOT SYSTEM START TO SHUT DOWN.
YOUR HUMAN EYES CLOSE.
THE LAST THING THAT YOU HEAR ARE SIRENS.
THEY GOT YOU. THEY GOT THE RELIC.
WE FAILED....

------ GAME OVER ------
"""

LOSE_AGENTS = """

THE AGENTS HAVE CLOSED IN ON YOU.
THERE ARE AT LEAST 20 CARS SURROUNDING YOU.
THE LEAD CAR BUMPS YOUR PASSENGER SIDE. 
YOU MANAGE TO CORRECT YOUR STEERING
TO KEEP YOU FROM CRASHING.

YOU DIDN'T SEE THE AGENTS CAR BESIDE YOU. 
THE DRIVER BUMPS YOUR CAR. 
AND THAT'S IT.

YOU SPIN OUT OF CONTROL.
THE CAR FLIPS OVER AT LEAST TWO TIME.
OR MORE... YOU LOST COUNT.

SIREN.

"ARE THEY ALIVE?" SOMEONE ASKS.
"DOESN'T MATTER. ALL WE WANTED WAS THE CAR."
YOU SEE A BLUE EYE MAN WALKING OUR OF THE CAR.
"WAS IT IN THE CAR THE WHOLE TIME?" YOU 
THINK TO YOURSELF.

THE BLUE EYE MAN LOOKS UP AT TEH OFFICERS.
"YOU WILL NEVER THE REVOLUTION."
"DID THE BLUE EYES JUST TALK?" YOU THINK TO YOURSELF.

YOUR DRIFT OFF INTO UNCONSCIOUSNESS.

------ GAME OVER ------
"""

LOSE_FUEL = """

THE CAR RUNS OUT OF FUEL,
THE AGENTS ARE CATCHING UP 
YOU KNEW YOU HAVE TO DO SOMETHING 
YOU DECIDED TO DRIVE INTO THE FOREST 
TO BET ON THE AGENTS COULDN'T FIND YOU
AS YOU MAKE THE TURNS AND SPED UP
YOU DIDN'T SEE A TREE BRANCH IN THE WAY
THE TREE BRANCH PIERCE THROUGH THE WINDSHIELD
AND STAB RIGHT INTO YOUR EYES AND HEAD
CAME OUT FROM THE HEAD
YOU DIDN'T EVEN HAVE TIME TO THINK

YOU DIED

------ GAME OVER ------
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
    DUMPLING_CHANCE = 0.03

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
        if random.random() < DUMPLING_CHANCE:
            # Fido pops up says something and gives you one dumpling
            dumplings += 1
            print()
            print("********* You magically gained one dumpling!")
            print("******** \"You're welcome!\" a voice says.")
            print("********* It's Your Ancestor.")
            print("********* He's using his dumpling frying skills to cook you a dumpling.")

        #  checked if reached END GAME
        if km_traveled > MAX_DISTANCE_TRAVELLED:
            # Win
            # print win scenario
            time.sleep(2)
            type_text_output(WIN)
            break
        elif hunger > 45:
            # LOSE - TOO Hungry
            time.sleep(2)
            type_text_output(LOSE_HUNGER)
            break
        elif agents_distance >= 0:
            time.sleep(2)
            type_text_output(LOSE_AGENTS)
            break
        elif fuel <= 0:
            time.sleep(2)
            type_text_output(LOSE_FUEL)
            break
        if hunger > 35:
                print("********* Gnawing hunger sets in, turning the body against itself, weakening the mind…")
        elif hunger > 20:
                print("********* No force of will can overcome a failing body.")
        # give player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.?")
        if users_choice == "a","b","c","d","e":
            turns += 1

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
    print(f"You finished the game in {turns} turns.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
