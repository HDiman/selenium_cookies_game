from datetime import datetime
from threading import Timer
import time

# def on_10th_second():
#     print('yo-ho-ho', datetime.now())
#
#
# def shedule(func, nth_sec):
#     now_sec = datetime.now().second
#     wait = (60 + nth_sec - now_sec) % 60
#
#     Timer(wait, func).start()
#     Timer(wait + 1, lambda: shedule(func, nth_sec)).start()

# shedule(on_10th_second, 10)

def hello():
    now_sec = datetime.now().second
    print(f"{now_sec}: hello, world")

t = Timer(5.0, hello)
t.start()



# print('ok') # В отличие от sleep, синхронный код ниже Timer() продолжает выполняться.


# Working code --------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
from datetime import datetime
from threading import Timer
import time


chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=url)

# store_list = ["Cursor", "Grandma", "Factory", "Mine", "Shipment", "Alchemy lab", "Portal", "Time machine"]

game_on = True
while game_on:
    t_end = time.time() + 30
    check_time = datetime.now()
    print(f"1: {check_time}")
    while time.time() < t_end:
        cookie = driver.find_element(By.ID, "cookie")
        cookie.click()
    check_time = datetime.now()
    print(f"2: {check_time}")
    print("waiting 10 sec ...")
    time.sleep(10)
    check_time = datetime.now()
    print(f"3: {check_time}")


