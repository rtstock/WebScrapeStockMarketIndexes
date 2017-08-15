import good_readmarketvaluesintodict_barclays_aggregate as obj
o = obj.perform()

#mypath = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\'
import config
print config.localunprocessedfolder


import os
folder1 = os.path.join(config.localunprocessedfolder,'barclays')
mydict1 = o.execute(-3000,folder1)
print mydict1
folder2 = os.path.join(config.localunprocessedfolder,'barclays','Ready for daily processing')
mydict2 = o.execute(-3000,folder2)
mydict1.update(mydict2)
print mydict1
