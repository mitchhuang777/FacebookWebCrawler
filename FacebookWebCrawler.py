# Write a program to scratch the facebooks and get the data

# WebDriver settings
# selenium 4.2.0 version

# Import regular expression
import re

# Time
import time

# Import selenium
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Path to the chromedriver
# Chromedriver 108.0.5359.22
# https://chromedriver.chromium.org/downloads
#### Notice the chromedriver version and google chrome version ###
PATH = "chromedriver"

# Set the options
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-default-apps")
options.add_argument("--disable-translate")
options.add_argument("--disable-sync")
options.add_argument("--disable-background-networking")
options.add_argument("--disable-background-timer-throttling")
options.add_argument("--disable-client-side-phishing-detection")
options.add_argument("--disable-component-update")
options.add_argument("--disable-domain-reliability")
options.add_argument("--disable-hang-monitor")
options.add_argument("--disable-ipc-flooding-protection")

# full screen
options.add_argument("--start-maximized")

# Please input the data you want to search
keyword = input("Please input the data you want to search: ")
# Please input the year you want to search, the year should be between 2004 to current year
year = input("Please input the year you want to search: ")
# if year not between 2004 to current year, please input again
while int(year) < 2004 or int(year) > int(time.strftime("%Y", time.localtime())):  # time.strftime("%Y", time.localtime()) get the current year
    year = input("Please input the year you want to search, the year should be between 2004 to current year: ")
# Please input the data you want to search in the context
context = input("Please input the data you want to search in the context: ")

# Set the driver
driver = webdriver.Chrome(PATH, options=options)

# Import beautifulsoup
from bs4 import BeautifulSoup

# Open the facebook
driver.get("https://www.facebook.com/")
# Open a file to read the username and password
with open("account.txt", "r") as f:
    user = f.readline()
    # Select the username between " and "
    user = re.findall(r'"(.*?)"', user)[0]
    # Select pswd between " and "
    pswd = f.readline()
    pswd = re.findall(r'"(.*?)"', pswd)[0]

# Wait until the email and password input box is loaded
email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "pass"))
)

# Get the email and password
email = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
# Input the email and password
email.send_keys(user)
password.send_keys(pswd)

# Click the login button
login = driver.find_element_by_name("login")
login.click()

# Wait until the search box is loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='搜尋 Facebook']")))
time.sleep(3)
# Click the search box
search = driver.find_element_by_xpath("//input[@placeholder='搜尋 Facebook']").click()
# Find the search box
search = driver.find_element_by_xpath("//input[@placeholder='搜尋 Facebook']")

# Create an array to store the data
data = []
data.append(keyword)

# Input the keyword
search.send_keys(keyword)
# Enter the search
search.send_keys(Keys.RETURN)

# Funciton 1: 先用臉書搜尋，接著點選最新貼文ex: 2022
# Click "貼文" button
# Wait until the "貼文" button is loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='貼文']")))
# Click the "貼文" button
post = driver.find_element_by_xpath("//span[text()='貼文']").click()

time.sleep(1)
# aria-label="最新貼文"
# input[@aria-label='最新貼文']
# Wait until the '最新貼文' is loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='最新貼文']")))
# Click the '最新貼文'
newest_post = driver.find_element_by_xpath("//input[@aria-label='最新貼文']").click()

# aria-label="發佈日期"
# span[@aria-label='發佈日期']
# Wait until the '發佈日期' is loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='發佈日期']")))
# Click the '發佈日期'
publish_date = driver.find_element_by_xpath("//span[text()='發佈日期']").click()

# Click year年
# span[text()='year年']
# Wait until the 'year年' is loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='" + year + "年']")))
# Click the 'year年'
year = driver.find_element_by_xpath("//span[text()='" + year + "年']").click()
time.sleep(5)

success = 0
scroll_times = 1000

# Funciton 2: 然後讀取右邊內容，有隱藏的需要自動點開
for i in range(1, scroll_times):
    # <div class ="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f" role="button" 
    # Find all "顯示更多" button
    # Wait until the '顯示更多' is loaded
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//div[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f']")))
    except:
        # Scroll down the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if len(driver.find_elements_by_xpath("//span[text()='無其他結果']")) > 0:
            break   
        time.sleep(0.2)
        continue

    show_more = driver.find_elements_by_xpath("//div[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f']")
    if len(show_more) > 0:
        for show in show_more:
            time.sleep(0.1)
            try:
                # if show_more contains "其他 x 人" then continue
                if show.text.find("其他") != -1:
                    continue 
                show.click()
                success += 1
            except:
                # if failed to click, click again
                try:
                    show.click()
                    success += 1
                except:
                    continue
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.1)
    # print(i)
    # If the page has "無其他結果" then break
    if len(driver.find_elements_by_xpath("//span[text()='無其他結果']")) > 0:
        break

# Beautiful soup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all the posts (data-ad-preview="message")
posts = soup.find_all("div", {"data-ad-preview": "message"})

# Funciton 3: 取得特定url
link_list = []
# Get the post content
for post in posts:
    # if post contains context
    if context in post.text:
        # Find all url in the post
        lines = re.findall(r'http[s]?://[\S]+', post.text)

        for line in lines:
            # if link contains chineses characters, remove the character after the chinese character
            if re.search('[\u4e00-\u9fff]', line):
                line = line.split(' ')[0]

            links = re.findall(r'http[s]?://[\S]+', line)
            start = 0
            end = 0
            for link in links:
                while True:
                    # locate the context index
                    start = link.find(context, end)
                    # if the context is not found, break
                    if start == -1:
                        break
                    # Find the first index before the context
                    while start >= 0:
                        # Find https or http index
                        if link[start:start+5] == "https":
                            end = link.find("https", start + 1)
                            break
                        if link[start:start+4] == "http":
                            end = link.find("http", start + 1)
                            break
                        start -= 1
                    if end == -1:
                        url = link[start:]
                    else:
                        url = link[start:end]
                    # Find the first chinese character index
                    for i in range(len(url)):
                        if re.search('[\u4e00-\u9fff]', url[i]):
                            url = url[:i]
                            break
                    # if find ... in the url, remove the ... after the url
                    if url.find("...") != -1:
                        url = url[:url.find("...")]
                    # if find --- in the url, remove the --- after the url
                    if url.find("---") != -1:
                        url = url[:url.find("---")]
                    # if find 🅨🅞🅤🅣🅤🅑🅔 in the url, remove the 🅨🅞🅤🅣🅤🅑🅔 after the url
                    if url.find("🅨") != -1:
                        url = url[:url.find("🅨")]
                    # if find 🅘🅝🅢🅣🅐🅖🅡🅐🅜 in the url, remove the 🅘🅝🅢🅣🅐🅖🅡🅐🅜 after the url
                    if url.find("🅘") != -1:
                        url = url[:url.find("🅘")]
                    # if find '、', '。', '，', '．', '《', '【', '…', remove the character after the '、', '。', '，'
                    if url.find("、") != -1:
                        url = url[:url.find("、")]
                    if url.find("。") != -1:
                        url = url[:url.find("。")]
                    if url.find("，") != -1:
                        url = url[:url.find("，")]
                    if url.find("．") != -1:
                        url = url[:url.find("．")]
                    if url.find("《") != -1:
                        url = url[:url.find("《")]
                    if url.find("【") != -1:
                        url = url[:url.find("【")]
                    if url.find("…") != -1:
                        url = url[:url.find("…")]
                    if url.find("91APP") != -1:
                        url = url[:url.find("91APP")]

                    # if the url is not in the list, append the url
                    if url not in link_list:
                        link_list.append(url)

# Create a text file, the name is date plus the time
with open(time.strftime("%Y%m%d-%H%M%S") + '.txt', 'w') as f:
    # for each link in the link_list
    for link in link_list:
        # write the link into the text file
        try: 
            f.write(link + '\n')
        except:
            continue

# Close the browserf
driver.close()

print("success: ", success)

# Count the number of link_list
print("New URL: ", len(link_list))
print()

for link in link_list:
    print(link)

print()
print("Finish")