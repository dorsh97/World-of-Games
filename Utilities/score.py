import os
from Utilities.utils import SCORES_FILE_NAME


def add_score(game_diff):
    game_score = (game_diff * 3) + 5
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as file:
            file_score = file.read()
        if file_score.isdigit():
            file_score = int(file_score)
        else:
            file_score = 0
        game_score = game_score + file_score
    with open(SCORES_FILE_NAME, 'w+') as file:
        file.write(str(game_score))

