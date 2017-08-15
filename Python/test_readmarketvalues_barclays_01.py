import config

import os
import good_readvalues_marketvalue_barclays_aggregate as o

print config.localunprocessedfolder
localunprocessedfolderext = os.path.join(config.localunprocessedfolder,'barclays')

p = o.perform()
mydict = p.execute(-30,localunprocessedfolderext)

for key, value in sorted(mydict.iteritems()):
    print key,value
