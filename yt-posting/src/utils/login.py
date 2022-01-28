from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as k
import time

def Login(driver, username, password):
    driver.get("https://accounts.google.com/signin/v2/identifier"); time.sleep(7)
    try:
        usrname = driver.find_element(by.XPATH, "//input[@name='identifier']")
        usrname.click(); usrname.send_keys(username); time.sleep(1.5)
        # driver.find_element(by.XPATH, "//span[contains(text(), 'Next')]").click(); time.sleep(5.5)
        usrname.send_keys(k.RETURN); time.sleep(5.5)
        passwrd = driver.find_element(by.XPATH, "//input[@name='password']")
        passwrd.click(); passwrd.send_keys(password); time.sleep(1.5)
        passwrd.send_keys(k.RETURN); time.sleep(5.5)
        # driver.get("https://www.youtube.com/"); time.sleep(5.5)
    except Exception as e:
        # print(e)
        pass