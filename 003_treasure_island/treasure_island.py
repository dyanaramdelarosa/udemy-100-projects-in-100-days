"""
Day 3 Project (Control Flow): Treasure Island

This project uses control flow to navigate a world wherein the user's
goal is to find the treasure.

Although there are possible code improvements for this code,
it was kept simple in order to showcase if else statements.
"""


def retry_input(expected_answers: list[str], answer: str) -> str:
    while True:
        if answer not in expected_answers:
            answer = input("\033[A\033[K").lower()
        else:
            break
    return answer


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

prompt = '''
You're at a cross road. Where do you want to go?
    Type "left" or "right"
'''
answer = input(prompt).lower()
expected_answers = ["left", "right"]
answer = retry_input(expected_answers, answer)

if answer == "right":
    print("You fell into a hole. Game over.")
    exit()

prompt = '''
You've come to a lake. There is an island in the middle of the lake.
    Type "wait" to wait for a boat. Type "swim" to swim across.
'''
answer = input(prompt).lower()
expected_answers = ["wait", "swim"]
answer = retry_input(expected_answers, answer)

if answer == "swim":
    print("You get attacked by an angry trout. Game over.")
    exit()

answer = input('''
You arrive at the island unharmed. There is a house with 3 doors.
    One red, one yellow and one blue. Which colour do you choose?
''').lower()
expected_answers = ["red", "blue", "yellow"]
answer = retry_input(expected_answers, answer)

if answer == "red":
    print("It's a room full of fire. Game over.")
elif answer == "blue":
    print("You get attacked by an angry trout. Game over.")
else:
    print("You found the treasure! You Win!")
