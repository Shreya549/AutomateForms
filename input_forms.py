from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, string, time

driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')

driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdK76evV1DfAus-MsbjdX6hqpFar0bidvdlcddWRystcHg0eg/viewform')

time.sleep(5)

# driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
name = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
letters = string.ascii_letters
result_str = ''.join(random.choice(letters) for i in range(8))
name.send_keys(result_str)

email = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
result_str = ''.join(random.choice(letters) for i in range(5))
email_inp = result_str + '@gmail.com'
email.send_keys(email_inp)

phone = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
n = 10
num = ''.join(["{}".format(random.randint(0, 9)) for i in range(0, n)])
phone.send_keys(num)

whatsapp = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
n = 10
num = ''.join(["{}".format(random.randint(0, 9)) for i in range(0, n)])
whatsapp.send_keys(num)

college_name = driver.find_element_by_xpath('//html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
letters = string.ascii_letters
result_str = ''.join(random.choice(letters) for i in range(30))
college_name.send_keys(result_str)


branch = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input')
letters = string.ascii_letters
result_str = ''.join(random.choice(letters) for i in range(30))
branch.send_keys(result_str)

driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[2]/div[8]/span').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[2]/div[5]/span').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[2]/div[5]/span').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[2]/div[4]/span').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()