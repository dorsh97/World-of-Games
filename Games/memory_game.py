import random
import time
from Utilities.utils import clear_line

def generate_sequence(game_diff):
    return [random.randint(1, 100) for i in range(game_diff)]


def get_list_from_user(game_diff, rand_list):
    user_list = input("Please type the numbers, separated with a comma: ").split(",")
    while len(rand_list) != len(user_list):
        user_list = input(f"Please type exactly {game_diff} numbers: ").split(",")
    return [int(i) for i in user_list if i.strip().isdigit()]


def is_list_equal(rand_list, user_list):
    return user_list == rand_list


def play(game_diff):
    rand_list = generate_sequence(game_diff)
    time.sleep(0.7)
    print(rand_list, end="", flush=True)
    time.sleep(0.7)
    clear_line(rand_list)
    time.sleep(0.7)
    user_list = get_list_from_user(game_diff, rand_list)
    return is_list_equal(rand_list, user_list)

