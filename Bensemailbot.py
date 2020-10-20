# Python script for manipulating the Cloudmail portal for NSG to automate the creation of mailboxes.
import time
import argparse
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
action = ActionChains(driver)
url = 'https://cloudmail.netservicesgroup.com:446'
opts = Options()
#driver.maximize_window()
driver.get(url)
# noinspection PyDeprecation
# opts.set_headless()
#assert opts.headless  # Operating in headless mode
# Get the args from the CLI
def main(user, fname, lname, dname, job, password):
   "Create mailbox using parameters"
if __name__ == '__main__':
   parser = argparse.ArgumentParser(description="This program creates a new mailbox for SSI users on NSG's system")
   parser.add_argument('--user', type=str, help='username')
   parser.add_argument('--fname', type=str, help='first name')
   parser.add_argument('--lname', type=str, help='last name')
   parser.add_argument('--dname', type=str, help='displayname')
   parser.add_argument('--job', type=str, help='job title')
   parser.add_argument('--password', type=str, help='mailbox password')
   args = parser.parse_args()
   main(user=args.user, fname=args.fname, lname=args.lname, dname=args.dname, job=args.job, password=args.password)
time.sleep(3)
# New mailbox info gathering #
# username = input('Enter username ')
# password = input('Enter password ')
# fname = input('Enter first name ')
# lname = input('Enter last name ')
# dname = input('Enter display name ')
# job = input('Enter job title ')
# Logging into the website #
search_form = driver.find_element_by_id('LoginName')
search_form.send_keys('user')
search_form = driver.find_element_by_id('Password')
search_form.send_keys('password')
search_form.submit()
time.sleep(3)
# Finding all the important fields, and clicking on things #
provision = driver.find_element_by_xpath('/html/body/div[2]/div[2]/nav/div/ul/li[4]/a/span[2]').click()
time.sleep(1)
exchange = driver.find_element_by_xpath('/html/body/div[2]/div[2]/nav/div/ul/li[4]/ul/li/a').click()
time.sleep(1)
mailboxes = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[3]/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[6]/div/button[1]').click()
time.sleep(1)
create_mailbox = driver.find_element_by_css_selector('button.btn-primary:nth-child(1)').click()
time.sleep(2)
# # Entering attributes #
add_user_name = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/form/div[6]/div/div[1]/div/div[1]/div/input').send_keys(args.user)  #Had to match on the "Full Xpath" via Chrome#
add_password = driver.find_element_by_xpath('//*[@id="Password"]').send_keys(args.password)
add_password2 = driver.find_element_by_xpath('//*[@id="ConfirmPassword"]').send_keys(args.password)
user_profile = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/form/div[9]/ul/li[2]').click()
add_DN = driver.find_element_by_xpath('//*[@id="GeneralProfile_DisplayName"]').send_keys(args.dname)
add_fname = driver.find_element_by_xpath('//*[@id="GeneralProfile_FirstName"]').send_keys(args.fname)
add_lname = driver.find_element_by_xpath('//*[@id="GeneralProfile_LastName"]').send_keys(args.lname)
add_job = driver.find_element_by_xpath('//*[@id="GeneralProfile_JobTitle"]').send_keys(args.job)
adv_settings = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/form/div[9]/ul/li[1]').click()
# Mailbox Settings #
# Enable unlimited size
mail_size = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/form/div[9]/div/div[1]/div/div[2]/div/span/label/input')
mail_size.click()
# Enable unlimited for Prohibit send/recieve
mail_size1 = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/form/div[9]/div/div[1]/div/div[5]/div/span/label/input')
mail_size1.click()
mail_size2 = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/form/div[9]/div/div[1]/div/div[6]/div/span/label/input')
mail_size2.click()
# Save mailbox changes #
save_button = driver.find_element_by_xpath('//*[@id="SaveBtn"]').click()
