import requests
from bs4 import BeautifulSoup
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max",help="Enter the number of pages to parse",type=int)
parser.add_argument("--dbname",help="Enter the number of pages to parse",type=str)
args = parser.parse_args()


flipkart_url = "https://www.flipkart.com/clothing-and-accessories/topwear/tshirts/pr?sid=clo%2Cash%2Cank&marketplace=FLIPKART&page="
page_num_max = args.page_num_max
scraped_info_list = []
connect.connect(args.dbname)
for page_num in range(1,page_num_max+1):
    url = flipkart_url+str(page_num)
    print(url)
    req = requests.get(url)
    content = req.content

    soup = BeautifulSoup(content,"html.parser")

    products = soup.find_all("div", {"class": "_2B099V"})

    for product in products:
        product_dict = {}
        product_dict["Brand Name"] = product.find("div", {"class": "_2WkVRV"}).text
        product_dict["Product Name"] = product.find("a", {"class": "IRpwTa"}).text
        product_dict["Price"] = product.find("div", {"class": "_30jeq3"}).text
        try:
            product_dict["discount"] = product.find("div", {"class": "_3Ay6Sb"}).text
        except AttributeError:
            product_dict["discount"] = None
        scraped_info_list.append(product_dict)
        connect.insert_into_table(args.dbname, tuple(product_dict.values()))

connect.get_product_info(args.dbname)
