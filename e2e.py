from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver_manager
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.common.by import By

chrome_options = ChromiumOptions()
service = Service(ChromeDriverManager().install(), options=chrome_options)

driver = webdriver.Chrome(service=service)


def test_scores_service(scores_url):
    driver.get(scores_url)
    score = int(driver.find_element(By.XPATH, '/html/body/div').text)
    if 1 <= score <= 1000:
        return True
    else:
        return False


def main_function(scores_url):
    if test_scores_service(scores_url):
        return 0
    else:
        return -1
