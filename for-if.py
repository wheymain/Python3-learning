# -*- coding:utf-8 -*-
#实现100以内质数的输出

x=2
while x<100:
	n=x//2
	if n==1:
	    print(x)
	else:
		a=n
		while a>0:
			m=x%a
			a=a-1
			if m==0:
				break
			if a==1:
				print(x)
				break
	x=x+1