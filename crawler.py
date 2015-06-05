__author__ = 'Shubham'

from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests

visited = []


def find(max):
    page = 1
    url = "http://www.indeed.co.in/jobs?q="
    print "Enter Job Description"
    a = raw_input()
    print "Enter Location"
    b = raw_input()
    #c = input()
    #max = c
    url = url + str(a) + "&l=" + str(b)
    while page <= max:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        try:
            for div in soup.find_all('div', {'class': 'row  result'}):
                if div.find('div',{'class': 'iaP'}):
                    visited.append(div.find('a', {'itemprop': 'title'}))
        except:
            print "error"
        url = "" + url + "&start=" + str(page) + "0"
        page += 1

find(2)
i = 1
c = MongoClient('localhost')
print c.database_names()
db = c.test5

lin = db.lin
for link in visited :
    try:
        newurl="http://www.indeed.co.in" + link.get('href')
        #print newurl
        #print str(i) + ") " + link.get('title')
        source_code = requests.get(newurl)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        lin.insert({'id':str(i),'link':link.get('title'),'Company':soup.find('span', {'class': 'company'}).text,'Location':soup.find('span', {'class': 'location'}).text,'Description':soup.find('span', {'class': 'summary'}).text})
        #print "Company: " + soup.find('span', {'class': 'company'}).text
        #print "Location: " + soup.find('span', {'class': 'location'}).text
        #print "Description:\n             " + soup.find('span', {'class': 'summary'}).text
    except:
        print "err"
    i += 1
peer = lin.find()
for x in peer:
    print x