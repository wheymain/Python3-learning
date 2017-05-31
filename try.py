# -*- coding:utf-8 -*-
#利用try进行错误判断

def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s)*2

def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:',e)
	finally:
		print('End')

main()