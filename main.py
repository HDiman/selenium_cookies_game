from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=url)

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
store_list = [item.get_attribute("id") for item in items]
store_list.reverse()

cookie = driver.find_element(By.ID, "cookie")

t = 0
game_on = True
while game_on:
    t += 1
    t_end = time.time() + 10 * t

    while time.time() < t_end:
        cookie.click()

    money = (driver.find_element(By.ID, "money")).text

    for i in range(8):
        buy_item = driver.find_element(By.ID, store_list[i])
        print(f"{i}: {store_list[i]}")
        class_atr = buy_item.get_attribute("class")
        print(f"class: {class_atr}")
        if class_atr == "":
            print(f"click: {i}")
            buy_item.click()
            break

    print("next round ...")

driver.close()
driver.quit()
