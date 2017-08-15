# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 13:18:36 2015

@author: justin.malinchak
"""

#import os, os.path
#dirtocheck = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\msci\\'
#for root, _, files in os.walk(dirtocheck):
#    for f in files:
#        fullpath = os.path.join(root, f)
#        print fullpath

import os    
dirtocheck = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\Downloads\\msci\\'
files = os.listdir(dirtocheck)
for filename in files:
    fullpath = os.path.join(dirtocheck, filename)
    print fullpath