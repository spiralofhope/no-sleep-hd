#!/usr/bin/python
#
# Description: Periodic read random sectors from hard drive. 
#              Keep external HD from going into sleep mode.
#
# Author:
#  Robin Chiu
# 
# idea : http://nosleephd.codeplex.com/
# reference code from internet:
# C1 http://stackoverflow.com/questions/13927889/show-non-printable-characters-in-a-string
# C2 http://stackoverflow.com/questions/911856/detecting-idle-time-using-python
# C3 http://code.activestate.com/recipes/475157-disk-dumper/
# C4 http://stackoverflow.com/questions/2398661/schedule-a-repeating-event-in-python-3


import os, sched, time, random, re, string, datetime
from ctypes import Structure, windll, c_uint, sizeof, byref ## for C2

EXT_DRIVE_NAME="G"
PERIOD_SECS=90

## C4

def periodic(scheduler, interval, action, actionargs=()):
	scheduler.enter(interval, 1, periodic,
        	(scheduler, interval, action, actionargs))
	action(*actionargs)


## C1

printable = string.ascii_letters + string.digits + string.punctuation + ' '
def hex_escape(s):
    ##return ''.join(c if c in printable else r'\x{0:02x}'.format(ord(c)) for c in s)
    return ''.join(c if c in printable else '-' for c in s)


## C2

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0
	

## C3
	
def raw_read(drive) :
	start = random.randrange(0, 1000) * 512
	
	print start

	if os.name == 'posix':
		f = file('/dev/' + drive)
	elif os.name == 'nt':
		f = file(r'\\.\%s:' % drive)

	f.seek(start)
	temp = f.read(512)
	f.close()
	print hex_escape(temp)
	
	
def do_wait_up() :
	print "From do_wait_up", time.time()
	idle = get_idle_duration()
	h = datetime.datetime.now().hour
	if idle < 600 and h >= 10 and h <= 19 :
		raw_read(EXT_DRIVE_NAME);
	

s = sched.scheduler(time.time, time.sleep)

def no_sleep_hd() :
	periodic(s, PERIOD_SECS, do_wait_up, ())
	s.run()

	
no_sleep_hd()

