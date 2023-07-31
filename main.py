# Libraries for Selenium
from selenium import webdriver
import time
# Libraries for email function
from email.message import EmailMessage
import ssl
import smtplib

### GLOBAL VARIABLES ####
sendEmail = ''
sendEmailPass = ''
receivingEmail = ''

dept = 'cpsc'
code = '121'
section = 'l1j'

setInterval = 60
### MAKE SURE TO FILL THESE OUT ###

def linkFormula(dept, code, section):
    URL = f'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept={dept}&course={code}&section={section}'
    return URL

def checker(URL):
    # Need these options to run Selenium headless but with a set user agent parameter to bypass user-agent detection.
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    
    driver = webdriver.Chrome(options=options)
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
        
        time.sleep(setInteval)
        driver.refresh()

def email():
    body = 'DO IT BRO'
    # Instance of EmailMessage()
    em = EmailMessage()
    em['From'] = sendEmail
    em['To'] = receivingEmail
    em['subject'] = 'Sign up for your course!'
    em.set_content(f'Your course, {dept}{code} {section} has availability!')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sendEmail, sendEmailPass)
        smtp.sendmail(sendEmail, receivingEmail, em.as_string())
    
def main():
    if checker(linkFormula(dept, code, section)):
        email()
    
main()