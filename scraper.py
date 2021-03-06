# python application that trackes a product on amazon and notifies you via email
# if price has gone down

import re
import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.com/dp/B07K97BQDF/ref=us_comp_a_ip_xr_5c008'

#gives information about the browser
header = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}



def analyze_price():
    page = requests.get(URL, headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    convert_price = price[0:4]
    convert_price = re.sub('[$]', '', convert_price)
    convert_price = int(convert_price)
    print(title)
    print(convert_price)

    if(convert_price < 700):
       send_mail()

    print(convert_price)
    print(title.strip())

    if(convert_price > 700):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()       
    server.starttls()   
    server.ehlo()

    server.login('email336699@gmail.com', 'Password336699')

    subject = 'Price dropped!'
    body = 'Check the link to see the the reduced price https://www.amazon.com/dp/B07K97BQDF/ref=us_comp_a_ip_xr_5c008'
    print('hello')

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'email336699@gmail.com',
        'newemail123@outlook.com',
        message
    )

    print('Amazon Price Tracker Email Has Been Sent')

    server.quit()


analyze_price()





