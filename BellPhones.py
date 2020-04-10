import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import time
import string
import pymysql


bellDevicesURL = "https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices"

driver = webdriver.Chrome("C:\\Users\\Admin\\webdrivers\\chromedriver.exe")
page = driver.get(bellDevicesURL);
time.sleep(10)
#Locate the button to load all devices and click
elementLocator = driver.find_element_by_xpath("//div[@class='rsx-product-grid-view-more row']//button[@type='button']");
elementLocator.click()
time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
#locate all the blocks to fetch device information
planBlocks = soup.find_all('div', class_='smartpay-product')

filename = "bellPhones.csv";
f = open(filename,"w")
headers = "PhoneName, DownPayment, PhonePrice, NoOfInstallments, DeviceURL\n"
f.write(headers)


#loop through each block and find all the needed device infromation
for planBlock in planBlocks:
    #---------------Find Phone name---------------------------------------------#
    phoneNameTag = planBlock.find("div",{"class":"smartpay-product-name"})
    phoneNameText = phoneNameTag.text
    phoneName = phoneNameText.strip()
    print("\nThe name of Phone is:"+phoneName)

    # ---------------Find Downpayment Amount---------------------------------------------#
    downpaymentTag = planBlock.find("div",{"class":"downpayment"})
    downpaymentText = downpaymentTag.text
    downAmountStrip = re.sub(r"^\s+|\s+$", " ", downpaymentText)
    downAmount = re.sub(r'\s*\n',' ',downAmountStrip)
    print("The downpayment is: "+downAmount)

    # ---------------Find Monthly Payment and number of Insatllments---------------------------------------------#
    monthlyPaymentTag = planBlock.find("div", {"class": "monthly-payments"})
    monthlyPaymentText = monthlyPaymentTag.text
    monthlyPaymentStrip = re.sub(r"^\s+|\s+$", "", monthlyPaymentText)
    monAmt = monthlyPaymentStrip.split('\n')
    amount = monAmt[0]
    installments = monAmt[2]
    print("The price is:"+amount)
    print("The number of installments are: "+installments)
    deviceURL = planBlock.find('a').get('href')
    providerURL = "https://www.bell.ca"
    phoneURL = providerURL+ deviceURL
    print("The URL of the phone is: "+phoneURL)

    f.write(phoneName + "," + downAmount + "," + amount + "," + installments + "," + phoneURL + "\n")


f.close()