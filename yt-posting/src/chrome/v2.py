import random, os, string

import undetected_chromedriver.v2 as uc
from selenium import webdriver

class Chrome():
    CHROMEDRIVER = None
    chrome_num = random.randint(1000, 9999)
    user_dir = None

    def __init__(self):
        pass
    
    def webdriver(self, i=None, proxy=False, headless=False, proxy_address=None, browser_profile=None):
        options = self.options(i=i, proxy=proxy, headless=headless, proxy_address=proxy_address, browser_profile=browser_profile)
        return uc.Chrome(executable_path=self.CHROMEDRIVER, options=options)

    def close(self, driver):
        driver.quit()

    def options(self, i=None, proxy=False, headless=False, proxy_address=None, browser_profile=None):
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        if proxy!=False and i!=None:
            chrome_options.add_extension(f"{os.path.abspath('')}/data/extension/proxy_auth_plugin_{i}.crx")
            # chrome_options.add_argument(f'--load-extension=data/extension/proxy_auth_plugin_{i}.crx')
        if proxy_address is not None:
            chrome_options.add_argument("--proxy-server="+proxy_address)
        if browser_profile is not None:
            os.makedirs(f"{os.path.abspath('')}/data/browser-profiles") if not os.path.exists(f"{os.path.abspath('')}/data/browser-profiles") else False
            # user_data_dir = user_data_dir = f'data/browser-profiles/{random.randint(1000, 9999)}-{"".join(random.choice(string.ascii_letters) for i in range(8))}'
            user_data_dir = f'{os.path.abspath("")}/data/browser-profiles/{browser_profile}'
            os.makedirs(user_data_dir) if not os.path.exists(user_data_dir) else False
            self.user_dir = user_data_dir
            chrome_options.add_argument("--user-data-dir=%s" % user_data_dir)
        chrome_options.add_argument('--mute-audio')
        # prefs = {"profile.default_content_setting_values.notifications" : 2}
        # chrome_options.add_experimental_option("prefs",prefs)
        return chrome_options