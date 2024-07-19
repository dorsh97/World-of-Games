import random
import requests
from currency_converter import CurrencyConverter
from Utilities.utils import check_user_input_num


def get_money_interval(game_diff):
    api_app_id = '0143356b50534276a2e4de9adef60d8c'
    url = f'https://openexchangerates.org/api/latest.json?app_id={api_app_id}&symbols=ILS'
    response = requests.get(url)
    interval = 10 - game_diff
    if response.status_code == 200:
        convert = response.json()
        usd_in_ils = convert['rates']['ILS']
        return usd_in_ils, interval
    else:
        print("Failed to connect to live rates, will use offline cache.")
        x = CurrencyConverter()
        return (x.convert(1, 'USD', 'ILS')), interval


def get_guess_from_user():
    usd_rand = random.randint(1, 100)
    return check_user_input_num(input(f"Please guess the value of {usd_rand} USD in ILS: ")), usd_rand


def compare_results(ils_calc, user_guess, interval):
    return user_guess - ils_calc <= interval and ils_calc - user_guess <= interval


def play(game_diff):
    usd_to_ils, interval = get_money_interval(game_diff)
    user_guess, usd_rand = get_guess_from_user()
    return compare_results(usd_to_ils * usd_rand, user_guess, interval)

