# -*- coding: cp1252 -*-
ddir = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\'
download_last_x_days = -10
#################################################################################
import config

import os
import good_readvalues_marketvalue_barclays_aggregate as o

#print config.localunprocessedfolder
#localunprocessedfolderext = os.path.join(config.localunprocessedfolder,'barclays')

p = o.perform()
newdata_dict = p.execute(download_last_x_days,ddir)
for key, value in sorted(newdata_dict.iteritems()):
    print value['currdate'],value['periodreturn']

