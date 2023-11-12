from art import logo,vs
from data import gamedata
import random as rd
import os

def compare(a, b):
    return 'a' if a > b else 'b'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

a_competetor = rd.choice(gamedata)
score = 0
game_over = False

while not game_over:
    b_competetor = rd.choice(gamedata)

    while b_competetor == a_competetor:
        b_competetor = rd.choice(gamedata)
    
    print(f"Compare A: {a_competetor['name']}, a {a_competetor['description']}, from {a_competetor['country']}")
    print(vs)
    print(f"Against B: {b_competetor['name']}, a {b_competetor['description']}, from {b_competetor['country']}")
    winner = compare(a_competetor['follower_count'], b_competetor['follower_count'])
    answer = input("Who Has More followers? Type A or B: ").lower()
    
    clear_screen()
    print(logo)

    if answer == winner:
        a_competetor = b_competetor
        score += 1
        game_over = False
        print(f"Correct Answer >> Your Current Score is : {score}")
    else:
        print(f"Wrong Answer >> Your Final Score is: {score}")
        game_over = True