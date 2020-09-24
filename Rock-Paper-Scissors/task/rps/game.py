import random

# Write your code here


def calculate_result(gesture_1, gesture_2, gesture_list):
    if gesture_1 == gesture_2:
        return "Draw"
    else:
        index_gesture_1 = gesture_list.index(gesture_1)
        first_list = gesture_list[:index_gesture_1]
        second_list = gesture_list[index_gesture_1 + 1:]
        new_list = second_list + first_list
        index_gesture_2 = new_list.index(gesture_2)
        if index_gesture_2 >= len(new_list) / 2:
            return "Win"
        else:
            return "Loss"


# Open file
rating_file = open("rating.txt", mode="r")
rating_lines = rating_file.readlines()
ratings = {x: y for x, y in [line.split() for line in rating_lines]}
# print(ratings["Tim"])
rating_file.close()

name = input("Enter your name:")
print("Hello, {}".format(name))
score = 0
if name in ratings.keys():
    score = int(ratings[name])

symbols = input("Please specify the used symbols: ").split(",")
if symbols == ['']:
    symbols = ["rock", "paper", "scissors"]
print("Okay, let's start")

gesture = input()
while gesture != "!exit":
    if gesture == "!rating":
        print("Your rating: {}".format(score))
    else:
        computer_choice = random.choice(["rock", "paper", "scissors"])
        if gesture not in symbols:
            print("Invalid input")
        else:
            status = calculate_result(gesture, computer_choice, symbols)
            if status == "Win":
                print("Well done. The computer chose {} and failed".format(computer_choice))
                score += 100
            elif status == "Draw":
                print("There is a draw ({})".format(computer_choice))
                score += 50
            elif status == "Loss":
                print("Sorry, but the computer chose {}".format(computer_choice))
            else:
                print("WTF?")

    gesture = input()
print("Bye!")
