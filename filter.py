# -*- coding:utf-8 -*-
#实现1000以内回数的输出

n=10   #第一种方法
while n<1000:
	n=n+1
	if n==int(str(n)[::-1]):
		print(n)

def is_palin(n):   #第二种方法
	if n==int(str(n)[::-1]):
		return n
prism=filter(is_palin,range(10,1000))
print (list(prism))