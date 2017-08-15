# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:41:19 2015

@author: justin.malinchak
"""

from webscraping import download, xpath
D = download.Download()

html = D.get('https://www.hedgefundresearch.com/hfrx_reg/index.php')
for row in xpath.search(html, '//table[@class="spad"]/tbody/t'): #xpath.search(html, '<b class=tenpx>HFRX Global Hedge Fund Index</b></TD>'):
    cols = xpath.search(row, '/td')
    print 'Sunrise: %s, Sunset: %s' % (cols[1], cols[2])