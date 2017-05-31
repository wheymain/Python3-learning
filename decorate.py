# -*- coding:utf-8 -*-
#利用decorator在函数调用的前后打印出'begin call'和'end call'

import functools
from datetime import datetime

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():' %(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log('begin call')
def now():
	print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	print('end call')

now()