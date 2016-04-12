
#!/usr/bin/env python
"""
这里的代码已经能打印除windows system中除了
fatal 的信息 以外的所有信息


"""


import codecs
import os
import sys
import time
import traceback
import win32con
import win32evtlog
import win32evtlogutil
import winerror
import operator  
system_handle=win32evtlog.OpenEventLog("localhost", "System") 
flags=win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ 
allevents=win32evtlog.ReadEventLog(system_handle, flags,0) 

#print len(allevents)
L=[]
M=[]
J={}
N=[]
k=1
while 1: 
	events = win32evtlog.ReadEventLog(system_handle, flags,0) 
 #   print type(events)
	if not events:  
		break 
#    print events
	k=k+1
	#if k==30:
	 #   break
	#for k in events:
		#print type(k)
	for ev_obj in events:
  #          print 'this is ev_obj %s'%type(ev_obj)
		the_time = ev_obj.TimeGenerated.Format() #'12/23/99 15:54:09'
#            print the_time
		evt_id = str(winerror.HRESULT_CODE(ev_obj.EventID))
#            print  'this is events_id %s'%ev_obj.EventID
 #           print 'event-type is %d'%ev_obj.EventType
		computer = str(ev_obj.ComputerName)
		cat = ev_obj.EventCategory
		record = ev_obj.RecordNumber
		msg = win32evtlogutil.SafeFormatMessage(ev_obj, 'System')
		msg = msg.encode('GB18030')
		if ev_obj.EventType==0:
			#L.append(ev_obj.EventType)
			L.append(ev_obj.EventID)  
			print msg
			print ev_obj.EventID
			print ev_obj.EventType
			print the_time
			print 'service_name is  %s '%ev_obj.SourceName
			N.append({
						'event_id' : str(winerror.HRESULT_CODE(ev_obj.EventID)),  #
						'time'     : ev_obj.TimeGenerated.Format(),    #'12/23/99 15:54:09'
						'hostname' : str(ev_obj.ComputerName),
						'record'   : ev_obj.RecordNumber,   #
						'Eventcategory'  : ev_obj.EventCategory,
						'EventType': ev_obj.EventType,
						'message'  : msg})
			#J.append(str(winerror.HRESULT_CODE(ev_obj.EventID)),0)
sort=[]
for k in L:
    if k not in sort:
        sort.append(k) 	
#sort=[]
q=[]
b={}
#for k in L:
 #   j=0
 #   for d in L:
	 
#	 if k==d:
#	   j=j+1
	#sort.append[j]  
for i in sort:
   # print 'event %d  occur %d times'%(i,L.count(i)) 
    q.append({str(i):L.count(i)})
    b[str(i)]=L.count(i)
newb= sorted(b.iteritems(), key=operator.itemgetter(1))#对字典进行排序      
for  k in newb:
    print 'event %s occur %d times'%(k[0],k[1])

