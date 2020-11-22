from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, time, string

driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
driver.get('https://docs.google.com/forms/d/1cwrwbYnALz9B3rsqZQBi9Ipd6hpPC9uTb5aoK_0yxMU/viewform?ts=5fb61caa&gxids=7628&edit_requested=true')

name = driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
letters = string.ascii_letters
result_str = ''.join(random.choice(letters) for i in range(8))
name.send_keys(result_str)

phone = driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
n = 10
num = ''.join(["{}".format(random.randint(0, 9)) for i in range(0, n)])
phone.send_keys(num)



