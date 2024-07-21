from Games.currency_roulette_game import play as currency_roulette_game_play
from Games.guess_game import play as guess_game_play
from Games.memory_game import play as memory_game_play
from Utilities.utils import check_range_int
from Utilities.score import add_score
from Utilities.utils import username


def welcome():
    global username
    if username == 'blank':
        username = input("Please choose a username: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey.")


def start_play():
    while True:
        gamenames = {1: "Memory Game", 2: "Guess Game", 3: "Currency Roullete"}
        game_num = check_range_int(input("Please choose a game to play by typing the corresponding number:\n"
                                     "1. Memory Game - a sequence of numbers will appear for 1 second and you have to "
                                     "guess it back.\n"
                                     "2. Guess Game - guess a number and see if you chose like the computer.\n"
                                     "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n"),
                               1, 3)
        game_diff = check_range_int(input(f"You have selected {gamenames[game_num]}, "
                                      f"please select a difficulty from 1-5: "), 1, 5)
        print(f"You have selected difficulty '{game_diff}'")
        if game_num == 1:
            result = memory_game_play(game_diff)
        elif game_num == 2:
            result = guess_game_play(game_diff)
        elif game_num == 3:
            result = currency_roulette_game_play(game_diff)
        if result:
            add_score(game_diff)
            print("Congratulations! You won!")
        else:
            print("You failed. Better luck next time!")
        play_again = input("Would you like to play again? (Yes/No): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

