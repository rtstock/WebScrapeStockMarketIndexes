# -*- coding: cp1252 -*-
ddir = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\Ready for daily processing\\'
download_last_x_days = -3000
#################################################################################
import config

import os
import good_readvalues_marketvalue_barclays_aggregate as o

#print config.localunprocessedfolder
#localunprocessedfolderext = os.path.join(config.localunprocessedfolder,'barclays')

p = o.perform()
newdata_dict = p.execute(download_last_x_days,ddir)

import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')

# Get path of savedjsonfile
savedjsonfile = os.path.join(config.localdatafileoutputpath,'dailyreturns-barclays-usaggregate.json')

# Read file with previously saved data into dictionary
import json
with open(savedjsonfile) as f:
    saved_dict = json.load(f)

# Create a copy of saved_dict, call it updated_dict and update it with newdata_dict
updated_dict = saved_dict.copy()
updated_dict.update(newdata_dict)

# save updated_dict to savedjsonfile
#import json
with open(savedjsonfile, 'w') as f:
    json.dump(updated_dict, f)

# open savedjsonfile into testing_dict, and print key values to screen
with open(savedjsonfile) as f:
    testing_dict = json.load(f)
for key, value in sorted(testing_dict.iteritems()):
    print value['currdate'],value['periodreturn']


print 'You can find your file here:',savedjsonfile



