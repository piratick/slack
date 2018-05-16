# Exercise in creating inbuilding an internal integration in Slack using using Python that contains an incoming webhook.
# let the fun begin

# open url in a new browser window in chrome 
import webbrowser
url = 'https://slack.com'
webbrowser.get('chrome').open_new_tab(url)

from selenium import webdriver
import time
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://codepad.org')
 
# click radio button
python_button = driver.find_elements_by_xpath("/html/body/header/nav[1]/div/ul/li[5]/a")[0]
python_button.click()
