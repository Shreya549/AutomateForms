from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')

def fill():
    # try:
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdF5S7wsRSfwWODm5761WAZJaGgZ28WhFQhM0DE0gW73gH1jw/viewform')

    options = [3, 3, 5, 2, 3, 3, 3, 3]

    for i in range(1, 9):
        option_range = options[i-1]
        option = random.randint(1, option_range)
        path = '/html/body/div/div[2]/form/div[2]/div/div[2]/div['  + str(i) +  ']/div/div/div[2]/div/div/span/div/div[' + str(option) +']/label/div/div[1]/div/div[3]/div'
        driver.find_element_by_xpath(path).click()

    # Submit button
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span').click()


i = 1
while (i<=10):
    fill()
    i+=1

driver.quit()
