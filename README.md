# Web-scraping-project
      * A python script to collect Product details such as Name, Brand, Price and Discount for 
        Men's T-Shirts from Flipkart and store it as .db file i.e database file using sql 
# What I Used
    * I used 'requests' to obtain data from the url provided.
    * I used 'BeautifulSoup' to parse the html file of the link provided.
    * I used 'argparse' to help enter arguments directly in command line.
    * I used 'sqlite3' to create .db file and store the data collected from the web page.

# How to run
    * To run the script enter "python scrapper.py --page_num_max 5 --dbname product_info.db" in terminal or shell.
    * In the above line "5" and "product_info.db" are arguments that can enterd as users wish.
    * Make sure dbname is unique. If any file with the same dbname already exists, then the code won't run.
 
# Code Breakdown
## Connect Module(connect.py)
        
        * I import sqlite3.
        * 'connect' function to create database file with filename argument  and table with name,
           brand, price, discount as arguments.
        * 'insert_into_table' function to add values to the table.
        * 'get_product_info' function to fetch and print(or display) the product details.
        
## Main Program(scrapper.py)
        * We have to import requests,argparse, connect, beautifulSoup from bs4
        * 'flipkart_url' variable contains the URl of the product you want to track.
        * 'page_num_max' variable stores the number of pages we want to scrap.
        * 'scraped_info_list' a list to collect product details.
        * A 'for' loop to execute code in all pages
            * 'req' variable requests the acess to URL.
            * 'content' varable stores the contents of the URL.
            * 'soup' variable parses the contents from the html file using BeautifulSoup.
            * 'products' lists all the products in that page  from the soup variable
            * Another 'for' loop to iterate through each product.
                * 'product_dict' a dictionary to store the each product details seperately.
                * In 'product_dict'  
                    "Brand Name" keyword stores the name of the brand.
                    "Name" keyword stores the name of the product.
                    "Price" keyword stores the price of the product in Rupees.
                    "Discount" keyword stores the discount percentage on the product.
                * A 'try' and 'except' block is assigned for Discount to avoid error if no discount is available.
                * 'append' function used to add the 'product_dict' to 'scrapped_info_list'
                * 'insert_into_table' function inserts the scraped data into the database file.
        * 'get_product_info' function fetches and displays the product information line by line.
## Result
    * When the code is run scuccessfully a new .db file with same name as the arqument dbname
      is created in the same directory where the scrapper.py is present.
    * You can use the db file directly or convert it into a csv file to view the product details.
