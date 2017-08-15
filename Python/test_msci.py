# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:01:36 2015

@author: justin.malinchak
"""
# http://www.boerse-frankfurt.de/en/etfs/db+x+trackers+msci+world+information+technology+trn+index+ucits+etf+LU0540980496/price+turnover+history/historical+data#page=1
# http://www.boerse-frankfurt.de/en/etfs/db+x+trackers+msci+world+information+technology+trn+index+ucits+etf+LU0540980496/price+turnover+history/historical+data#page=2
from bs4 import BeautifulSoup
import urllib
import urllib2
import re

url = 'http://www.boerse-frankfurt.de/en/parts/boxes/history/_histdata_full.m'
values = {'COMPONENT_ID':'PREeb7da7a4f4654f818494b6189b755e76', 
    'ag':'103708549', 
    'boerse_id': '12',
    'include_url': '/parts/boxes/history/_histdata_full.m',
    'item_count': '126',
    'items_per_page': '50',
    'lang': 'en',
    'link_id': '',
    'min_time': '2015-03-11',
    'max_time': '2015-05-21',
    'page': 0,
    'page_size': '50',
    'pages_total': '4',
    'secu': '103708549',
    'template': '0',
    'titel': '',
    'title': '',
    'title_link': '',
    'use_external_secu': '1'}

dates = []
prices = []
while True:
    print 'PAGE',values['page']
    print values
    
    data = urllib.urlencode(values)
    request = urllib.urlopen(url, data)
    soup = BeautifulSoup(request.read())
    temp_dates  = soup.findAll('td', class_='column-date')
    temp_dates  = [re.sub('[\\nt\s]','',d.string) for d in temp_dates]
    temp_prices = soup.findAll('td', class_='column-price')
    temp_prices = [re.sub('[\\nt\s]','',p.string) for p in temp_prices]
    if not temp_prices:
        print 'done'
        break
    else:
        dates = dates + temp_dates
        prices = prices + temp_prices
        values['page'] += 1
print dates
print prices
