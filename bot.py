from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()


    def login(self):
        bot = self.bot
        bot.get("https://instagram.com")
        time.sleep(10)
        bot.find_element_by_xpath("//input[@name=\"username\"]") \
        .send_keys(self.username)
        bot.find_element_by_xpath("//input[@name=\"password\"]") \
        .send_keys(self.password)
        bot.find_element_by_xpath('//button[@type="submit"]') \
        .click()
        time.sleep(10)


    def search(self , url):
        bot = self.bot
        bot.get(url)
        time.sleep(10)

    def fllikecm(self , comm):
        bot = self.bot
        bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]").click()
        time.sleep(5)
        try:
        
            if bot.find_element_by_xpath('//button[text()="Cancel"]').is_displayed():
                time.sleep(10)
                element = bot.find_element_by_xpath('//button[text()="Cancel"]')
                bot.execute_script("arguments[0].click();", element)
                
                time.sleep(2)
                bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div").click()
                time.sleep(2)
                bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button/div") .click()
                time.sleep(5)
                bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(comm + Keys.ENTER)
                time.sleep(2)
        except:
            bot.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div").click()
            time.sleep(2)
            bot.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button/div").click()
            time.sleep(5)
            bot.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(comm + Keys.ENTER)
            time.sleep(2)


      

urls =["post_url"]

usernames = ["user_name"]

cmm = ["your comment"]




for i in range(0,10):
    insta = InstagramBot(usernames[i] , "your password")
    insta.login()
    for p in range(0,1):
        insta.search(urls[p])
        insta.fllikecm(cmm[i])
