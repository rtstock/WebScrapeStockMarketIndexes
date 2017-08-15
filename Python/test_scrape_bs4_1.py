# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:05:03 2015

@author: justin.malinchak
"""

from bs4 import BeautifulSoup
import urllib2
url="http://www.99acres.com/property-in-velachery-chennai-south-ffid?"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
import re
properties = soup.find_all('a', title=re.compile('Bedroom'))
for eachproperty in properties:
    print eachproperty['href']+",", eachproperty.string