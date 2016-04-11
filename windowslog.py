
import os
pyscript ="""

import codecs
import os
import sys
import time
import traceback
import win32con
import win32evtlog
import win32evtlogutil
import winerror
hand = win32evtlog.OpenEventLog('localhost','System')
total = win32evtlog.GetNumberOfEventLogRecords(hand)
print "Total events in %s = %s" % ('System', total)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
events = win32evtlog.ReadEventLog(hand,flags,0)
evt_dict={win32con.EVENTLOG_AUDIT_FAILURE:'EVENTLOG_AUDIT_FAILURE',
              win32con.EVENTLOG_AUDIT_SUCCESS:'EVENTLOG_AUDIT_SUCCESS',
              win32con.EVENTLOG_INFORMATION_TYPE:'EVENTLOG_INFORMATION_TYPE',
              win32con.EVENTLOG_WARNING_TYPE:'EVENTLOG_WARNING_TYPE',
              win32con.EVENTLOG_ERROR_TYPE:'EVENTLOG_ERROR_TYPE'}


try:
    events = 1
    while events:

        events=win32evtlog.ReadEventLog(hand,flags,0)
        for ev_obj in events:
            the_time = ev_obj.TimeGenerated.Format() #'12/23/99 15:54:09'
            print the_time
            evt_id = str(winerror.HRESULT_CODE(ev_obj.EventID))
            print ev_obj.EventID
            computer = str(ev_obj.ComputerName)
            cat = ev_obj.EventCategory
            record = ev_obj.RecordNumber
            msg = win32evtlogutil.SafeFormatMessage(ev_obj, 'System')
            msg = msg.encode('gb2312')
            print msg
except:
    pass

"""

with open('C:\\Users\\Administrator\\Downloads\\test.py','w') as f:
    f.write(pyscript)
result = os.popen('C:\\Python27\\python.exe C:\\Users\\Administrator\\Downloads\\test.py')
print result.read()
