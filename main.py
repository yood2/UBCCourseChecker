# Libraries for Selenium
from selenium import webdriver
import time


def linkFormula(dept, code, section):
    URL = f'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept={dept}&course={code}&section={section}'
    return URL

def checker(URL):
    driver = webdriver.Chrome()
    driver.get(URL)

    # Wait till page is clickable
    time.sleep(2)

    # xpath for general seats
    xpath = '/html/body/div[2]/div[4]/table[4]/tbody/tr[3]/td[2]/strong'

    while True:
        alpha = int((driver.find_element('xpath', xpath)).text)
        print(alpha)

        if alpha > 0:
            print('yata desu ne!')
            return True
        
        time.sleep(5)
        driver.refresh()

def email(address):
    print("SIGN UP WEE OOO")
    
def main():
    dept = input('What dept?')
    code = int(input('What course code?'))
    section = input('What section?')

    URL = linkFormula(dept, code, section)
    if checker(URL):
        email('test@test.com')
    
main()