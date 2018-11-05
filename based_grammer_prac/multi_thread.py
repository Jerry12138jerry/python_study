#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 13:34
# @Author  : Jerry
# @Site    : 
# @File    : multi_thread.py
# @Software: PyCharm
import _thread
import time
# 为线程定义一个函数
def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count = +1
        print (threadName,time.ctime(time.time()))

try:
    _thread.start_new_thread(print_time,("Thread-1", 2 ))
    _thread.start_new_thread( print_time, ("Thread-2", 4 ) )
except:
    print ("Error: unable to start thread")

while 1:
    pass