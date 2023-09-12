from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from os import getenv
from dotenv import load_dotenv

import json
import time

load_dotenv()

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://lks.siriusuniversity.ru/schedule/groups')

s_search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/form/div[4]/input')
s_search.clear()
s_search.send_keys(getenv("login"))

s_search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/form/div[5]/input')
s_search.clear()
s_search.send_keys(getenv("password"))

s_search.send_keys(Keys.ENTER)
time.sleep(1)

post_requests = [request for request in driver.requests if request.method == 'POST']

if post_requests:
    # Получите содержимое последнего POST-запроса
    last_post_request = post_requests[-1]
    post_data = last_post_request.body.decode('utf-8')  # Раскодируйте данные POST-запроса, если это текст
    json_object = json.loads(post_data)

    print("Понедельник")
    for j in range(6):
        try:
            prep = json_object["serverMemo"]["data"]["events"][f"{j}_0"][0]["teachers"]
            # print(prep[list(prep.keys())[0]]['last_name'])
            # print(json_object["serverMemo"]["data"]["events"][f"{j}_0"][0])
            para = json_object["serverMemo"]["data"]["events"][f"{j}_0"][0]
            print(f'{j+1}:{para["startTime"]}-{para["endTime"]} {para["discipline"]}({para["groupType"]}): {para["classroom"]} - {prep[list(prep.keys())[0]]["last_name"]}')
        except:
            print(f'{j + 1}:')

    print("Вторник")
    for j in range(6):
        try:
            prep = json_object["serverMemo"]["data"]["events"][f"{j}_1"][0]["teachers"]
            para = json_object["serverMemo"]["data"]["events"][f"{j}_1"][0]
            print(f'{j+1}:{para["startTime"]}-{para["endTime"]} {para["discipline"]}({para["groupType"]}): {para["classroom"]} - {prep[list(prep.keys())[0]]["last_name"]}')
        except:
            print(f'{j + 1}:')

    print("Среда")
    for j in range(6):
        try:
            prep = json_object["serverMemo"]["data"]["events"][f"{j}_2"][0]["teachers"]
            para = json_object["serverMemo"]["data"]["events"][f"{j}_2"][0]
            print(f'{j+1}:{para["startTime"]}-{para["endTime"]} {para["discipline"]}({para["groupType"]}): {para["classroom"]} - {prep[list(prep.keys())[0]]["last_name"]}')
        except:
            print(f'{j + 1}:')

    print("Четверг")
    for j in range(6):
        try:
            prep = json_object["serverMemo"]["data"]["events"][f"{j}_3"][0]["teachers"]
            para = json_object["serverMemo"]["data"]["events"][f"{j}_3"][0]
            print(f'{j+1}:{para["startTime"]}-{para["endTime"]} {para["discipline"]}({para["groupType"]}): {para["classroom"]} - {prep[list(prep.keys())[0]]["last_name"]}')
        except:
            print(f'{j + 1}:')

    print("Пятница")
    for j in range(6):
        try:
            prep = json_object["serverMemo"]["data"]["events"][f"{j}_4"][0]["teachers"]
            para = json_object["serverMemo"]["data"]["events"][f"{j}_4"][0]
            print(f'{j+1}:{para["startTime"]}-{para["endTime"]} {para["discipline"]}({para["groupType"]}): {para["classroom"]} - {prep[list(prep.keys())[0]]["last_name"]}')
        except:
            print(f'{j + 1}:')

    print("Суббота")
    for j in range(6):
        try:
            prep = json_object["serverMemo"]["data"]["events"][f"{j}_5"][0]["teachers"]
            para = json_object["serverMemo"]["data"]["events"][f"{j}_5"][0]
            print(f'{j+1}:{para["startTime"]}-{para["endTime"]} {para["discipline"]}({para["groupType"]}): {para["classroom"]} - {prep[list(prep.keys())[0]]["last_name"]}')
        except:
            print(f'{j + 1}:')
    # for i in range(7):
    #     for j in range(7):
    #         try:
    #             # print(json_object["serverMemo"]["data"]["events"][f"{j}_0"])
    #             print(json_object["serverMemo"]["data"]["events"][f"{j}_{i}"])
    #         except:
    #             ...

    # with open('class.json', 'w', encoding="utf-8") as f:
    #     json.dump(json_object, f, indent=2)

else:
    print("POST-запросы не были обнаружены.")