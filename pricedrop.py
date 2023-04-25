import numpy as np
import pandas as pd
import re
import smtplib
from bs4 import BeautifulSoup
import requests

url='https://www.flipkart.com/nutrabay-pure-series-whey-protein-concentrate-raw-usa-33-servings/p/itm7b92e8ee7a4ac?pid=PSLFHNGCXQMGDGMN&lid=LSTPSLFHNGCXQMGDGMNYSGMEJ&marketplace=FLIPKART&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&fm=SEARCH&iid=eb74d601-5e8c-48c7-a46a-b86f0b3ef15c.PSLFHNGCXQMGDGMN.SEARCH&ppt=sp&ppn=sp&ssid=9fdwf16im80000001589007101432&qH=23303970e8805854 '

#search for my user agent in  browser
title={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

#function for check price
def checkprice():

    page = requests.get(url, headers=title) #access url link
    soup = BeautifulSoup(page.content, 'html.parser') #page content

    product = soup.find('span', {"class": '_35KyD6'}).get_text() #inspect for product name
    price = soup.find('div', {"class": '_1vC4OE _3qQ9m1'}).get_text() #inspect for productprice

    #convert string value into integer
    a = [float(i) for i in price if i.isdigit()]
    convertedprice = a[0] * 1000 + a[1] * 100 + a[2] * 10 + a[3] #convert into aprropriate value

    #check for price drop
    if(convertedprice<2000):
        send_mail()


def send_mail():
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.ehlo()


   //comment
   //comment

   #generate password for your gmail account
   server.login('shivnathchavan101@gmail.com','generated password')
   #content of gmail
   subject="price fell down"
   body="go to th link 'https://www.flipkart.com/nutrabay-pure-series-whey-protein-concentrate-raw-usa-33-servings/p/itm7b92e8ee7a4ac?pid=PSLFHNGCXQMGDGMN&lid=LSTPSLFHNGCXQMGDGMNYSGMEJ&marketplace=FLIPKART&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&fm=SEARCH&iid=eb74d601-5e8c-48c7-a46a-b86f0b3ef15c.PSLFHNGCXQMGDGMN.SEARCH&ppt=sp&ppn=sp&ssid=9fdwf16im80000001589007101432&qH=23303970e8805854 '"

   msg=f"subject:{subject}\n\n{body}"

   server.sendmail(
       'sc18111999@gmail.com',
       'shivnathchavan101@gmail.com',
       msg
   )
   print("done")
   server.quit()

 //comment

#function to checkprice
checkprice()