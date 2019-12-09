# -*- coding: utf-8 -*-
import time

import datetime


def current_time():
    return long(time.time() * 1000)


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def format_full_datetime(value):
    try:
        time_int = int(value) / 1000
        time_str = datetime.datetime.fromtimestamp(time_int).strftime('%Y-%m-%d %H:%M:%S')
        return time_str
    except ValueError:
        return ''


def parse_time(val):
    try:
        mydate = datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
        val = int(time.mktime(mydate.timetuple()) * 1000)
    except ValueError:
        val = 0
    return val


def parse_time_by_minute(val):
    try:
        mydate = datetime.datetime.strptime(val, "%Y-%m-%d %H:%M")
        val = int(time.mktime(mydate.timetuple()) * 1000)
    except ValueError:
        val = -1
    return val
