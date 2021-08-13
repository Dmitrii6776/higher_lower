from data import data
from art import logo, vs
import random
from replit import clear


def give_random_account():
    random_account = random.choice(data)
    return random_account


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}'


def check_the_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'


def play_the_game():
    print(logo)
    score = 0
    account_a = give_random_account()
    account_b = give_random_account()
    game_should_continue = True

    while game_should_continue:
        account_a = account_b
        account_b = give_random_account()
        while account_a == account_b:
            account_b = give_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B':  ")
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check_the_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)

        if is_correct:
            score += 1
            print(f"Ypu`ve right! Current score {score}")
        else:
            game_should_continue = False
            print(f"Sorry that`s wrong. Final score {score}")


play_the_game()


