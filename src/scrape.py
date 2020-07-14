from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.bestbuy.ca/en-ca/category/unlocked-phones/743355?icmp=bbym_shopby_unlocked_phones";

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup (page_html, "html.parser");

containers = page_soup.findAll("div",{"class":"productItemRow_hyNOs row_1Rbqw"})

container = containers[0]

name = container.findAll("div",{"class":"productItemName_3IZ3c"})
price = container.findAll("div",{"class":"productPricingContainer_3gTS3"})


filename = "products.csv";
f = open(filename,"w")
headers = "Product_Name, Pricing\n"
f.write(headers)

for container in containers:
    name_container = container.findAll("div",{"class":"productItemName_3IZ3c"})
    name = name_container[0].text

    price_container = container.findAll("div",{"class":"productPricingContainer_3gTS3"})
    price = price_container[0].text

    print("product_name: "+name)
    print("Price: " + price)

    f.write(name.replace(",","|")+ ","+ price+"\n")
f.close()
