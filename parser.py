import json
import time
from os import getenv

from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver

import config

load_dotenv()

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get(config.main_url)

s_search = driver.find_element(By.XPATH, config.login_str)
s_search.clear()
s_search.send_keys(getenv('login'))

s_search = driver.find_element(By.XPATH, config.password_str)
s_search.clear()
s_search.send_keys(getenv('password'))

s_search.send_keys(Keys.ENTER)
time.sleep(1)

post_requests = [request for request in driver.requests if request.method == 'POST']

if post_requests:
    last_post_request = post_requests[-1]
    post_data = last_post_request.body.decode('utf-8')  # Раскодируйте данные POST-запроса, если это текст
    json_object = json.loads(post_data)

    for i in range(len(config.days_of_week)):
        # TODO поменять на список
        print(config.days_of_week[i])
        for j in range(config.max_lessons):
            try:
                prep = json_object['serverMemo']['data']['events'][f'{j}_{i}'][0]['teachers']
                para = json_object['serverMemo']['data']['events'][f'{j}_{i}'][0]
                print(
                    f"{j + 1}:{para['startTime']}-{para['endTime']}"
                    f" {para['discipline']}({para['groupType']}): {para['classroom']}"
                    f" - {prep[list(prep.keys())[0]]['last_name']}"
                    f" {prep[list(prep.keys())[0]]['first_name']}"
                    f" {prep[list(prep.keys())[0]]['middle_name']}")
            except:
                print(f'{j + 1}:')

    # with open('class.json', 'w', encoding='utf-8') as f:
    #     json.dump(json_object, f, indent=2)

else:
    print('POST-запросы не были обнаружены.')
