#!/usr/bin/env python
#encoding:utf8
import pickle
try:
    db=open('/var/log/uptime.db','rb')
    result=pickle.load(db)
    db.close()
except:
    print('db file not exits makeit!')
    result={'uptime':0,'bootimes':0}
fi=open('/var/log/uptime.log')
src=fi.read().strip().split()
result['uptime']+=float(src[0])/3600/24
result['bootimes']+=1
print(result)
db=open('/var/log/uptime.db','wb')
pickle.dump(result,db)

