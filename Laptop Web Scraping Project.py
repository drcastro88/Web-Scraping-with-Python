#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime
import lxml

import smtplib


# In[2]:


# Connect to Website and pull in data

URL = 'https://www.amazon.com/Acer-AN515-57-79TD-i7-11800H-GeForce-Keyboard/dp/B09R65RN43/ref=sr_1_7?crid=2V3CBB0QGEDFL&keywords=laptop&qid=1680901816&s=electronics&sprefix=%2Celectronics%2C138&sr=1-7'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "lxml")

soup2 = BeautifulSoup(soup1.prettify(), "lxml")

title = soup2.find(id='productTitle').get_text()

print(title)

price = soup2.find(id='mbc-price-2').get_text()

print(price)


# In[3]:


# Clean up the Data

title = title.strip()[:40]
price = price.strip()

print(title)
print(price)


# In[4]:


# Adding date to our dataset

import datetime

date = datetime.date.today()

print(date)


# In[6]:


# Create CSV file for Excel 

import csv

header = ['Title', 'Price', 'Date']
data = [title, price, date]

# Checking data type for new dataset

type(data)

with open('WebScrapingDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[7]:


# Now we will append data to the csv

with open('WebScrapingDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[8]:


# Creating a function for the combined code above

def price_checker():
    URL = 'https://www.amazon.com/Acer-AN515-57-79TD-i7-11800H-GeForce-Keyboard/dp/B09R65RN43/ref=sr_1_7?crid=2V3CBB0QGEDFL&keywords=laptop&qid=1680901816&s=electronics&sprefix=%2Celectronics%2C138&sr=1-7'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "lxml")

    soup2 = BeautifulSoup(soup1.prettify(), "lxml")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='mbc-price-2').get_text()
    
    title = title.strip()[:40]
    price = price.strip()
    
    import datetime

    date = datetime.date.today()

    import csv

    header = ['Title', 'Price', 'Date']
    data = [title, price, date]
    
    with open('WebScrapingDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    if(price < 700):
        send_mail()


# In[ ]:


# Creating a timer to check the price daily

while(True):
    price_checker()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv('WebScrapingDataset.csv')

print(df)


# In[3]:


# Sending an email to myself if this labtop goes under $700

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('drcastro12345@gmail.com','*************')
    
    subject = "The laptop you want is now on sale!"
    body = "Derek, the amazing gaming laptop that you've had your eyes on is on sale! Get your hands on it before it's gone! Link here: https://www.amazon.com/Acer-AN515-57-79TD-i7-11800H-GeForce-Keyboard/dp/B09R65RN43/ref=sr_1_7?crid=2V3CBB0QGEDFL&keywords=laptop&qid=1680901816&s=electronics&sprefix=%2Celectronics%2C138&sr=1-7"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'derekcastro12345@gmail.com',
        msg
     
    )


# In[ ]:




