# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:54:43 2015

@author: Justin.Malinchak
"""

import os
import pandas as pd
file_name = os.path.join('C:\\','Batches','MyPython','DataAgg','output','test.pkl')
df = pd.read_pickle(file_name) 
print df
