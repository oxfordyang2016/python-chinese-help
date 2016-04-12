
#!/usr/bin/env python
#coding:utf8


import win32evtlog
import win32evtlogutila
import winerror
import datetime


system_handle = win32evtlog.OpenEventLog("localhost", "System")
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
events = win32evtlog.ReadEventLog(system_handle, flags,0)

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
            #msg = msg.encode('GB18030')
            #msg = msg.encode('GBK')
            #print ev_obj.Data
            #print ev_obj.EventType
            #print ev_obj.ComputerName
            #print ev_obj.EventCategory
            #print ev_obj.EventID
            #print ev_obj.RecordNumber
            #print ev_obj.SourceName
            #print ev_obj.TimeGenerated
            log_time = ev_obj.TimeGenerated.Format()
            log_time = log_time.split()[0]
            log_time = datetime.datetime.strptime(log_time,'%m/%d/%y')
            now_time = datetime.datetime.now()
            day = now_time - log_time


            if len(msg):
                if all_events.has_key(ev_obj.EventType):
                    if not all_events[ev_obj.EventType].has_key(ev_obj.SourceName):
                        all_events[ev_obj.EventType][str(ev_obj.SourceName)] = {'data':[],'count':0}

                    if day.days <= 7:
                        #print day.days
                        all_events[ev_obj.EventType][str(ev_obj.SourceName)]['data'].append({
                            'SourceName':str(ev_obj.SourceName),
                            'event_id' : str(winerror.HRESULT_CODE(ev_obj.EventID)),  #
                            'time'     : ev_obj.TimeGenerated.Format(),    #'12/23/99 15:54:09'
                            'hostname' : str(ev_obj.ComputerName),
                           #'record'   : str(ev_obj.RecordNumber),   #
                           #'Eventcategory'  : str(ev_obj.EventCategory),
                           #'EventType': ev_obj.EventType,

                            'message'  : msg})
                        all_events[ev_obj.EventType][ev_obj.SourceName]['count'] += 1
except Exception as e:
    print e


#致命错误
data = {}
for k,v in all_events[0].items():
    #print 'Error Type: {0}'.format(k)
    data[v['count']] = v['data']
for x,y in sorted(data.iteritems(),key=lambda t:t[0],reverse=True):
    print "Error Count: {0}".format(x)
    for k in y:
        for key,value in k.items():
            print key,value



#错误
data = {}
for k,v in all_events[1].items():
    #print k
    data[v['count']] = v['data']
for x,y in sorted(data.iteritems(),key=lambda t:t[0],reverse=True):
    print "Error Count: {0}".format(x)
    for k in y:
        for key,value in k.items():
            print key,value


#警告
data = {}
for k,v in all_events[2].items():
    #print k
    data[v['count']] = v['data']
for x,y in sorted(data.iteritems(),key=lambda t:t[0],reverse=True):
    print "Error Count: {0}".format(x)
    for k in y:
        for key,value in k.items():
            print key,value


#信息
data = {}
for k,v in all_events[4].items():
    #print k
    data[v['count']] = v['data']
for x,y in sorted(data.iteritems(),key=lambda t:t[0],reverse=True):
    print "Error Count: {0}".format(x)
    for k in y:
        for key,value in k.items():
            print key,value

