
#################################################################################
download_last_x_days = -2000

#################################################################################
import good_downloadclass_barclays_aggregate as c1
p1 = c1.perform()
directory_where_datafiles_are_downloaded = p1.execute(download_last_x_days)
print 'OK',directory_where_datafiles_are_downloaded

#################################################################################

#################################################################################
import config
import os
import good_readvalues_marketvalue_barclays_aggregate as ofile
pclass = ofile.perform()
newdata_dict = pclass.execute(download_last_x_days,directory_where_datafiles_are_downloaded)

import datetime
filedatetime = datetime.datetime.today()
filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S')

# Get path of savedjsonfile
savedjsonfile = os.path.join(config.localdatafileoutputpath,'dailyreturns-barclays-usaggregate.json')

def create_saved_dict(p_savedjsonfile):
    import json
    saved_dict = {}
    try:
        with open(p_savedjsonfile) as f:
            saved_dict = json.load(f)
    except Exception as e:
        print 'error: just created a new saved_dict'
    return saved_dict

        
import json
if os.path.isfile(savedjsonfile) == True:
    print 'got here 1'
    # Read file with previously saved data into dictionary
    saved_dict = create_saved_dict(savedjsonfile)
    print len(saved_dict)
    # Create a copy of saved_dict, call it updated_dict and update it with newdata_dict
    updated_dict = saved_dict.copy()
    updated_dict.update(newdata_dict)
else:
    print 'got here 2'
    updated_dict = newdata_dict

# save updated_dict to savedjsonfile
#import json
with open(savedjsonfile, 'w') as f:
    json.dump(updated_dict, f)

# open savedjsonfile into testing_dict, and print key values to screen
with open(savedjsonfile) as f:
    testing_dict = json.load(f)
for key, value in sorted(testing_dict.iteritems()):
    print value['currdate'], value['filedatetime'], value['periodreturn']


print 'You can find your file here:',savedjsonfile

