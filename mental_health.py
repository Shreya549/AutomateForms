from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, time

driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')

fnames = [
    "Saanvi",
    "Anya",
    "Aadhya",
    "Aaradhya",
    "Ananya",
    "Pari",
    "Anika",
    "Navya",
    "Angel",
    "Diya",
    "Myra",
    "Sara",
    "Iraa",
    "Ahana",
    "Anvi",
    "Prisha",
    "Riya",
    "Aarohi",
    "Anaya",
    "Akshara",
    "Eva",
    "Shanaya",
    "Kyra",
    "Siya",
    "Aarav",
    "Vihaan",
    "Vivaan",
    "Ananya",
    "Diya",
    "Advik",
    "Kabir",
    "Anaya",
    "Aarav",
    "Vivaan",
    "Aditya",
    "Vivaan",
    "Vihaan",
    "Arjun",
    "Vivaan",
    "Reyansh",
    "Mohammed",
    "Sai",
    "Arnav",
    "Aayan",
    "Krishna",
    "Ishaan",
    "Shaurya",
    "Atharva",
    "Advik",
    "Pranav",
    "Advaith",
    "Aaryan",
    "Dhruv",
    "Kabir",
    "Ritvik",
    "Aarush",
    "Kian",
    "Darsh",
    "Veer"
  ]

surnames = [
    "Bedi",
    "Gandhi",
    "Parekh",
    "Kohli",
    "Ahluwalia",
    "Chandra",
    "Jha",
    "Khanna",
    "Bajwa",
    "Chawla",
    "Lal",
    "Anand",
    "Gill",
    "Chakrabarti",
    "Dubey",
    "Kapoor",
    "Khurana",
    "Modi",
    "Kulkarni",
    "Khatri",
    "Kaur",
    "Dhillon",
    "Kumar",
    "Gupta",
    "Naidu",
    "Das",
    "Jain",
    "Chowdhury",
    "Dalal",
    "Thakur",
    "Gokhale",
    "Apte",
    "Sachdev",
    "Mehta",
    "Ganguly",
    "Bhasin",
    "Mannan",
    "Ahuja",
    "Singh",
    "Bakshi",
    "Basu",
    "Ray",
    "Mani",
    "Datta",
    "Balakrishna",
    "Biswas",
    "Laghari",
    "Malhotra",
    "Dewan",
    "Purohit"
  ]

flen = len(fnames)
slen = len(surnames)

def fill():
    driver.get('https://docs.google.com/forms/d/1B3MLUQq6zgx1ruUf-0J3jjlDjwP1Py-oQQ5l2RsNwjg/viewform?edit_requested=true')
    time.sleep(5)
    fname = fnames[random.randint(0, flen-1)]
    sname = surnames[random.randint(0, slen-1)]
    name = fname + " " + sname
    print(name)

    name_input = driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_input.send_keys(name)

    
    for i in range(2, 12):
        option = random.randint(1, 5)
        path = '/html/body/div/div[3]/form/div[2]/div/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div/span/div/div[' + str(option) + ']/label/div/div[1]/div/div[3]/div'
        driver.find_element_by_xpath(path).click()

    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div/div/span/span').click()

i = 1
while (i<=20):
    fill()
    i+= 1
    if i==20:
        driver.quit()