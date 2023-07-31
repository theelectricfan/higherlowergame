import os
import random
import art
from game_data import data


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def compare_parameters(comp_a, comp_b):
    print(f"Compare A:")
    print(f"Name: {comp_a['name']}")
    print(f"Description: {comp_a['description']}")
    print(f"Country: {comp_a['country']}")
    print(art.vs)
    print(f"Against B:")
    print(f"Name: {comp_b['name']}")
    print(f"Description: {comp_b['description']}")
    print(f"Country: {comp_b['country']}")
    ans = ''
    while ans != 'a' and ans != 'b':
        ans = input("Who has more followers, Type 'a' or 'b': ").lower()
        if ans != 'a' and ans != 'b':
            print("Invalid input! Try again.")

    if (ans == 'a' and comp_a['follower_count'] >= comp_b['follower_count']) or (
            ans == 'b' and comp_b['follower_count'] >= comp_a['follower_count']):
        return 1
    else:
        return 0


def game():
    comp_a = {}
    comp_b = {}
    while comp_a == comp_b:
        comp_a = random.choice(data)
        comp_b = random.choice(data)

    result = 1
    score = 0

    clear_screen()
    print(art.logo)
    while result != 0:
        result = compare_parameters(comp_a, comp_b)
        if result == 1:
            clear_screen()
            print(art.logo)
            score += 1
            print(f"You're right! Current score = {score}")
            comp_a = comp_b
            comp_b = random.choice(data)
    clear_screen()
    print(art.logo)
    print(f"You're wrong! Final score = {score}")


play = 'y'
while play == 'y':
    game()
    play = ''
    while play != 'y' and play != 'n':
        play = input("Would you like to play another game. Type 'y' or 'n': ").lower()
        if play != 'y' and play != 'n':
            print("Invalid input! Try again.")
