# -*- coding:utf-8 -*-
#利用sorted函数对学生名字和成绩进行排序

def name(t):
	return t[0]
def score(t):
	return t[1]
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa', 88)]
L2=sorted(L,key=name)
print("按姓名排序：",L2)
L3=sorted(L,key=score,reverse=True)
print("按成绩排序：",L3)