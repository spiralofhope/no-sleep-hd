#!/usr/bin/env python3
#
# Description: Periodically read random sectors from a hard drive to
#              keep an external HD from going into sleep mode.
#
# Author:
#  Robin Chiu
#
# Idea: http://nosleephd.codeplex.com/
# Reference code from the internet:
# C1 http://stackoverflow.com/questions/13927889/show-non-printable-characters-in-a-string
# C2 http://stackoverflow.com/questions/911856/detecting-idle-time-using-python
# C3 http://code.activestate.com/recipes/475157-disk-dumper/
# C4 http://stackoverflow.com/questions/2398661/schedule-a-repeating-event-in-python-3
#
# Updated to Python 3 by:
#   spiralofhope

import os
import sched
import time
import random
import re
import string
import datetime
import platform
import itertools
import sys
import threading

EXT_DRIVE_NAME = "B"
PERIOD_SECS = 90

def periodic(scheduler, interval, action, actionargs=()):
    scheduler.enter(interval, 1, periodic,
                    (scheduler, interval, action, actionargs))
    action(*actionargs)

printable = string.ascii_letters + string.digits + string.punctuation + ' '

def hex_escape(b):
    s = b.decode('latin1')
    return ''.join(c if c in printable else '-' for c in s)

if platform.system() == 'Windows':
    from ctypes import Structure, windll, c_uint, sizeof, byref
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
else:
    def get_idle_duration():
        return 0.0

def raw_read(drive):
    start = random.randrange(0, 1000) * 512
    sys.stdout.write(f'\r    Read sector: {start}')
    sys.stdout.flush()
    if os.name == 'posix':
        with open('/dev/' + drive, 'rb') as f:
            f.seek(start)
            temp = f.read(512)
    elif os.name == 'nt':
        with open(r'\\.\%s:' % drive, 'rb') as f:
            f.seek(start)
            temp = f.read(512)

def spinner():
    spinner_chars = itertools.cycle(['|', '/', '-', '\\'])
    while True:
        sys.stdout.write(f'\r{next(spinner_chars)}')
        sys.stdout.flush()
        time.sleep(1)

def do_wait_up():
    idle = get_idle_duration()
    h = datetime.datetime.now().hour
    if idle < 600 and 10 <= h <= 19:
        raw_read(EXT_DRIVE_NAME)

s = sched.scheduler(time.time, time.sleep)

def no_sleep_hd():
    threading.Thread(target=spinner, daemon=True).start()
    periodic(s, PERIOD_SECS, do_wait_up, ())
    s.run()

if __name__ == '__main__':
    no_sleep_hd()