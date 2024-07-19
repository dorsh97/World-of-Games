import random
from Utilities.utils import check_range_int


def generate_number(game_diff):
    return random.randint(0, game_diff)


def get_guess_from_user(game_diff):
    return check_range_int(input(f"Please guess a number between 0 and {game_diff}: "), 0, game_diff)


def compare_results(secret_number, user_guess):
    return secret_number == user_guess


def play(game_diff):
    secret_number = generate_number(game_diff)
    user_guess = get_guess_from_user(game_diff)
    return compare_results(secret_number, user_guess)

