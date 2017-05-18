import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

quote_page = {'http://nurserylive.com/buy-medicinal-plants-online-in-india?start=30'}

data = []
for pg in quote_page:
    # query the website and return the html to the variable 'page'
    page = urllib2.urlopen(pg)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
   # name_box = soup.findall('h3', attrs={'class': 'text-left'})
    for y in  soup.findall('h3', attrs={'class': 'text-left'}):
        name = y.text.strip()  # strip() is used to remove starting and trailing

    # get the index price
    #price_box = soup.findall('h3', attrs={'class': 'text-left'})
    for y in soup.soup.findall('h3', attrs={'class': 'text-left'}):
        price = y.text.strip()

    # save the data in tuple
    data.append(name,price)
print data
