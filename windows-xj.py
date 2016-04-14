
/usr/bin/env python
#coding=utf-8
"
@author : eric,i-menyoy
@date   : /4/15/16
@version: 1.0 
"

import wmi 
import os 
import sys 
import platform 
import time
import win32evtlog
import win32evtlogutil
import winerror
import datetime
import codecs
#cpu-info
print
def cpu(): 
    c = wmi.WMI ()        
    for processor in c.Win32_Processor(): 
        print "Processor ID: %s" % processor.DeviceID 
        print "Process Name: %s" % processor.Name.strip() 
cpu()


# start-time-info
print
c = wmi.WMI()
for sys in c.Win32_OperatingSystem():
    boottime = sys.lastbootuptime

boottime = boottime.split('.')[0]
boottime = datetime.datetime.strptime(boottime,'%Y%m%d%H%M%S')
d = datetime.datetime.now() - boottime
print d



#disk-io-info
print 
from psutil import disk_io_counters
disk_io = disk_io_counters()
print "Disk Read: %s MB" %long( disk_io.read_bytes /1024 /1024/ 1024)
print "Disk Write: %s MB" %long( disk_io.write_bytes /1024 /1024 /1024)



#disk-info
print
def disk(): 
    c = wmi.WMI()
    for physical_disk in c.Win32_DiskDrive (): 
        for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
            for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"): 
                print physical_disk.Caption.encode("UTF8"), partition.Caption.encode("UTF8"), logical_disk.Caption 

    for disk in c.Win32_LogicalDisk (DriveType=3): 
        print disk.Caption, str(long(disk.Size) / 1024 / 1024 / 1024 ) + 'GB', "%0.2f%% free" % (100.0 * long (disk.FreeSpace) / long (disk.Size)) 
disk()

#sys-version-info
print
def sys_version():  
    c = wmi.WMI()
    for sys in c.Win32_OperatingSystem(): 
        print "Version:%s" % sys.Caption.encode("UTF8"),"Vernum:%s" % sys.BuildNumber 
        print  sys.OSArchitecture.encode("UTF8")
        #print sys.NumberOfProcesses

sys_version()

#memory-info
print
def mem(): 
    c = wmi.WMI()
    for Memory in c.Win32_PhysicalMemory(): 
        print "Memory Capacity: %.fMB" %(int(Memory.Capacity)/1048576) 
mem()

#sys-log info


print

system_handle = win32evtlog.OpenEventLog("localhost", "System")
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
events = win32evtlog.ReadEventLog(system_handle, flags,0)
#logger = codecs.open('logger.txt', encoding='utf-8', mode='w')

all_events = {
        0 :   {},
        1 :   {},
        2 :   {},
        4 :   {},
    }

try:
    while 1:
        events = win32evtlog.ReadEventLog(system_handle, flags,0)
        if not events:
            break

        for ev_obj in events:
            msg = win32evtlogutil.SafeFormatMessage(ev_obj, 'System')
            #print type(msg.encode('GB2312'))

            msg = msg.encode('GB18030')
            log_time = ev_obj.TimeGenerated.Format()
            log_time = log_time.split()[0]
            log_time = datetime.datetime.strptime(log_time,'%m/%d/%y')
            now_time = datetime.datetime.now()
            day = now_time - log_time


            if day.days <= 7:
                if len(msg):
                    if all_events.has_key(ev_obj.EventType):
                        if not all_events[ev_obj.EventType].has_key(ev_obj.SourceName):
                            all_events[ev_obj.EventType][ev_obj.SourceName] = {}

                        if not all_events[ev_obj.EventType][ev_obj.SourceName].has_key(winerror.HRESULT_CODE(ev_obj.EventID)):
                            all_events[ev_obj.EventType][ev_obj.SourceName][winerror.HRESULT_CODE(ev_obj.EventID)] = {'data':None,'count':0}
                            #print day.days
                        all_events[ev_obj.EventType][ev_obj.SourceName][winerror.HRESULT_CODE(ev_obj.EventID)]['data'] = {
                                'SourceName'  : str(ev_obj.SourceName),
                                'event_level' : ev_obj.EventType,
                                'event_id'    : winerror.HRESULT_CODE(ev_obj.EventID),  #
                                'time'        : ev_obj.TimeGenerated.Format(),    #'12/23/99 15:54:09'
                                'hostname'    : str(ev_obj.ComputerName),
                                'message'  : msg}
                        all_events[ev_obj.EventType][ev_obj.SourceName][winerror.HRESULT_CODE(ev_obj.EventID)]['count'] += 1

except:
    pass




for k,v in all_events[0].items():
    for a,b in v.items():
        print u' Error Count: \t %s '.encode('GB18030')  %( b['count'] )
        for c,d in b['data'].items():
            print " %s:  \t %s " %(c,d)
        else:
            print
    else:
        print


for k,v in all_events[1].items():
    for a,b in v.items():
        print u' Error Count: \t %s '  %( b['count'] )
        for c,d in b['data'].items():
            print " %s: \t %s " %(c,d)
        else:
            print
    else:
        print


for k,v in all_events[2].items():
    for a,b in v.items():
        print u' Error Count: \t %s '  %( b['count'] )
        for c,d in b['data'].items():
            print " %s: \t %s " %(c,d)
        else:
            print
    else:
        print


for k,v in all_events[4].items():
    for a,b in v.items():
        print u' Error Count: \t %s '  %( b['count'] )
        for c,d in b['data'].items():
            print " %s: \t %s " %(c,d)
        else:
            print

    else:
        print

#syn-time --->info
print
print 'present-time is cn.pool ntp.org' 
import psutil
import ntplib
c = ntplib.NTPClient()  
response = c.request('pool.ntp.org') 
ts = response.tx_time  
_date = time.strftime('%Y-%m-%d',time.localtime(ts))  
_time = time.strftime('%X',time.localtime(ts))  
os.system('date {} && time {}'.format(_date,_time))


#log-security-info
system_handle = win32evtlog.OpenEventLog("localhost", "Security")
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
events = win32evtlog.ReadEventLog(system_handle, flags,0)
#logger = codecs.open('logger.txt', encoding='utf-8', mode='w')

print

#security-->info
all_events = {
        8 :   {},
        16 :  {},
    }

try:
    while 1:
        events = win32evtlog.ReadEventLog(system_handle, flags,0)
        if not events:
            break

        for ev_obj in events:
            msg = win32evtlogutil.SafeFormatMessage(ev_obj, 'Security')
            #print type(msg.encode('GB2312'))

            msg = msg.encode('GB18030')
            log_time = ev_obj.TimeGenerated.Format()
            log_time = log_time.split()[0]
            log_time = datetime.datetime.strptime(log_time,'%m/%d/%y')
            now_time = datetime.datetime.now()
            day = now_time - log_time


            if day.days <= 7:
                if len(msg):
                    if all_events.has_key(ev_obj.EventType):
                        if not all_events[ev_obj.EventType].has_key(ev_obj.SourceName):
                            all_events[ev_obj.EventType][ev_obj.SourceName] = {}

                        if not all_events[ev_obj.EventType][ev_obj.SourceName].has_key(winerror.HRESULT_CODE(ev_obj.EventID)):
                            all_events[ev_obj.EventType][ev_obj.SourceName][winerror.HRESULT_CODE(ev_obj.EventID)] = {'data':None,'count':0}
                            #print day.days
                        all_events[ev_obj.EventType][ev_obj.SourceName][winerror.HRESULT_CODE(ev_obj.EventID)]['data'] = {
                                'SourceName'  : str(ev_obj.SourceName),
                                'event_level' : ev_obj.EventType,
                                'event_id'    : winerror.HRESULT_CODE(ev_obj.EventID),  #
                                'time'        : ev_obj.TimeGenerated.Format(),    #'12/23/99 15:54:09'
                                'hostname'    : str(ev_obj.ComputerName),
                                'message'  : msg}
                        all_events[ev_obj.EventType][ev_obj.SourceName][winerror.HRESULT_CODE(ev_obj.EventID)]['count'] += 1

except:
    pass


for k,v in all_events[8].items():
    for a,b in v.items():
        print u' Error Count: \t %s '  %( b['count'] )
        for c,d in b['data'].items():
            print " %s \t %s " %(c,d)
        else:
            print

    else:
        print


for k,v in all_events[16].items():
    for a,b in v.items():
        print u' Error Count: \t %s '  %( b['count'] )
        for c,d in b['data'].items():
            print " %s: \t %s " %(c,d)
        else:
            print

    else:
        print











