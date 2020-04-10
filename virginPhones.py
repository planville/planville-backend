from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import time
import pymysql


virginURL = "https://www.virginmobile.ca/en/phones/phones-summary.html"

driver = webdriver.Chrome("C:\\Users\\Admin\\webdrivers\\chromedriver.exe")
page = driver.get(virginURL);
time.sleep(5)


soup = BeautifulSoup(driver.page_source, 'html.parser')
planBlocks = soup.find_all('div', class_='item phone Smartphone')
counter = len(planBlocks)
print(counter)

filename = "virginPhones.csv";
f = open(filename,"w")
headers = "PhoneName, DownPayment, NoOfInstallments, DeviceURL\n"
f.write(headers)

for planBlock in planBlocks:
    # ---------------Find Phone name---------------------------------------------#
    phoneNameTag = planBlock.find("div",{"class":"phoneTitle ng-binding"})
    phoneName = phoneNameTag.text.strip()
    # ---------------Find Downpayment Amount---------------------------------------------#
    planAmountTag = planBlock.find("p",{"class":"onPlan ultra"})
    planAmount = planAmountTag.text.strip()
    # ---------------Find Monthly Payment and number of Insatllments---------------------------------------------#
    installmentsTag = planBlock.find("div", {"class": "price priceUltra"})
    installments = installmentsTag.text.strip()

    deviceURL = planBlock.find('a').get('href')
    providerURL = "https://www.virginmobile.ca/en/phones/"
    phoneURL = providerURL + deviceURL
    print("The URL of the phone is: " + phoneURL)
    f.write(phoneName+","+planAmount+","+installments+","+phoneURL+"\n")


f.close()

