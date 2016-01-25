#!/usr/bin/env python
#encoding:utf8
import pickle
import time
import sqlite3
#打开数据库，若不存在，新建一个
try:
    db=open('/var/log/uptime.db','rb')
    result=pickle.load(db)
    db.close()
except:
    print('db file not exits makeit!')
    boot_t=time.strftime('%Y-%m-%d %H:%M:%S')
    result={'uptime':0,'bootimes':0,'begin':boot_t,'boot_t':boot_t}

#打开上次启动存储的uptime数据
fi=open('/var/log/uptime.log')
src=fi.read().strip().split()
#存储上次开机的时间
result['uptime']+=float(src[0])/3600/24
#开机的次数+1
result['bootimes']+=1

#把上次开机时间，开机时长写入数据库
try:
    sqldb=sqlite3.connect("/var/log/uptime.hi")
    sqldb.execute('CREATE TABLE IF NOT EXISTS bootlist(boot_t,uptime)')
    sqldb.execute('INSERT INTO bootlist values("{0}","{1}")'.format(str(result['boot_t']),src[0]))
    sqldb.commit()
    sqldb.close()
except:
    pass

#存储本次的开机时间
boot_t=time.strftime('%Y-%m-%d %H:%M:%S')
result['boot_t']=boot_t
print(result)
#持久化存储result结构体
db=open('/var/log/uptime.db','wb')
pickle.dump(result,db)

