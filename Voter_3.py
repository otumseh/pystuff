# for John, a looping vote bot base.

from selenium import webdriver
import time


class VoteBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--remote-debugging-port=9222')
        self.driver = webdriver.Chrome("./chromedriver", options=options)
        self.driver.get("https://poll.fm/10615673")
        self.driver.get("https://www.google.com")
        time.sleep(1)
        n = 1
        while n < 2:
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='PDI_answer49174035']").click()
            vote = self.driver.find_element_by_css_selector(".vote-button")
            time.sleep(1)
            vote.click()
            time.sleep(3)
            self.driver.back()
            time.sleep(1)
            # self.driver.deleteAllCookies()
            self.driver.close()
