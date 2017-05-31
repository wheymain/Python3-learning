# -*- coding:utf-8 -*-
#Threadlocal来解决线程间数据传递的问题

import threading

#local_school=threading.local()

def proc_stu(name):
#	local_school.stu=name
#	std=local_school.stu
	print('Hello, %s (in %s)'%(name,threading.current_thread().name))

t1=threading.Thread(target= proc_stu, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= proc_stu, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()