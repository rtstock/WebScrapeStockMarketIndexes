# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:23:27 2015

@author: justin.malinchak
"""

import urllib2

response = urllib2.urlopen("http://google.de")
page_source = response.read()
print page_source