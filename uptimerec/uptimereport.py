#!/usr/bin/env python
#encoding:utf8
import pickle
try:
    db=open('/var/log/uptime.db','rb')
    result=pickle.load(db)
    db.close()
except:
    print('db file not exits!')
    t=list(time.localtime())
    result={'uptime':0,'bootimes':0,'begin':t}
ti=result['uptime']
Day=int(ti)
Hour=int((ti-Day)*24)
Min=int(60*((ti-Day)*24-Hour))
print("开机计时程序")
print('----------------------------------')
print("历史开机总时间:",Day,'天',Hour,"小时",Min,'分钟')
print("历史共开机",result["bootimes"],'次')
uptime=open('/proc/uptime').read().strip().split()[0]
ti=float(uptime)/3600/24
Day=int(ti)
Hour=int((ti-Day)*24)
Min=int(60*((ti-Day)*24-Hour))
print("本次开机时间:",Day,'天',Hour,"小时",Min,'分钟')
t=result['begin']
print('----------------------------------')
print("本程序计时开始于{0}年{1}月{2}日".format(t[0],t[1],t[2]))
