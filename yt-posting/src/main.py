from selenium.webdriver.common.by import By as by
import time, os

from .utils.login import Login
from .chrome.v2 import Chrome
# from .chrome._compat import Chrome
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, HardwareType

def random_user_agent():
	return UserAgent(software_names=[SoftwareName.CHROME.value], hardware_types={HardwareType.COMPUTER.value}, limit=100).get_random_user_agent()
chrome = Chrome()

def close(driver):
    chrome.close_driver(driver)

def __init__(proxy_address=None, browser_profile=None):
    return chrome.webdriver(proxy_address=proxy_address, headless=False, browser_profile=browser_profile)

def start(description, path, username=None, password=None):
    driver = __init__(browser_profile=username)
    # driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": f"{random_user_agent()}"})
    # if not os.path.exists(f"data/browser-profiles/{username}"):
    #     print("login")
    try:
        Login(driver, username, password)
    except:
        pass
    driver.get("https://studio.youtube.com"); time.sleep(10)
    driver.find_element(by.XPATH, "//ytcp-icon-button[@id='upload-icon']").click(); time.sleep(5.5)
    # upload = driver.find_element(by.XPATH, '//ytcp-button[@id="select-files-button"]')
    for inpt in driver.find_elements(by.TAG_NAME, "input"):
        if inpt.get_attribute("type") == "file":
            upload = inpt
            break
    upload.send_keys(os.path.abspath(path))
    time.sleep(15)
    title = driver.find_elements(by.XPATH, "//*[@id='textbox']")[0]
    try: title.clear(); title.click(); title.send_keys(f"{description} #shorts #ytshorts #fyp #FYP"); time.sleep(1.5)
    except: title.clear(); title.click(); title.send_keys("#shorts #ytshorts #fyp #FYP"); time.sleep(1.5)
    #   Children videos
    # driver.find_element(by.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]/div[1]").click(); time.sleep(1.5)
    desc = driver.find_elements(by.XPATH, '//*[@id="textbox"]')[1]
    desc.click(); desc.send_keys("#shorts #shortvideo #ytshorts #yt-shorts"); time.sleep(1.5)
    driver.find_element(by.XPATH, "//ytcp-button[@id='next-button']").click(); time.sleep(2.5)
    driver.find_element(by.XPATH, "//ytcp-button[@id='next-button']").click(); time.sleep(2.5)
    driver.find_element(by.XPATH, "//ytcp-button[@id='next-button']").click(); time.sleep(2.5)
    driver.find_element(by.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]').click(); time.sleep(2.5)
    driver.find_element(by.XPATH, '//ytcp-button[@id="done-button"]').click(); time.sleep(2.5)
    time.sleep(15)
    driver.quit()