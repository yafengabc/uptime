#!/usr/bin/env python
#encoding:utf8
import pickle
import sqlite3

def format_his():
    sqldb=sqlite3.connect('/var/log/uptime.hi')
    cur=sqldb.execute('SELECT * FROM bootlist')
    li=cur.fetchall()
    print('----------开机历史----------------')
    for i in li:
        ti=int(float(i[1]))
        Day=ti//(3600*24)
        Hou=ti//3600-Day*24
        Min=ti//60
        print(i[0],"{}天{}小时{}分钟".format(Day,Hou,Min))

format_his()

try:
    db=open('/var/log/uptime.db','rb')
    result=pickle.load(db)
    db.close()
except:
    print('db file not exits!')
    boot_t=time.strftime('%Y-%m-%d %H:%M:%S')
    result={'uptime':0,'bootimes':0,'begin':boot_t}
ti=result['uptime']
Day=int(ti)
Hour=int((ti-Day)*24)
Min=int(60*((ti-Day)*24-Hour))
print('----------开机统计----------------')
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
print("本程序计时开始于",t)
