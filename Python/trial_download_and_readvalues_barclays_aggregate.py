marketvalues_dict = {}

import datetime

today = datetime.date.today()
print 'today is:', today

dict_of_date8s = {}
iref = -15
while True:
    if iref > 0:
        break
    refdate = today + datetime.timedelta(days=iref)
    refdate8 = str(refdate).replace('-','')
    dict_of_date8s[len(dict_of_date8s)] = refdate8
    iref = iref + 1

for key, value in sorted(dict_of_date8s.iteritems()):
    #print(key, value)

    myfile = 'C:\\Batches\\AutomationProjects\\Investment Strategy\\ETL\\Downloads\\Unprocessed\\barclays\\'+value+'.agg'
    import os
    import good_readvalue_marketvalue_barclays_aggregate as o
    p = o.perform()
    mydict = p.execute(myfile)
    for k,v in mydict.items():
        #print k,v
        #print v
        date8 = os.path.basename(v['filename'])[:8]
        marketvalue = v['marketvalue']
        marketvalues_dict[date8] = marketvalue
prevmv = -1
returns_dict = {}
for key, value in sorted(marketvalues_dict.iteritems()):
    currmv = float(value)
    #print(key, prevmv,currmv)
    if prevmv > 0:
        periodreturn = (currmv - prevmv) / prevmv
        returns_dict[key] = [prevmv,currmv,periodreturn]
    prevmv = currmv
    
for key, value in sorted(returns_dict.iteritems()):
    print key,value
