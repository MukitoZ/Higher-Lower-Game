# import art and game_data and random
from art import logo, vs
from game_data import data
from replit import clear
import random

comparison = []
for _ in range(2):
    comparison.append(random.choice(data))
    
    
def got_you(ab, key):
    """Function to search with array number and key needed in comparison"""
    for x in comparison:
        for y in x:
            if y == key:
                return comparison[ab][y]


def right_wrong(follower_count, is_continue, guess):
    """"Function for checking the answer is it right or wrong"""
    compare_a = follower_count[0]
    compare_b = follower_count[1]

    if compare_a > compare_b and guess == "a":
        is_continue = True
        return is_continue
    elif compare_a < compare_b and guess == "b":
        is_continue = True
        return is_continue
    else:
        is_continue = False
        return is_continue

        
def add_remove_comparison(comparison):
    """Function to add a data to comparison"""
    del comparison[0]
    comparison.append(random.choice(data))
    while comparison[0] == comparison[1]:
        del comparison[1]
        comparison.append(random.choice(data))


def play_game():
    is_game = True
    your_score = 0
    is_continue = False
    print(logo)
    while is_game:
        name = got_you(0,"name")
        follower_count = [got_you(0, "follower_count")]
        description = got_you(0, "description")
        country = got_you(0, "country")


        print(f"Compare A: {name}, {description}, from {country}")

        print(vs)

        name = got_you(1,"name")
        follower_count += [got_you(1, "follower_count")]
        description = got_you(1, "description")
        country = got_you(1, "country")
        print(f"Againts B: {name}, {description}, from {country}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_continue = right_wrong(follower_count, is_continue, guess)

        if is_continue:
            your_score += 1
            add_remove_comparison(comparison)
            clear()
            print(logo)
            print(f"You're right! Current score: {your_score}")
        else:
            is_game = False
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {your_score}")
            
play_game()        

