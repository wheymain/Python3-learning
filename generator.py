# -*- coding:utf-8 -*-
#实现杨辉三角

def yang(max):
	L=[1]
	n=0
	while n<max:
		yield L
		L=[L[x]+L[x+1] for x in range(len(L)-1)]
		L.insert(0,1)
		L.append(1)
		n=n+1

for t in yang(10):
	print(t)